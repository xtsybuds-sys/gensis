/* Genesis — live world viewer.

 *

 * Draws the running primordial dish: a shallow basin of water with three nutrient

 * patches, and the pilot's actual cells as enlarged motes. The sun comes from real

 * solar geometry computed by the gateway, so day and night here are the planet's.

 */



(() => {

  const canvas = document.getElementById('scene');

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

  renderer.setSize(window.innerWidth, window.innerHeight, false);

  renderer.shadowMap.enabled = true;

  renderer.shadowMap.type = THREE.PCFSoftShadowMap;



  const scene = new THREE.Scene();

  scene.fog = new THREE.FogExp2(0x0a1620, 0.028);



  const camera = new THREE.PerspectiveCamera(

    68, window.innerWidth / window.innerHeight, 0.05, 1200

  );

  camera.rotation.order = 'YXZ';

  camera.position.set(0, 1.72, 11.2);



  const DISH = 16.0;

  const HALF = DISH / 2;

  const POND_RADIUS = 8.6;



  // ---------------------------------------------------------------- sky & light

  const skyUniforms = {

    topColor: { value: new THREE.Color(0x3a7bd5) },

    bottomColor: { value: new THREE.Color(0xbfe3f2) },

    sunColor: { value: new THREE.Color(0xfff2c4) },

    sunDir: { value: new THREE.Vector3(0, 1, 0) },

    day: { value: 1.0 }

  };

  const sky = new THREE.Mesh(

    new THREE.SphereGeometry(500, 32, 24),

    new THREE.ShaderMaterial({

      uniforms: skyUniforms,

      side: THREE.BackSide,

      depthWrite: false,

      vertexShader: `

        varying vec3 vDir;

        void main() {

          vDir = normalize(position);

          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);

        }`,

      fragmentShader: `

        uniform vec3 topColor; uniform vec3 bottomColor; uniform vec3 sunColor;

        uniform vec3 sunDir; uniform float day;

        varying vec3 vDir;

        void main() {

          vec3 d = normalize(vDir);

          float t = clamp(d.y * 0.5 + 0.5, 0.0, 1.0);

          vec3 c = mix(bottomColor, topColor, pow(t, 0.75));

          float glow = pow(max(dot(d, normalize(sunDir)), 0.0), 48.0);

          c += sunColor * glow * clamp(day, 0.0, 1.0) * 1.6;

          float horizon = pow(1.0 - abs(d.y), 6.0);

          c += vec3(0.10, 0.16, 0.22) * horizon * (1.0 - clamp(day, 0.0, 1.0));

          gl_FragColor = vec4(c, 1.0);

        }`

    })

  );

  scene.add(sky);



  const sunLight = new THREE.DirectionalLight(0xfff1cf, 2.4);

  sunLight.castShadow = true;

  sunLight.shadow.mapSize.set(1024, 1024);

  sunLight.shadow.camera.left = -14;

  sunLight.shadow.camera.right = 14;

  sunLight.shadow.camera.top = 14;

  sunLight.shadow.camera.bottom = -14;

  sunLight.shadow.camera.far = 120;

  scene.add(sunLight);

  scene.add(sunLight.target);



  const hemi = new THREE.HemisphereLight(0x9fc8e8, 0x20303a, 0.55);

  scene.add(hemi);



  const sunDisc = new THREE.Mesh(

    new THREE.SphereGeometry(6, 16, 12),

    new THREE.MeshBasicMaterial({ color: 0xfff0b8 })

  );

  scene.add(sunDisc);



  const starGeo = new THREE.BufferGeometry();

  {

    const count = 900;

    const pos = new Float32Array(count * 3);

    let seed = 1234567;

    const rand = () => {

      seed = (seed * 1103515245 + 12345) & 0x7fffffff;

      return seed / 0x7fffffff;

    };

    for (let i = 0; i < count; i++) {

      const theta = rand() * Math.PI * 2;

      const phi = Math.acos(1 - rand() * 1.0);

      const r = 460;

      pos[i * 3] = r * Math.sin(phi) * Math.cos(theta);

      pos[i * 3 + 1] = Math.abs(r * Math.cos(phi)) + 30;

      pos[i * 3 + 2] = r * Math.sin(phi) * Math.sin(theta);

    }

    starGeo.setAttribute('position', new THREE.BufferAttribute(pos, 3));

  }

  const stars = new THREE.Points(

    starGeo,

    new THREE.PointsMaterial({ color: 0xdfe9ff, size: 1.4, sizeAttenuation: false,

                               transparent: true, opacity: 0.0, depthWrite: false })

  );

  scene.add(stars);



  // ---------------------------------------------------------------------- basin

  const basinMat = new THREE.MeshStandardMaterial({ color: 0x5b4a36, roughness: 1.0 });

  const basin = new THREE.Mesh(new THREE.CylinderGeometry(POND_RADIUS + 2.4, POND_RADIUS + 3.4, 0.9, 72, 1, true), basinMat);

  basin.position.y = -0.42;

  basin.receiveShadow = true;

  scene.add(basin);



  const rim = new THREE.Mesh(

    new THREE.RingGeometry(POND_RADIUS + 2.3, POND_RADIUS + 3.6, 72),

    new THREE.MeshStandardMaterial({ color: 0x6d6047, roughness: 1.0, side: THREE.DoubleSide })

  );

  rim.rotation.x = -Math.PI / 2;

  rim.position.y = 0.03;

  rim.receiveShadow = true;

  scene.add(rim);



  const floor = new THREE.Mesh(

    new THREE.CircleGeometry(POND_RADIUS + 2.4, 72),

    new THREE.MeshStandardMaterial({ color: 0x233832, roughness: 0.95 })

  );

  floor.rotation.x = -Math.PI / 2;

  floor.position.y = -0.30;

  floor.receiveShadow = true;

  scene.add(floor);



  // Nutrient field, refreshed from the live frame's coarse grid.

  const nutCanvas = document.createElement('canvas');

  nutCanvas.width = 16;

  nutCanvas.height = 16;

  const nutCtx = nutCanvas.getContext('2d');

  const nutImage = nutCtx.createImageData(16, 16);

  const nutTexture = new THREE.CanvasTexture(nutCanvas);

  nutTexture.magFilter = THREE.LinearFilter;

  nutTexture.minFilter = THREE.LinearFilter;

  const nutrientPlane = new THREE.Mesh(

    new THREE.PlaneGeometry(DISH, DISH),

    new THREE.MeshBasicMaterial({ map: nutTexture, transparent: true, opacity: 0.40,

                                  depthWrite: false })

  );

  nutrientPlane.rotation.x = -Math.PI / 2;

  nutrientPlane.position.y = -0.27;

  scene.add(nutrientPlane);



  const PATCH_CENTRES = [[4.0, 4.0], [12.0, 4.0], [8.0, 12.0]];

  const patchMeshes = PATCH_CENTRES.map(([px, py]) => {

    const mesh = new THREE.Mesh(

      new THREE.CircleGeometry(3.0, 48),

      new THREE.MeshBasicMaterial({ color: 0x39d0c8, transparent: true,

                                    opacity: 0.16, depthWrite: false })

    );

    mesh.rotation.x = -Math.PI / 2;

    mesh.position.set(px - HALF, -0.25, py - HALF);

    scene.add(mesh);

    return mesh;

  });



  // ---------------------------------------------------------------------- water

  const waterUniforms = {

    time: { value: 0 },

    sunDir: { value: new THREE.Vector3(0, 1, 0) },

    sunColor: { value: new THREE.Color(0xfff0c0) },

    day: { value: 1.0 },

    deep: { value: new THREE.Color(0x0d2f3c) },

    shallow: { value: new THREE.Color(0x2f8f8a) }

  };

  const water = new THREE.Mesh(

    new THREE.CircleGeometry(POND_RADIUS, 128),

    new THREE.ShaderMaterial({

      uniforms: waterUniforms,

      transparent: true,

      vertexShader: `

        varying vec2 vUv; varying vec3 vWorld;

        void main() {

          vUv = uv;

          vWorld = (modelMatrix * vec4(position, 1.0)).xyz;

          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);

        }`,

      fragmentShader: `

        uniform float time; uniform vec3 sunDir; uniform vec3 sunColor;

        uniform float day; uniform vec3 deep; uniform vec3 shallow;

        varying vec2 vUv; varying vec3 vWorld;

        void main() {

          vec2 p = vUv * 2.0 - 1.0;

          float r = length(p);

          float wave = sin(r * 22.0 - time * 2.4) * 0.5 + 0.5;

          float wave2 = sin(p.x * 14.0 + time * 1.3) * sin(p.y * 16.0 - time * 1.1);

          vec3 normal = normalize(vec3(wave2 * 0.16, 1.0, wave2 * 0.12));

          vec3 viewDir = normalize(cameraPosition - vWorld);

          float fres = pow(1.0 - max(dot(normal, viewDir), 0.0), 3.0);

          vec3 base = mix(deep, shallow, clamp(0.35 + wave * 0.3, 0.0, 1.0));

          vec3 halfV = normalize(normalize(sunDir) + viewDir);

          float spec = pow(max(dot(normal, halfV), 0.0), 220.0);

          float edge = smoothstep(0.94, 1.0, r);

          vec3 col = base + sunColor * spec * 5.0 + vec3(0.5, 0.75, 0.8) * edge * 0.25;

          col = mix(col, vec3(0.02, 0.05, 0.07), fres * (1.0 - clamp(day, 0.0, 1.0)) * 0.85);

          gl_FragColor = vec4(col, 0.80);

        }`

    })

  );

  water.rotation.x = -Math.PI / 2;

  water.position.y = 0.0;

  scene.add(water);



  // ---------------------------------------------------------------------- cells

  const MAX_CELLS = 400;

  const cellGeo = new THREE.SphereGeometry(1, 10, 8);

  const cellMat = new THREE.MeshStandardMaterial({

    roughness: 0.35, metalness: 0.05, emissive: 0x2f6f63, emissiveIntensity: 0.55

  });

  const cells = new THREE.InstancedMesh(cellGeo, cellMat, MAX_CELLS);

  cells.instanceMatrix.setUsage(THREE.DynamicDrawUsage);

  cells.castShadow = false;

  scene.add(cells);



  const dummy = new THREE.Object3D();

  const tint = new THREE.Color();

  let simCells = [];

  let simTime = 0;



  function lineageColor(lineage, energy) {

    const hue = (lineage * 0.6180339887) % 1.0;

    tint.setHSL(hue, 0.62, 0.42 + Math.min(energy, 2.0) * 0.12);

    return tint;

  }



  // ------------------------------------------------------------------ input

  const keys = new Set();

  let yaw = 0.0;

  let pitch = -0.12;

  let locked = false;

  let mode = 'world';



  const overlay = document.getElementById('overlay');

  const overlayStatus = document.getElementById('overlayStatus');

  const viewName = document.getElementById('viewName');



  const landing = new URLSearchParams(location.search);

  if (landing.get('from') === 'cosmos') {

    overlay.classList.add('hidden');

    viewName.textContent = 'SURFACE';
    camera.position.set(0.6, 1.35, 7.4);
    yaw = 0.28;
    pitch = -0.06;
    applyLook();

    const radius = landing.get('radius');

    const water = landing.get('water');

    if (radius) {

      document.getElementById('hint').textContent =

        'first world · orbit ' + radius + (water ? ' · water ' + water : '') +

        ' · click to look · WASD move · M map';

    }

  }



  document.addEventListener('keydown', (e) => {

    keys.add(e.code);

    if (e.code === 'KeyM') toggleMode();

  });

  document.addEventListener('keyup', (e) => keys.delete(e.code));



  function applyLook() {

    camera.rotation.y = yaw;

    camera.rotation.x = pitch;

  }

  applyLook();



  document.addEventListener('mousemove', (e) => {

    if (!locked || mode !== 'world') return;

    yaw -= e.movementX * 0.0022;

    pitch -= e.movementY * 0.0022;

    pitch = Math.max(-1.35, Math.min(1.35, pitch));

    applyLook();

  });



  document.getElementById('enter').addEventListener('click', () => {

    overlay.classList.add('hidden');

    if (mode === 'world') canvas.requestPointerLock();

  });



  document.addEventListener('pointerlockchange', () => {

    locked = document.pointerLockElement === canvas;

  });



  canvas.addEventListener('click', () => {

    if (mode === 'world') canvas.requestPointerLock();

  });



  function toggleMode() {

    mode = mode === 'world' ? 'map' : 'world';

    viewName.textContent = mode === 'world' ? 'WORLD VIEW' : 'COMMAND CENTER';

    if (mode === 'map') {

      document.exitPointerLock();

      camera.position.set(0, 26, 0.6);

      camera.lookAt(0, 0, 0);

    } else {

      camera.position.set(0, 1.72, 11.2);

      yaw = 0.0;

      pitch = -0.12;

      applyLook();

    }

  }



  // ------------------------------------------------------------------ gateway

  let lastFrameAt = 0;

  let pollTimer = null;



  function applyPayload(data) {

    const sim = data.sim || {};

    if (sim.cells) simCells = sim.cells;

    if (sim.tick !== undefined) simTime = sim.tick;

    lastFrameAt = performance.now();



    document.getElementById('pop').textContent = (sim.population == null ? '—' : sim.population);

    document.getElementById('turn').textContent = (sim.turnovers == null ? 0 : sim.turnovers).toFixed(0);

    document.getElementById('gen').textContent = (sim.max_gen == null ? '—' : sim.max_gen);

    document.getElementById('lin').textContent = (sim.lineages == null ? '—' : sim.lineages);

    document.getElementById('size').textContent = (sim.mean_size == null ? 0 : sim.mean_size).toFixed(2);

    document.getElementById('speed').textContent = (sim.mean_speed == null ? 0 : sim.mean_speed).toFixed(3);

    document.getElementById('status').textContent = sim.tick

      ? `live · tick ${sim.tick} · ${data.source}`

      : 'waiting for the simulation…';



    const sun = data.sun;

    if (sun) {

      const dir = new THREE.Vector3(...sun.direction);

      const elevation = sun.elevation_deg;

      document.getElementById('elev').textContent = `${elevation.toFixed(1)}°`;

      const hours = sun.solar_time_hours;

      const hh = Math.floor(hours);

      const mm = Math.floor((hours - hh) * 60);

      document.getElementById('ptime').textContent =

        String(hh).padStart(2, '0') + ':' + String(mm).padStart(2, '0');

      const day = THREE.MathUtils.clamp((elevation + 4.0) / 20.0, 0.0, 1.0);

      skyUniforms.day.value = day;

      waterUniforms.day.value = day;

      waterUniforms.sunDir.value.copy(dir);

      skyUniforms.sunDir.value.copy(dir);

      sunLight.position.copy(dir).multiplyScalar(60);

      sunLight.intensity = 0.25 + day * 2.3;

      sunDisc.position.copy(dir).multiplyScalar(430);

      sunDisc.visible = elevation > -3;

      stars.material.opacity = 1.0 - day;

      hemi.intensity = 0.15 + day * 0.5;

      const top = new THREE.Color(0x3a7bd5).lerp(new THREE.Color(0x03060f), 1 - day);

      const bottom = new THREE.Color(0xbfe3f2).lerp(new THREE.Color(0x0a1a26), 1 - day);

      skyUniforms.topColor.value.copy(top);

      skyUniforms.bottomColor.value.copy(bottom);

      const fogTarget = new THREE.Color(0x0a1620).lerp(new THREE.Color(0x9ec9d8), day);

      scene.fog.color.copy(fogTarget);

    }



    if (sim.nutrient) {

      const n = sim.nutrient;

      for (let i = 0; i < 256; i++) {

        const v = Math.max(0, Math.min(100, (n[i] == null ? 0 : n[i]))) / 100;

        const idx = i * 4;

        nutImage.data[idx] = 30 + v * 40;

        nutImage.data[idx + 1] = 120 + v * 120;

        nutImage.data[idx + 2] = 120 + v * 80;

        nutImage.data[idx + 3] = 170 + v * 60;

      }

      nutCtx.putImageData(nutImage, 0, 0);

      nutTexture.needsUpdate = true;

      patchMeshes.forEach((mesh, index) => {

        const [cx, cy] = PATCH_CENTRES[index];

        let sum = 0, count = 0;

        for (let j = 0; j < 16; j++) {

          for (let i = 0; i < 16; i++) {

            const wx = (i + 0.5), wy = (j + 0.5);

            if (Math.hypot(wx - cx, wy - cy) <= 3.0) { sum += n[j * 16 + i]; count++; }

          }

        }

        mesh.material.opacity = 0.10 + 0.55 * (count ? (sum / count) / 100 : 0);

      });

    }



    if (overlayStatus.textContent.includes('waiting')) {

      overlayStatus.textContent = `live · ${sim.population} cells · generation ${sim.max_gen}`;

    }

  }



  function connect() {

    const source = new EventSource('/api/stream');

    source.onmessage = (event) => {

      try { applyPayload(JSON.parse(event.data)); } catch (err) { /* keep last frame */ }

    };

    source.onerror = () => {

      source.close();

      if (pollTimer) return;

      pollTimer = setInterval(async () => {

        try {

          const res = await fetch('/api/world', { cache: 'no-store' });

          applyPayload(await res.json());

        } catch (err) { /* server restarting */ }

      }, 700);

      setTimeout(() => {

        clearInterval(pollTimer);

        pollTimer = null;

        connect();

      }, 6000);

    };

  }

  connect();



  // ---------------------------------------------------------------------- loop

  const clock = new THREE.Clock();

  let frames = 0;

  let fpsAt = performance.now();



  function animate() {

    requestAnimationFrame(animate);

    const dt = Math.min(clock.getDelta(), 0.05);

    const t = clock.elapsedTime;

    waterUniforms.time.value = t;



    if (mode === 'world') {

      const speed = (keys.has('ShiftLeft') || keys.has('ShiftRight')) ? 7.0 : 3.0;

      let fx = 0, fz = 0;

      if (keys.has('KeyW')) fz -= 1;

      if (keys.has('KeyS')) fz += 1;

      if (keys.has('KeyA')) fx -= 1;

      if (keys.has('KeyD')) fx += 1;

      if (fx || fz) {

        const len = Math.hypot(fx, fz);

        fx /= len; fz /= len;

        const sin = Math.sin(yaw), cos = Math.cos(yaw);

        camera.position.x += (fx * cos + fz * sin) * speed * dt;

        camera.position.z += (fz * cos - fx * sin) * speed * dt;

        const r = Math.hypot(camera.position.x, camera.position.z);

        if (r > 13.5) {

          camera.position.x *= 13.5 / r;

          camera.position.z *= 13.5 / r;

        }

      }

      camera.position.y = 1.72 + Math.sin(t * 0.8) * 0.02;

    }



    // Draw the real cells, enlarged. Position is the simulation's; the size is scaled.

    const count = Math.min(simCells.length, MAX_CELLS);

    for (let i = 0; i < count; i++) {

      const c = simCells[i];

      const x = c[0] - HALF;

      const z = c[1] - HALF;

      const size = 0.09 + c[2] * 0.055;

      const bob = Math.sin(t * 1.6 + i * 0.7) * 0.02;

      dummy.position.set(x, 0.05 + bob, z);

      dummy.scale.setScalar(size);

      dummy.updateMatrix();

      cells.setMatrixAt(i, dummy.matrix);

      cells.setColorAt(i, lineageColor(c[4], c[3]));

    }

    cells.count = count;

    cells.instanceMatrix.needsUpdate = true;

    if (cells.instanceColor) cells.instanceColor.needsUpdate = true;



    renderer.render(scene, camera);



    frames++;

    const now = performance.now();

    if (now - fpsAt > 500) {

      document.getElementById('fps').textContent =

        Math.round((frames * 1000) / (now - fpsAt));

      frames = 0;

      fpsAt = now;

    }

    if (now - lastFrameAt > 4000 && lastFrameAt > 0) {

      document.getElementById('status').textContent = 'gateway silent — retrying';

    }

  }

  animate();



  // Read-only handle for automated checks; the viewer itself never depends on it.

  window.__genesis = {

    camera,

    get mode() { return mode; },

    get cells() { return simCells.length; },

    get locked() { return locked; }

  };



  window.addEventListener('resize', () => {

    camera.aspect = window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth, window.innerHeight, false);

  });

})();

