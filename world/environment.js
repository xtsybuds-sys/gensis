/* Genesis - early-Earth shelf around the live protocell pond.
 *
 * Presentation only. The reactor is well-mixed and has no terrain state; this
 * module builds a mineral shore, shelf, boulders, vents, distant volcanoes and
 * clouds so the chemistry sits in a place rather than on a black plane.
 */
(() => {
  const THREE = window.THREE;
  const world = window.__genesisWorld;
  if (!THREE || !world || !world.scene) return;

  const { scene, camera, POND_RADIUS } = world;
  const group = new THREE.Group();
  group.name = 'early-earth-shelf';
  scene.add(group);

  // A little airborne fill keeps the shadowed ridge faces readable.
  const skyFill = new THREE.AmbientLight(0x84968e, 0.28);
  skyFill.name = 'shelf-sky-fill';
  scene.add(skyFill);

  const faceFill = new THREE.DirectionalLight(0xa3b8b1, 0.45);
  faceFill.name = 'shelf-face-fill';
  faceFill.position.set(10, 18, 12);
  faceFill.target.position.set(0, 0, -30);
  scene.add(faceFill);
  scene.add(faceFill.target);

  const TAU = Math.PI * 2;
  const clamp01 = (x) => Math.max(0, Math.min(1, x));
  const smooth = (a, b, x) => {
    const t = clamp01((x - a) / (b - a));
    return t * t * (3 - 2 * t);
  };
  const mix = (a, b, t) => a + (b - a) * t;

  // Deterministic layout: the shelf looks the same after every reload.
  let seed = 0x9e3779b9;
  const rand = () => {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const hash = (x, z) => {
    const n = Math.sin(x * 127.1 + z * 311.7) * 43758.5453;
    return n - Math.floor(n);
  };

  // A shallow shelf that climbs into ridges, with a clear flat apron near the
  // pond. The camera never leaves a 13.5-unit radius, so the apron stays low.
  function heightAt(r, a) {
    const apron = smooth(11.8, 18.0, r) * 0.38;
    const foothill = smooth(15.0, 38.0, r) *
      (1.8 + 1.2 * Math.sin(a * 3.1 + 0.8) + 0.7 * Math.sin(a * 7.0 - 1.2));
    const ridge = smooth(28.0, 85.0, r) *
      (4.5 + 3.2 * Math.sin(a * 2.1 + 1.0) + 2.4 * Math.sin(a * 5.7 - 0.6));
    const far = smooth(65.0, 130.0, r) * 7.0 *
      (0.55 + 0.45 * Math.sin(a * 1.7 + 2.4));
    const grain = (hash(Math.floor(r * 0.55), Math.floor(a * 9.0)) - 0.5) *
      0.75 * smooth(12.0, 24.0, r);
    return -0.10 + apron + foothill + ridge + far + grain;
  }

  // Let the ridges read at distance instead of disappearing into the old murk.
  if (scene.fog) scene.fog.density = 0.0075;

  // ---------------------------------------------------------------- shelf body
  const terrainGeo = new THREE.RingGeometry(11.45, 140, 176, 72);
  const terrainPos = terrainGeo.attributes.position;
  const terrainColors = [];
  for (let i = 0; i < terrainPos.count; i++) {
    const x = terrainPos.getX(i);
    const y = terrainPos.getY(i);
    const r = Math.hypot(x, y);
    const a = Math.atan2(y, x);
    const h = heightAt(r, a);
    terrainPos.setZ(i, h);

    const n = hash(Math.floor(x * 0.4), Math.floor(y * 0.4));
    const c = new THREE.Color();
    if (h < 0.55) {
      c.setHSL(0.085, 0.24, 0.17 + n * 0.10);
    } else if (h < 3.5) {
      c.setHSL(0.070, 0.22, 0.19 + n * 0.12);
    } else {
      c.setHSL(0.075, 0.11, 0.14 + n * 0.10);
      if (n > 0.84) c.setHSL(0.27, 0.09, 0.16 + n * 0.05);
    }
    terrainColors.push(c.r, c.g, c.b);
  }
  terrainGeo.setAttribute('color', new THREE.Float32BufferAttribute(terrainColors, 3));
  terrainGeo.computeVertexNormals();
  const terrain = new THREE.Mesh(terrainGeo, new THREE.MeshStandardMaterial({
    vertexColors: true,
    roughness: 0.97,
    metalness: 0.0,
    flatShading: true
  }));
  terrain.name = 'shelf-terrain';
  terrain.rotation.x = -Math.PI / 2;
  terrain.receiveShadow = true;
  group.add(terrain);

  // Dark earth under the inner hole keeps the camera's feet from showing void.
  const underlay = new THREE.Mesh(
    new THREE.CircleGeometry(19, 64),
    new THREE.MeshStandardMaterial({ color: 0x24231d, roughness: 1.0 })
  );
  underlay.name = 'shelf-underlay';
  underlay.rotation.x = -Math.PI / 2;
  underlay.position.y = -0.44;
  underlay.receiveShadow = true;
  group.add(underlay);

  // A wet, pebbly beach covers the old artificial rim at the waterline.
  const shoreGeo = new THREE.RingGeometry(10.35, 13.05, 160, 8);
  const shorePos = shoreGeo.attributes.position;
  const shoreColors = [];
  for (let i = 0; i < shorePos.count; i++) {
    const x = shorePos.getX(i);
    const y = shorePos.getY(i);
    const r = Math.hypot(x, y);
    const a = Math.atan2(y, x);
    const grain = 0.012 * Math.sin(a * 13.0 + r * 3.2) +
      0.007 * Math.sin(a * 29.0 - r * 1.4);
    shorePos.setZ(i, grain + 0.018 * Math.sin(a * 3.5 + r * 0.55));
    const c = new THREE.Color().setHSL(
      0.075,
      0.25,
      mix(0.24, 0.13, smooth(10.4, 11.2, r)) + hash(x, y) * 0.05
    );
    shoreColors.push(c.r, c.g, c.b);
  }
  shoreGeo.setAttribute('color', new THREE.Float32BufferAttribute(shoreColors, 3));
  shoreGeo.computeVertexNormals();
  const shore = new THREE.Mesh(shoreGeo, new THREE.MeshStandardMaterial({
    vertexColors: true,
    roughness: 0.98,
    metalness: 0.0,
    side: THREE.DoubleSide
  }));
  shore.name = 'shelf-shore';
  shore.rotation.x = -Math.PI / 2;
  shore.position.y = 0.035;
  shore.receiveShadow = true;
  group.add(shore);

  // A wet mineral apron softens the old hard waterline.
  const apron = new THREE.Mesh(
    new THREE.RingGeometry(POND_RADIUS - 0.05, 10.55, 128, 4),
    new THREE.MeshStandardMaterial({
      color: 0x3b3a2d,
      roughness: 1.0,
      metalness: 0.0,
      side: THREE.DoubleSide
    })
  );
  apron.name = 'shelf-wet-apron';
  apron.rotation.x = -Math.PI / 2;
  apron.position.y = 0.009;
  apron.receiveShadow = true;
  group.add(apron);

  // ------------------------------------------------------------ boulders + stones
  const rockGeo = new THREE.DodecahedronGeometry(1, 0);
  const rockMat = new THREE.MeshStandardMaterial({
    color: 0xffffff,
    roughness: 0.95,
    metalness: 0.02,
    flatShading: true
  });
  const rockCount = 84;
  const rocks = new THREE.InstancedMesh(rockGeo, rockMat, rockCount);
  rocks.name = 'shelf-boulders';
  rocks.castShadow = true;
  rocks.receiveShadow = true;
  const dummy = new THREE.Object3D();
  const tint = new THREE.Color();
  for (let i = 0; i < rockCount; i++) {
    const a = rand() * TAU;
    const r = 12.15 + Math.pow(rand(), 0.72) * 17.0;
    let s = 0.16 + Math.pow(rand(), 2.0) * 0.92;
    if (r < 13.55) s *= 0.62;
    const base = r < 13.2 ? 0.055 : heightAt(r, Math.atan2(Math.sin(a) * r, Math.cos(a) * r));
    dummy.position.set(
      Math.cos(a) * r,
      base + s * 0.28,
      Math.sin(a) * r
    );
    dummy.rotation.set(rand() * 1.2, rand() * TAU, rand() * 0.8);
    dummy.scale.set(s * (0.85 + rand() * 0.5), s * (0.55 + rand() * 0.45), s * (0.8 + rand() * 0.4));
    dummy.updateMatrix();
    rocks.setMatrixAt(i, dummy.matrix);
    tint.setHSL(0.07 + rand() * 0.025, 0.05 + rand() * 0.10, 0.30 + rand() * 0.17);
    rocks.setColorAt(i, tint);
  }
  rocks.instanceMatrix.needsUpdate = true;
  if (rocks.instanceColor) rocks.instanceColor.needsUpdate = true;
  group.add(rocks);

  // A few big outcrops break the circular shore into landmarks.
  const outcropMat = new THREE.MeshStandardMaterial({
    color: 0x605b4d,
    roughness: 0.98,
    metalness: 0.02,
    flatShading: true
  });
  const outcropSpecs = [
    [-8.2, -11.8, 1.35],
    [8.0, -11.5, 1.05],
    [-12.6, -6.8, 1.55],
    [12.8, -5.2, 1.20],
    [-12.0, 3.4, 1.10],
    [12.4, 3.8, 0.90],
    [-6.8, -13.4, 0.78],
    [6.4, -13.8, 0.70]
  ];
  for (const [x, z, s] of outcropSpecs) {
    const rock = new THREE.Mesh(rockGeo, outcropMat);
    rock.name = 'shelf-outcrop';
    rock.position.set(x, 0.08 + s * 0.34, z);
    rock.rotation.set(rand() * 0.5, rand() * TAU, rand() * 0.35);
    rock.scale.set(s * 1.25, s * 0.90, s * 1.05);
    rock.castShadow = true;
    rock.receiveShadow = true;
    group.add(rock);
  }

  // Flat mineral / microbial crust patches along the wet shore. They are
  // decoration, not nutrient cells; the live positions remain in the reactor.
  const crustColors = [0x3c4c36, 0x51483a, 0x5d4a34, 0x314438];
  for (let i = 0; i < 13; i++) {
    const a = rand() * TAU;
    const r = 10.8 + rand() * 2.1;
    const mat = new THREE.MeshStandardMaterial({
      color: crustColors[Math.floor(rand() * crustColors.length)],
      roughness: 1.0,
      metalness: 0.0,
      transparent: true,
      opacity: 0.82,
      side: THREE.DoubleSide
    });
    const patch = new THREE.Mesh(new THREE.CircleGeometry(0.35 + rand() * 0.55, 9), mat);
    patch.name = 'shelf-crust';
    patch.rotation.x = -Math.PI / 2;
    patch.rotation.z = rand() * TAU;
    patch.scale.set(1.0 + rand() * 1.2, 0.5 + rand() * 0.8, 1.0);
    patch.position.set(Math.cos(a) * r, 0.072, Math.sin(a) * r);
    group.add(patch);
  }

  // ------------------------------------------------------------------ vent field
  const softTexture = (() => {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');
    const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
    grad.addColorStop(0.0, 'rgba(255,255,255,0.92)');
    grad.addColorStop(0.35, 'rgba(255,255,255,0.34)');
    grad.addColorStop(1.0, 'rgba(255,255,255,0.0)');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 64, 64);
    return new THREE.CanvasTexture(canvas);
  })();

  const plumes = [];
  function addPlume(x, z, baseY, height, count, size, opacity, color) {
    const positions = new Float32Array(count * 3);
    const data = [];
    for (let i = 0; i < count; i++) {
      data.push({
        phase: rand(),
        speed: 0.035 + rand() * 0.075,
        sway: rand() * TAU,
        spread: 0.3 + rand() * 0.7
      });
      const k = i * 3;
      positions[k] = x;
      positions[k + 1] = baseY;
      positions[k + 2] = z;
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    const points = new THREE.Points(geo, new THREE.PointsMaterial({
      map: softTexture,
      color,
      size,
      transparent: true,
      opacity,
      depthWrite: false,
      sizeAttenuation: true
    }));
    points.name = 'vent-plume';
    group.add(points);
    plumes.push({ geo, data, x, z, baseY, height });
  }

  const ventMat = new THREE.MeshStandardMaterial({
    color: 0x504d41,
    roughness: 0.98,
    metalness: 0.04,
    flatShading: true
  });
  const ventGlowMat = new THREE.MeshBasicMaterial({
    color: 0xff7433,
    transparent: true,
    opacity: 0.55,
    depthWrite: false,
    side: THREE.DoubleSide
  });
  const ventSites = [[-10.8, -12.2], [10.6, -12.4], [-14.6, -5.2]];
  for (let i = 0; i < ventSites.length; i++) {
    const x = ventSites[i][0];
    const z = ventSites[i][1];
    const r = Math.hypot(x, z);
    const a = Math.atan2(z, x);
    const base = Math.max(0.02, heightAt(r, a)) + 0.04;
    const h = 1.05 + rand() * 1.00;
    const chimney = new THREE.Mesh(new THREE.ConeGeometry(0.18 + rand() * 0.10, h, 7, 2), ventMat);
    chimney.name = 'vent-chimney';
    chimney.position.set(x, base + h * 0.5, z);
    chimney.castShadow = true;
    chimney.receiveShadow = true;
    group.add(chimney);

    const lip = new THREE.Mesh(new THREE.CylinderGeometry(0.30, 0.40, 0.12, 8), ventMat);
    lip.position.set(x, base + 0.04, z);
    lip.receiveShadow = true;
    group.add(lip);

    const glow = new THREE.Mesh(new THREE.CircleGeometry(0.25 + rand() * 0.09, 10), ventGlowMat);
    glow.rotation.x = -Math.PI / 2;
    glow.position.set(x, base + 0.012, z);
    group.add(glow);

    addPlume(x, z, base + h * 0.9, 5.2 + rand() * 1.8, 36, 0.82, 0.24, 0xc9d8d2);
  }
  const ventLight = new THREE.PointLight(0xff6f2e, 0.70, 7.0, 2.0);
  ventLight.position.set(-10.8, 0.80, -12.2);
  group.add(ventLight);

  // ------------------------------------------------------------- distant volcanoes
  const volcanoMat = new THREE.MeshStandardMaterial({
    color: 0x42433a,
    roughness: 1.0,
    metalness: 0.0,
    flatShading: true,
    emissive: 0x10120e,
    emissiveIntensity: 0.45
  });
  const lavaMat = new THREE.MeshBasicMaterial({
    color: 0xff5f28,
    transparent: true,
    opacity: 0.42,
    depthWrite: false,
    side: THREE.DoubleSide
  });
  function addVolcano(x, z, radius, height) {
    const a = Math.atan2(z, x);
    const r = Math.hypot(x, z);
    const base = heightAt(r, a) - 0.5;
    const peak = new THREE.Mesh(new THREE.ConeGeometry(radius, height, 9, 3), volcanoMat);
    peak.name = 'volcanic-peak';
    peak.position.set(x, base + height * 0.5, z);
    peak.rotation.y = rand() * TAU;
    peak.receiveShadow = true;
    group.add(peak);

    const crater = new THREE.Mesh(new THREE.CircleGeometry(radius * 0.22, 12), lavaMat);
    crater.name = 'volcanic-crater';
    crater.rotation.x = -Math.PI / 2;
    crater.position.set(x, base + height - 0.06, z);
    group.add(crater);

    const rim = new THREE.Mesh(
      new THREE.RingGeometry(radius * 0.21, radius * 0.30, 16),
      new THREE.MeshStandardMaterial({ color: 0x24241f, roughness: 1.0, side: THREE.DoubleSide })
    );
    rim.rotation.x = -Math.PI / 2;
    rim.position.set(x, base + height - 0.02, z);
    group.add(rim);

    addPlume(x, z, base + height * 0.92, height * 1.4, 80, 1.55, 0.11, 0xd6ddd7);
  }
  addVolcano(-31, -49, 12.5, 19.0);
  addVolcano(37, -61, 9.0, 14.0);

  // Midground ridges make the far shore a landform, not a flat rim.
  const ridgeMat = new THREE.MeshStandardMaterial({
    color: 0x555444,
    roughness: 1.0,
    metalness: 0.0,
    flatShading: true,
    emissive: 0x171a13,
    emissiveIntensity: 0.55
  });
  const ridgeSpecs = [
    [-28, -38, 14, 11],
    [-7, -50, 17, 18],
    [16, -43, 12, 13],
    [34, -58, 14, 17],
    [-46, -59, 15, 16],
    [0, -72, 22, 24]
  ];
  for (const [x, z, radius, height] of ridgeSpecs) {
    const a = Math.atan2(z, x);
    const r = Math.hypot(x, z);
    const base = heightAt(r, a) - 1.0;
    const peak = new THREE.Mesh(new THREE.ConeGeometry(radius, height, 7, 2), ridgeMat);
    peak.name = 'shelf-ridge';
    peak.position.set(x, base + height * 0.5, z);
    peak.rotation.y = rand() * TAU;
    peak.receiveShadow = true;
    group.add(peak);
  }

  // --------------------------------------------------------------------- clouds
  const cloudLayer = new THREE.Group();
  cloudLayer.name = 'cloud-layer';
  group.add(cloudLayer);
  const cloudGeo = new THREE.SphereGeometry(1, 8, 6);
  const cloudMat = new THREE.MeshBasicMaterial({
    color: 0xcfe0dc,
    transparent: true,
    opacity: 0.16,
    depthWrite: false,
    fog: false
  });
  function addCloudCluster(x, y, z, scale) {
    const cluster = new THREE.Group();
    cluster.position.set(x, y, z);
    const parts = 3 + Math.floor(rand() * 3);
    for (let j = 0; j < parts; j++) {
      const puff = new THREE.Mesh(cloudGeo, cloudMat);
      puff.scale.set(
        (5 + rand() * 7) * scale,
        (1.0 + rand() * 1.8) * scale,
        (2.5 + rand() * 3.0) * scale
      );
      puff.position.set((j - parts * 0.5) * 4.5 * scale, rand() * 1.8, (rand() - 0.5) * 5.0);
      cluster.add(puff);
    }
    cloudLayer.add(cluster);
  }
  for (let i = 0; i < 7; i++) {
    const a = rand() * TAU;
    const dist = 42 + rand() * 55;
    const y = 24 + rand() * 15;
    addCloudCluster(Math.cos(a) * dist, y, Math.sin(a) * dist, 1.0);
  }
  addCloudCluster(-18, 20, -38, 1.3);
  addCloudCluster(15, 22, -48, 1.7);
  addCloudCluster(0, 26, -70, 2.0);
  addCloudCluster(32, 18, -30, 1.1);
  addCloudCluster(0, 14, -30, 1.4);

  // A faint foam edge keeps the waterline readable at eye height.
  const foam = new THREE.Mesh(
    new THREE.RingGeometry(POND_RADIUS - 0.20, POND_RADIUS + 0.12, 160),
    new THREE.MeshBasicMaterial({
      color: 0x9acfc2,
      transparent: true,
      opacity: 0.08,
      side: THREE.DoubleSide,
      depthWrite: false
    })
  );
  foam.name = 'shelf-foam';
  foam.rotation.x = -Math.PI / 2;
  foam.position.y = 0.014;
  group.add(foam);

  // ------------------------------------------------------------------- animation
  const clock = new THREE.Clock();
  function updatePlumes(t) {
    for (const plume of plumes) {
      const pos = plume.geo.attributes.position;
      for (let i = 0; i < plume.data.length; i++) {
        const d = plume.data[i];
        const u = (d.phase + t * d.speed) % 1;
        const spread = 0.15 + u * d.spread;
        const k = i * 3;
        pos.setX(k, plume.x + Math.sin(t * 0.55 + d.sway) * 0.45 * spread);
        pos.setY(k + 1, plume.baseY + u * plume.height);
        pos.setZ(k, plume.z + Math.cos(t * 0.42 + d.sway) * 0.35 * spread);
      }
      pos.needsUpdate = true;
    }
  }

  function tick() {
    const t = clock.getElapsedTime();
    cloudLayer.rotation.y = t * 0.0015;
    foam.material.opacity = 0.12 + 0.04 * Math.sin(t * 0.8);
    updatePlumes(t);
    window.requestAnimationFrame(tick);
  }
  tick();

  window.__genesisEnvironment = {
    ready: true,
    terrainVertices: terrainPos.count,
    rocks: rockCount,
    vents: ventSites.length,
    clouds: cloudLayer.children.length,
    heightAt,
    pondRadius: POND_RADIUS,
    camera
  };
})();
