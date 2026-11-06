/* Genesis — cosmogony viewer.
 *
 * Renders the reduced model in genesis/cosmos/cosmogony.py: an expanding cloud,
 * gravitational collapse, star ignition, a disk, planets, and the first water-bearing
 * planet inside the habitable zone, which the camera then follows. All positions come
 * from the model; nothing is drawn that the model did not produce.
 */

(() => {
  const canvas = document.getElementById('scene');
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(window.innerWidth, window.innerHeight, false);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
    55, window.innerWidth / window.innerHeight, 0.01, 200
  );
  camera.position.set(0, 0.6, 2.6);

  // ------------------------------------------------------------------ star field
  {
    const count = 1200;
    const positions = new Float32Array(count * 3);
    let seed = 99;
    const rand = () => {
      seed = (seed * 1103515245 + 12345) & 0x7fffffff;
      return seed / 0x7fffffff;
    };
    for (let i = 0; i < count; i++) {
      const theta = rand() * Math.PI * 2;
      const phi = Math.acos(1 - 2 * rand());
      const r = 40 + rand() * 40;
      positions[i * 3] = r * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = r * Math.cos(phi);
      positions[i * 3 + 2] = r * Math.sin(phi) * Math.sin(theta);
    }
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    scene.add(new THREE.Points(geometry, new THREE.PointsMaterial({
      color: 0xdfe9ff, size: 1.4, sizeAttenuation: false, transparent: true,
      opacity: 0.85, depthWrite: false
    })));
  }

  // --------------------------------------------------------------------- matter
  const MAX_POINTS = 640;
  const cloudGeo = new THREE.BufferGeometry();
  const cloudPos = new Float32Array(MAX_POINTS * 3);
  const cloudCol = new Float32Array(MAX_POINTS * 3);
  cloudGeo.setAttribute('position', new THREE.BufferAttribute(cloudPos, 3));
  cloudGeo.setAttribute('color', new THREE.BufferAttribute(cloudCol, 3));
  cloudGeo.setDrawRange(0, 0);
  const cloud = new THREE.Points(cloudGeo, new THREE.PointsMaterial({
    size: 0.022, vertexColors: true, transparent: true, opacity: 0.9,
    blending: THREE.AdditiveBlending, depthWrite: false
  }));
  scene.add(cloud);

  const star = new THREE.Mesh(
    new THREE.SphereGeometry(1, 24, 16),
    new THREE.MeshBasicMaterial({ color: 0xfff2c8 })
  );
  scene.add(star);
  const starLight = new THREE.PointLight(0xfff0c0, 2, 12, 1.3);
  scene.add(starLight);
  scene.add(new THREE.AmbientLight(0x203040, 0.6));

  // The focus world, drawn on its own so the close-up never depends on instancing.
  function worldTexture() {
    const width = 512;
    const height = 256;
    const surface = document.createElement('canvas');
    surface.width = width;
    surface.height = height;
    const context = surface.getContext('2d');
    const image = context.createImageData(width, height);
    let seed = 1234567;
    const rand = () => {
      seed = (seed * 1103515245 + 12345) & 0x7fffffff;
      return seed / 0x7fffffff;
    };
    const waves = [];
    for (let i = 0; i < 9; i++) {
      waves.push({
        fx: 1 + Math.floor(rand() * 7), fy: 1 + Math.floor(rand() * 4),
        px: rand() * 6.283, py: rand() * 6.283, amp: 0.5 / (i + 1)
      });
    }
    for (let y = 0; y < height; y++) {
      const v = y / height;
      for (let x = 0; x < width; x++) {
        const u = x / width;
        let n = 0;
        for (const wave of waves) {
          n += wave.amp * Math.sin(u * 6.283 * wave.fx + wave.px)
                        * Math.cos(v * 6.283 * wave.fy + wave.py);
        }
        n = n * 1.4 + 0.5;
        const polar = Math.abs(v - 0.5) * 2;
        let r; let g; let b;
        if (polar > 0.86) { r = 226; g = 236; b = 244; }
        else if (n < 0.46) { r = 10; g = 42; b = 92; }
        else if (n < 0.52) { r = 18; g = 74; b = 120; }
        else if (n < 0.57) { r = 40; g = 116; b = 128; }
        else if (n < 0.63) { r = 74; g = 108; b = 70; }
        else { r = 104; g = 104; b = 82; }
        const index = (y * width + x) * 4;
        image.data[index] = r;
        image.data[index + 1] = g;
        image.data[index + 2] = b;
        image.data[index + 3] = 255;
      }
    }
    context.putImageData(image, 0, 0);
    const texture = new THREE.CanvasTexture(surface);
    texture.colorSpace = THREE.SRGBColorSpace;
    return texture;
  }

  const focusMesh = new THREE.Mesh(
    new THREE.SphereGeometry(1, 32, 24),
    new THREE.MeshStandardMaterial({
      map: worldTexture(), roughness: 0.72, metalness: 0.02,
      emissive: 0x04121f, emissiveIntensity: 0.5
    })
  );
  focusMesh.visible = false;
  scene.add(focusMesh);

  const MAX_PLANETS = 16;
  const planets = new THREE.InstancedMesh(
    new THREE.SphereGeometry(1, 20, 14),
    new THREE.MeshStandardMaterial({ roughness: 0.62, metalness: 0.05 }),
    MAX_PLANETS
  );
  planets.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  planets.count = 0;
  scene.add(planets);

  const orbitGroup = new THREE.Group();
  scene.add(orbitGroup);

  const hzRing = new THREE.Mesh(
    new THREE.RingGeometry(1, 1.2, 96),
    new THREE.MeshBasicMaterial({
      color: 0x3fe0c0, transparent: true, opacity: 0.10,
      side: THREE.DoubleSide, depthWrite: false
    })
  );
  hzRing.rotation.x = -Math.PI / 2;
  scene.add(hzRing);

  const dummy = new THREE.Object3D();
  const tint = new THREE.Color();
  let state = null;
  let focusPos = null;
  let orbitKey = '';

  // -------------------------------------------------------------------- input
  const params = new URLSearchParams(location.search);
  const frozen = params.has('tau') ? parseFloat(params.get('tau')) : null;

  // --------------------------------------------------------------------- feed
  async function poll() {
    const url = frozen !== null
      ? '/api/cosmos?tau=' + encodeURIComponent(frozen)
      : '/api/cosmos';
    try {
      const response = await fetch(url, { cache: 'no-store' });
      apply(await response.json());
    } catch (err) {
      document.getElementById('status').textContent = 'gateway silent — retrying';
    }
  }

  function apply(data) {
    state = data;
    const el = (id) => document.getElementById(id);
    el('phase').textContent = data.phase;
    el('tau').textContent = (data.tau * 100).toFixed(0) + '%';
    el('star').textContent = data.star_mass.toFixed(3);
    el('planets').textContent = data.planets.length;
    el('hz').textContent = data.hz[0].toFixed(2) + '–' + data.hz[1].toFixed(2);
    el('focus').textContent = data.phase === 'life' && data.focus
      ? data.focus.water.toFixed(2) + ' at ' + data.focus.radius.toFixed(2)
      : 'searching…';
    el('status').textContent = 'live · ' + data.source;

    const banner = document.getElementById('banner');
    if (data.phase === 'life') {
      banner.classList.add('show');
      document.getElementById('bannerSub').textContent =
        'water fraction ' + data.focus.water.toFixed(2) +
        ' · orbit ' + data.focus.radius.toFixed(2) + ' · in the habitable zone';
    } else {
      banner.classList.remove('show');
    }

    const flash = document.getElementById('flash');
    flash.style.opacity = data.tau < 0.02 ? String(1 - data.tau / 0.02) : '0';

    const count = Math.min(data.points.length, MAX_POINTS);
    const hot = data.phase === 'expansion' || data.phase === 'collapse';
    for (let i = 0; i < count; i++) {
      const point = data.points[i];
      cloudPos[i * 3] = point[0];
      cloudPos[i * 3 + 1] = point[1];
      cloudPos[i * 3 + 2] = point[2];
      if (hot) {
        const heat = 1.0 - Math.min(1.0, data.tau / 0.4);
        tint.setRGB(1.0, 0.55 + 0.4 * (1 - heat), 0.25 + 0.6 * (1 - heat));
      } else if (point[4] === 1) {
        tint.setRGB(0.35, 0.62, 1.0);
      } else {
        tint.setRGB(0.85, 0.80, 0.72);
      }
      cloudCol[i * 3] = tint.r;
      cloudCol[i * 3 + 1] = tint.g;
      cloudCol[i * 3 + 2] = tint.b;
    }
    cloudGeo.setDrawRange(0, count);
    cloudGeo.attributes.position.needsUpdate = true;
    cloudGeo.attributes.color.needsUpdate = true;

    const starSize = Math.max(0.010, data.star_radius * 1.2);
    star.scale.setScalar(starSize);
    starLight.intensity = 0.8 + data.star_mass * 2.2;

    hzRing.scale.set(data.hz[1], data.hz[1], 1);
    const inner = data.hz[0] / Math.max(data.hz[1], 1e-6);
    hzRing.geometry.dispose();
    hzRing.geometry = new THREE.RingGeometry(inner, 1.0, 96);

    const key = data.planets.map((p) => p.radius.toFixed(3)).join(',');
    if (key !== orbitKey) {
      orbitKey = key;
      while (orbitGroup.children.length) {
        const child = orbitGroup.children.pop();
        child.geometry.dispose();
        child.material.dispose();
      }
      for (const planet of data.planets) {
        const segments = 128;
        const positions = new Float32Array((segments + 1) * 3);
        for (let i = 0; i <= segments; i++) {
          const angle = (i / segments) * Math.PI * 2;
          positions[i * 3] = Math.cos(angle) * planet.radius;
          positions[i * 3 + 1] = 0;
          positions[i * 3 + 2] = Math.sin(angle) * planet.radius;
        }
        const geometry = new THREE.BufferGeometry();
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        orbitGroup.add(new THREE.Line(geometry, new THREE.LineBasicMaterial({
          color: planet.in_hz ? 0x2f8f80 : 0x2a3a46, transparent: true, opacity: 0.55
        })));
      }
    }

    planets.count = Math.min(data.planets.length, MAX_PLANETS);
    focusPos = null;
    data.planets.forEach((planet, index) => {
      if (index >= MAX_PLANETS) return;
      const x = Math.cos(planet.angle) * planet.radius;
      const z = Math.sin(planet.angle) * planet.radius;
      const radius = (0.018 + planet.mass * 0.35) * (planet.focus ? 1.8 : 1.0);
      dummy.position.set(x, 0, z);
      dummy.scale.setScalar(radius);
      dummy.updateMatrix();
      planets.setMatrixAt(index, dummy.matrix);
      tint.setHSL(0.58 - planet.water * 0.12, 0.55, 0.35 + planet.water * 0.25);
      planets.setColorAt(index, tint);
      if (planet.focus) focusPos = new THREE.Vector3(x, 0, z);
    });
    focusMesh.visible = data.phase === 'life' && focusPos !== null;
    if (focusPos) {
      focusMesh.position.copy(focusPos);
      focusMesh.scale.setScalar(0.055);
      focusMesh.rotation.y += 0.0015;
    }
    planets.instanceMatrix.needsUpdate = true;
    if (planets.instanceColor) planets.instanceColor.needsUpdate = true;

    updateCamera(data);
  }

  // ------------------------------------------------------------------- camera
  let cameraTarget = new THREE.Vector3(0, 0, 0);

  function updateCamera(data) {
    let wanted = new THREE.Vector3(0, 0.9, 2.6);
    let look = new THREE.Vector3(0, 0, 0);
    if (data.phase === 'expansion') {
      wanted.set(0, 0.5, 2.4);
    } else if (data.phase === 'collapse') {
      wanted.set(0, 0.8, 2.7);
    } else if (data.phase === 'ignition') {
      wanted.set(0, 0.7, 2.1);
    } else if (data.phase === 'disk') {
      wanted.set(0, 1.15, 2.0);
    } else if (data.phase === 'planets') {
      wanted.set(0, 1.05, 2.5);
    } else if (data.phase === 'life' && focusPos) {
      // Sit inside the orbit: the star lights the near face of the planet.
      const tangent = new THREE.Vector3(-focusPos.z, 0, focusPos.x).normalize();
      wanted.copy(focusPos).addScaledVector(tangent, 0.40).add(new THREE.Vector3(0, 0.10, 0));
      look.copy(focusPos);
    }
    camera.position.lerp(wanted, 0.06);
    cameraTarget.lerp(look, 0.08);
    camera.lookAt(cameraTarget);
  }

  // --------------------------------------------------------------------- loop
  let frames = 0;
  let fpsAt = performance.now();
  function animate() {
    requestAnimationFrame(animate);
    const t = performance.now() * 0.001;
    if (state && state.phase !== 'life') {
      scene.rotation.y = Math.sin(t * 0.05) * 0.04;
    } else {
      scene.rotation.y = 0;
    }
    renderer.render(scene, camera);
    frames++;
    const now = performance.now();
    if (now - fpsAt > 500) {
      document.getElementById('fps').textContent =
        Math.round((frames * 1000) / (now - fpsAt));
      frames = 0;
      fpsAt = now;
    }
  }

  window.__cosmos = {
    get state() { return state; },
    get phase() { return state ? state.phase : null; },
    get tau() { return state ? state.tau : null; },
    get planets() { return state ? state.planets.length : -1; },
    get star() { return state ? state.star_mass : null; }
    , get cam() { return camera.position.toArray(); }
    , get target() { return cameraTarget.toArray(); }
    , get focusPos() { return focusPos ? focusPos.toArray() : null; }
  };

  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight, false);
  });

  poll();
  setInterval(poll, 100);
  animate();
})();
