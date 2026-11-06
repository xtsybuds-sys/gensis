# GENESIS — THE PERFECT START PLAN (v3, the real 1000-point plan)

## What v3 is

v3 supersedes v2. It is 1000 topics, each going into in-depth detail: 10 phases × 10 milestones × 10 topics. Every topic states the rule (the mechanism, in detail), the numbers (starting values and ranges), and the check (how you know it works — the measurement, the number, or the falsifier). Nothing is claimed done without a measured result.

The world is a real world: an Earth-like planet under this universe's rules — the same physics and chemistry as real life, nothing invented, no new physics. Life starts from single cells and evolution does the rest; human-level minds are the destination, not the start. The Discovery Principle governs throughout: build rules, not things — inhabitants must be able to discover things even the owner did not place. Nothing is scripted into existence; emergence is measured honestly. Death is permanent; history stays. The world runs 24/7. One hybrid mind for every inhabitant (neural core + forward model + episodic memory; planner cut). The world must look as real as possible (photoreal bar: ray-traced lighting, textured materials, no low-poly). Decisions carried forward from v2: the species criterion (reproductive isolation OR genetic distance beyond a measured threshold); the four human-level tests (all must pass); the 15 m peer range and the house-gap rule; physiological sleep; the psychoactive plant rule; the Gateway contract (closed); the six-criterion protocell test as the origin-of-life bar, with the live protocell pond as the served baseline.

## Phase 1 — The real world: physics and chemistry

### 1.1 Gravity, mass, momentum

**1. Gravity pulls everything down**
- **Rule:** Every body with mass attracts every other body with mass, and near the planet's surface this shows as a steady downward pull. A dropped object accelerates downward, a thrown object follows a curved arc, and nothing floats unless some other force holds it up.
- **Numbers:** Surface gravity g = 9.81 m/s² downward; gravitational constant G = 6.67430×10⁻¹¹ m³·kg⁻¹·s⁻²; planet mass and radius set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A dropped test mass from 10 m hits the ground in 1.43 s (±0.05 s) with final speed 14.0 m/s; a deviation larger than 5% fails the check.

**2. Mass is conserved**
- **Rule:** Mass is never created or destroyed inside the world; it only moves, combines, or splits. Eating, burning, building, and dying all move mass between bodies and the environment, and the world's total mass stays the same.
- **Numbers:** Total world mass is a fixed starting value recorded at t = 0; numerical drift allowed ≤ 0.01% per simulated day; every transfer logs source, destination, and amount in kg.
- **Check:** Sum all mass in the world at any tick; if the total differs from the t = 0 total by more than 0.01% per day, the run fails.

**3. Momentum is conserved**
- **Rule:** Momentum (mass × velocity) is conserved in every interaction. When two bodies collide, what one gains the other loses, and the total momentum of a closed system stays constant unless an outside force acts.
- **Numbers:** Momentum in kg·m/s; elastic collisions conserve kinetic energy within 1%; inelastic collisions lose kinetic energy to heat and deformation, never to nothing.
- **Check:** In a two-body collision test with no outside force, total momentum before and after must match within 0.5%; a larger mismatch fails.

**4. Weight is gravity on mass**
- **Rule:** Weight is the force gravity exerts on a mass, so the same body weighs the same wherever it stands on the surface, and a heavier body needs more force to lift or move. Weight changes only if mass or local gravity changes.
- **Numbers:** Weight W = m × g; a 1 kg body weighs 9.81 N; a 70 kg body weighs 687 N; local g varies by less than 0.5% across the simulated region.
- **Check:** A 10 kg test mass on a scale reads 98.1 N (±1 N); a scale reading off by more than 2% fails.

**5. Falling bodies accelerate**
- **Rule:** In free fall, velocity grows linearly with time and distance grows with the square of time, because gravity adds the same speed every second. Air resistance eventually caps the speed, but in still air the early fall follows the square law.
- **Numbers:** v = g·t; distance = ½·g·t²; after 1 s a body falls 4.9 m at 9.81 m/s; after 2 s it has fallen 19.6 m at 19.6 m/s.
- **Check:** Drop a test mass from 20 m in still air; measured fall time must be 2.02 s (±0.1 s) and impact speed 19.8 m/s (±1 m/s).

**6. Projectiles follow arcs**
- **Rule:** A thrown object keeps its horizontal speed while gravity pulls it down, so its path is a parabola. The range depends on launch speed, launch angle, and air drag; the highest point is reached halfway through the flight.
- **Numbers:** Range R = v²·sin(2θ)/g in vacuum; maximum range at 45°; a 10 m/s throw at 45° travels 10.2 m in vacuum, less with drag.
- **Check:** Launch a test projectile at 10 m/s and 45°; measured range must be within 10% of the drag-corrected prediction, or the drag model fails.

**7. Inertia resists change**
- **Rule:** A body at rest stays at rest and a moving body keeps moving in a straight line unless a force acts on it. Changing a body's motion always costs force, and heavier bodies cost more force for the same change.
- **Numbers:** F = m·a; to accelerate a 1 kg body at 1 m/s² takes 1 N; to accelerate a 70 kg body at 1 m/s² takes 70 N; stopping a 1 kg body moving at 5 m/s in 0.1 s takes 50 N.
- **Check:** Apply a known 10 N force to a 2 kg test body for 1 s; its speed must change by 5 m/s (±0.25 m/s).

**8. Action and reaction are equal**
- **Rule:** Every force has an equal and opposite reaction. Pushing against the ground pushes the body forward; a body resting on a surface presses down exactly as hard as the surface pushes up.
- **Numbers:** Normal force on flat ground equals weight (9.81 N per kg); a jump that pushes down with 1,400 N gets 1,400 N back up; ground reaction is measured in newtons.
- **Check:** A 70 kg body standing still shows a ground reaction of 687 N (±7 N); a moving body shows the reaction matching its acceleration within 2%.

**9. Orbits and the planet's pull**
- **Rule:** The same gravity that drops a stone holds the planet's moon and keeps the planet in its orbit around its star. Orbital speed depends only on distance from the centre of mass and the mass being orbited, not on the orbiting body's own mass.
- **Numbers:** Orbital speed v = √(G·M/r); low orbit around an Earth-like planet is about 7.9 km/s; the planet's year and day length are set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A test body placed in a circular orbit at a given radius must complete one orbit in the predicted period within 1%, or the gravity model fails.

**10. Tides and the moon's pull**
- **Rule:** The moon's gravity pulls the near side of the planet's oceans more strongly than the far side, making two bulges of water that sweep around as the planet rotates, producing two high tides per day. The sun adds a smaller tide that strengthens or weakens the moon's.
- **Numbers:** Two high tides per lunar day (~24 h 50 min); spring tides at new and full moon, neap tides at quarter moons; tidal height range set by experiment — Freebuff proposes, Muse reviews.
- **Check:** Water level at a fixed shore point must show two high tides per lunar day with heights within 20% of the predicted range; a missing second tide fails.

### 1.2 Energy and heat

**11. Energy is conserved**
- **Rule:** Energy is never created or destroyed inside the world; it only changes form — motion becomes heat, chemical energy becomes motion, light becomes heat. Every transfer is accounted for, and the world's total energy stays the same.
- **Numbers:** Total energy tracked in joules; numerical drift allowed ≤ 0.01% per simulated day; every conversion logs the amount in and the amount out.
- **Check:** Sum kinetic, potential, thermal, and chemical energy at any tick; the total must match the t = 0 total within 0.01% per day, or the run fails.

**12. Kinetic energy is motion**
- **Rule:** A moving body carries kinetic energy that grows with the square of its speed, so doubling speed quadruples the energy. Stopping a body means that energy has to go somewhere — into heat, deformation, or another body's motion.
- **Numbers:** KE = ½·m·v²; a 70 kg body walking at 1.4 m/s carries 69 J; running at 5 m/s it carries 875 J; a 1 kg stone at 20 m/s carries 200 J.
- **Check:** A test body of known mass and speed must report kinetic energy within 1% of ½·m·v²; a larger error fails.

**13. Potential energy is stored height**
- **Rule:** Lifting a body against gravity stores energy in its position, and dropping it converts that stored energy back into motion. The amount stored depends only on mass, height, and gravity, not on the path taken to get there.
- **Numbers:** PE = m·g·h; a 1 kg body lifted 10 m stores 98.1 J; a 70 kg body lifted 1 m stores 687 J; falling that height returns the same energy.
- **Check:** Drop a 1 kg test mass from 10 m; its impact kinetic energy must be 98.1 J (±2 J), or the conversion is broken.

**14. Heat flows from hot to cold**
- **Rule:** Heat always flows from a hotter body to a colder one, never the reverse, until temperatures equalise. It moves by conduction through contact, by convection through moving fluid, and by radiation through empty space, all at once where all three apply.
- **Numbers:** Conduction follows Fourier's law (heat flux proportional to temperature gradient); convection and radiation rates set by experiment — Freebuff proposes, Muse reviews; heat measured in joules, temperature in kelvin or °C.
- **Check:** Two test blocks at 100 °C and 0 °C in contact must converge toward the same temperature with no net heat gain; a temperature difference that grows fails.

**15. Temperature is average motion**
- **Rule:** Temperature measures the average kinetic energy of the particles in a body: hotter means faster-moving particles. Absolute zero (0 K, −273.15 °C) is the point where particle motion stops, and no body in the world can go below it.
- **Numbers:** 0 K = −273.15 °C; water freezes at 273.15 K (0 °C) and boils at 373.15 K (100 °C) at 1 atm; human-scale body temperature is about 310 K (37 °C).
- **Check:** A thermometer in a test body must read within 0.5 K of the body's computed average particle energy, and never below 0 K.

**16. Friction turns motion into heat**
- **Rule:** When two surfaces slide against each other, friction converts kinetic energy into heat at the contact, warming both surfaces. The heat produced equals the work done against friction, so no energy is lost — it changes form.
- **Numbers:** Heat produced = friction force × sliding distance; sliding a 10 kg block 1 m against a surface with friction coefficient 0.5 produces 49 J of heat.
- **Check:** Slide a test block a known distance under a known friction force; the temperature rise of the block and surface must account for the work done within 10%, or the conversion fails.

**17. Work is force over distance**
- **Rule:** Doing work means applying a force through a distance: lifting, pushing, or pulling. The work done equals force times distance in the direction of the force, and it is stored as energy in the body or spent as heat.
- **Numbers:** Work W = F·d in joules; lifting 10 kg by 2 m does 196 J of work; pushing a 50 N load 10 m does 500 J of work.
- **Check:** A test body pushed 5 m by a measured 20 N force must gain or lose exactly 100 J of energy (±5 J), or the work accounting fails.

**18. Power is energy per second**
- **Rule:** Power is the rate at which energy is used or transferred. A body can do the same total work slowly or quickly, but doing it quickly needs more power, and sustained power is limited by the body's energy supply and by heat.
- **Numbers:** Power in watts (1 W = 1 J/s); a resting human-scale body uses about 100 W; walking uses about 200–300 W; running uses about 800–1,000 W.
- **Check:** A test body doing 500 J of work in 5 s must show 100 W average power (±5 W); a mismatch fails.

**19. Chemical energy is stored in bonds**
- **Rule:** Energy is stored in chemical bonds and released when bonds break and reform into lower-energy arrangements. Burning, eating, and metabolism all run on this: fuel plus oxygen becomes carbon dioxide plus water plus released heat and usable energy.
- **Numbers:** Burning 1 g of wood releases about 15–18 kJ; 1 g of fat releases about 37 kJ; 1 g of sugar releases about 17 kJ; exact values depend on composition, set by experiment — Freebuff proposes, Muse reviews.
- **Check:** Burning a measured mass of test fuel in a calorimeter must release heat within 10% of the tabulated value for that fuel, or the chemistry energy accounting fails.

**20. Entropy always increases**
- **Rule:** In any real process, some energy becomes unavailable for useful work — it spreads out as waste heat. Order can be built locally (a body, a house, a cell) only by spending energy and producing more disorder elsewhere, so the world's total disorder never decreases.
- **Numbers:** Entropy measured in J/K; a perfectly reversible process has zero entropy change, every real process has a positive one; waste heat per process is logged in joules.
- **Check:** In any closed test process, total entropy change must be ≥ 0; a measured decrease fails, and a process claiming 100% conversion efficiency fails.

### 1.3 Light and sound

**21. Light travels in straight lines**
- **Rule:** In a uniform medium, light travels in straight lines at a fixed speed, casting sharp shadows behind opaque objects. Rays bend only when the medium changes (refraction) or when light grazes an edge (diffraction), and the speed is the same for every observer.
- **Numbers:** Speed of light in vacuum c = 299,792,458 m/s; in water about 225,000,000 m/s; in air about 299,700,000 m/s; shadows are cast along the ray from the light source.
- **Check:** A light ray from a point source past a test obstacle must cast a shadow whose edges match straight-line geometry within 1°, or the light model fails.

**22. Light carries energy**
- **Rule:** Light is energy travelling as waves, and when it is absorbed it warms the surface that absorbs it. Bright light carries more energy per second than dim light, and shorter wavelengths carry more energy per photon than longer ones.
- **Numbers:** Solar irradiance at the surface is about 1,000 W/m² at noon on a clear day; photon energy E = h·f with Planck constant h = 6.626×10⁻³⁴ J·s; a black surface absorbs nearly all of it.
- **Check:** A black test plate of 1 m² under a known light source must warm at the rate predicted by the absorbed power within 10%, or the light-energy accounting fails.

**23. Reflection bounces light**
- **Rule:** When light hits a smooth surface it bounces off at the same angle it arrived, measured from the surface normal. Rough surfaces scatter light in many directions, which is why matte objects look the same from every angle and mirrors look different.
- **Numbers:** Angle of incidence equals angle of reflection; a mirror reflects about 90–95% of visible light; water reflects about 2% at straight-on angles and much more at grazing angles.
- **Check:** A ray striking a flat mirror at 30° must leave at 30° on the other side of the normal (±1°), or the reflection rule fails.

**24. Refraction bends light**
- **Rule:** Light bends when it passes from one transparent medium to another, because its speed changes. The bend follows Snell's law, which is why a stick looks broken at the water's surface and why lenses focus light.
- **Numbers:** Refractive index n: air 1.0003, water 1.33, glass about 1.5; Snell's law n₁·sin(θ₁) = n₂·sin(θ₂); a ray entering water at 45° bends to about 32°.
- **Check:** A ray entering a water test tank at 45° must bend to 32° (±2°); a larger error fails the refraction check.

**25. Colour is wavelength**
- **Rule:** Visible light spans wavelengths from about 380 nm (violet) to 750 nm (red), and an object's colour is the set of wavelengths it reflects while absorbing the rest. White light contains all visible wavelengths; a red object reflects red and absorbs the rest.
- **Numbers:** Violet 380–450 nm, blue 450–495 nm, green 495–570 nm, yellow 570–590 nm, orange 590–620 nm, red 620–750 nm; a surface's colour is its reflectance spectrum.
- **Check:** A test surface lit by white light must reflect the wavelengths its spectrum says it reflects, within 5% of the measured reflectance, or the colour model fails.

**26. Shadows and occlusion**
- **Rule:** An opaque object blocks light, leaving a shadow where its rays cannot reach. The shadow's size and sharpness depend on the light source's size and distance: a small distant source makes a sharp shadow, a large near source makes a soft one with a fuzzy edge.
- **Numbers:** Point source shadow edge is sharp (penumbra width 0); a source of angular diameter 0.5° (like the sun) gives a penumbra about 1 cm wide per metre of shadow distance.
- **Check:** A test obstacle 1 m from a surface under a sun-sized source must cast a shadow with a penumbra width within 20% of the predicted value, or the shadow model fails.

**27. Sound is vibration in a medium**
- **Rule:** Sound is a pressure wave travelling through air, water, or solid matter — it cannot travel through a vacuum. A vibrating source pushes the medium, the disturbance spreads, and a listener's ear or sensor detects the arriving pressure changes.
- **Numbers:** Speed of sound in air is 343 m/s at 20 °C; in water about 1,480 m/s; in rock about 5,000 m/s; speed in air rises about 0.6 m/s per °C.
- **Check:** A sound pulse fired across a 34.3 m air gap at 20 °C must arrive in 0.10 s (±0.01 s); a vacuum test must transmit nothing.

**28. Sound falls off with distance**
- **Rule:** Sound spreads out from its source, so its intensity drops with the square of the distance in open air, and it is further weakened by absorption in the air and by obstacles. Doubling the distance cuts the intensity to a quarter.
- **Numbers:** Intensity follows the inverse-square law; sound level in decibels drops about 6 dB per doubling of distance in open air; a shout at 1 m is about 80 dB, at 8 m about 62 dB.
- **Check:** A test source measured at 1 m and at 4 m must show a level drop of about 12 dB (±2 dB); a larger deviation fails.

**29. Echoes and reflection of sound**
- **Rule:** Sound reflects off hard surfaces like light reflects off mirrors, producing echoes that arrive later than the direct sound. The delay tells the distance to the reflecting surface, and soft or irregular surfaces absorb or scatter the sound instead.
- **Numbers:** Echo delay is 2 × distance / speed of sound; a wall 17 m away gives a 0.1 s echo in air; hard rock reflects most sound, soft soil absorbs much of it.
- **Check:** A sound pulse fired at a wall 34.3 m away must return in 0.20 s (±0.02 s); a missing or mistimed echo fails.

**30. Pitch and frequency**
- **Rule:** The pitch of a sound is its frequency — how many pressure cycles arrive per second. Higher frequency means higher pitch, and different materials and sizes of sound source produce different frequencies when struck or blown.
- **Numbers:** Human hearing spans about 20 Hz to 20,000 Hz; a 440 Hz tone is the musical note A; frequency f = speed / wavelength; a 343 Hz tone in air has a 1 m wavelength.
- **Check:** A test tone of 440 Hz must be measured at 440 Hz (±5 Hz) at the receiver, and its wavelength in air must be 0.78 m (±0.05 m).

### 1.4 Fluids

**31. Fluids flow and fill**
- **Rule:** Liquids and gases flow to fill their container, taking its shape while keeping their volume (liquids) or expanding to fill it (gases). A liquid's surface stays level under gravity, and fluid moves from high pressure to low pressure.
- **Numbers:** Water density 1,000 kg/m³ at 4 °C; air density 1.225 kg/m³ at sea level, 15 °C; a liquid surface is horizontal within 0.1° in still conditions.
- **Check:** Pour 1 litre of water into a test container; the measured volume must be 1 litre (±1%) and the surface level within 0.1°, or the fluid model fails.

**32. Pressure grows with depth**
- **Rule:** In a still liquid, pressure increases with depth because the weight of the liquid above presses down. The increase depends only on depth, liquid density, and gravity — not on the shape of the container.
- **Numbers:** Pressure P = ρ·g·h; in water the pressure rises about 9.81 kPa per metre of depth; at 10 m depth the pressure is about 1 atm above the surface.
- **Check:** A pressure sensor at 5 m depth in water must read about 49 kPa above the surface pressure (±2 kPa); a larger error fails.

**33. Buoyancy lifts what it displaces**
- **Rule:** A body in a fluid is pushed up by a force equal to the weight of the fluid it displaces. If the body is less dense than the fluid it floats; if denser, it sinks; if equal, it hangs suspended.
- **Numbers:** Buoyant force F = ρ_fluid·V·g; a 1 m³ body in water feels 9,810 N of lift; wood (density ~600 kg/m³) floats with about 60% submerged.
- **Check:** A test block of known volume and density placed in water must float at the predicted submerged fraction within 5%, or the buoyancy rule fails.

**34. Viscosity resists flow**
- **Rule:** Viscosity is a fluid's internal friction — how hard it is to stir or pour. Honey flows slowly because it is viscous; water flows easily because it is not. Viscosity falls as temperature rises, and it sets how fast objects sink or move through the fluid.
- **Numbers:** Water viscosity 0.001 Pa·s at 20 °C; honey about 10 Pa·s; air about 1.8×10⁻⁵ Pa·s; a sphere sinking in a viscous fluid reaches a terminal speed set by Stokes' law.
- **Check:** A test sphere dropped in water must reach the terminal speed predicted by Stokes' law within 10%, or the viscosity model fails.

**35. Surface tension holds the skin**
- **Rule:** At a liquid's surface, molecules pull sideways on each other more strongly than they pull outward, forming a skin that can support small weights and lets droplets hold their shape. It is strongest in pure water and weaker when soap or other substances are present.
- **Numbers:** Water surface tension 0.072 N/m at 20 °C; it can support a small insect or a carefully placed needle; droplets form spheres to minimise surface area.
- **Check:** A test droplet on a flat surface must show the contact angle predicted by the surface tension value within 5°, and a needle test must support the predicted weight within 10%.

**36. Flow can be smooth or turbulent**
- **Rule:** Slow flow in a smooth channel is laminar — layers slide past each other without mixing. Faster flow, or flow past obstacles, becomes turbulent, with eddies and mixing. The switch depends on speed, size, density, and viscosity, captured by the Reynolds number.
- **Numbers:** Reynolds number Re = ρ·v·L/μ; flow in a pipe turns turbulent above Re ≈ 4,000; a river 1 m deep flowing at 1 m/s has Re ≈ 1,000,000 and is turbulent.
- **Check:** A test channel run at Re below 2,000 must show laminar flow (no eddies) and above 4,000 must show turbulence; a wrong regime fails.

**37. Waves carry energy across water**
- **Rule:** Wind blowing over water, or a disturbance in the water, makes waves that carry energy across the surface while the water itself mostly moves in small circles. Wave speed depends on wavelength and depth: long waves in deep water travel faster than short ones.
- **Numbers:** Deep-water wave speed v = √(g·λ/2π); a 10 m wavelength wave travels about 3.95 m/s; wave height and period set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A test wave of 10 m wavelength in deep water must travel at 3.95 m/s (±0.2 m/s); a larger error fails the wave model.

**38. Currents move water**
- **Rule:** Water moves in currents driven by wind, by temperature and salt differences, and by tides. A current carries heat, nutrients, and anything floating in it, and it can be steady or change with the seasons and the weather.
- **Numbers:** Surface currents run about 0.1–1 m/s; a river flows about 0.5–2 m/s; current speed and direction are measured in m/s and degrees, logged per region.
- **Check:** A floating test marker released in a known current must drift at the current's speed within 10% over 100 m, or the current model fails.

**39. Evaporation and condensation**
- **Rule:** At a liquid's surface, the fastest molecules escape into the air as vapour (evaporation), and vapour molecules can return to the liquid (condensation). Warm air holds more vapour than cold air, so evaporation is faster on warm, dry, windy days.
- **Numbers:** Water evaporates at about 0.1–0.5 mm per hour from an open surface on a warm day; saturated air at 20 °C holds about 17 g of water vapour per m³; boiling happens when vapour pressure equals air pressure.
- **Check:** An open test pan of water under known temperature, humidity, and wind must lose mass at the predicted evaporation rate within 15%, or the model fails.

**40. Freezing and melting**
- **Rule:** When water cools to 0 °C it freezes into ice, which is less dense than liquid water, so ice floats. Melting reverses the process, and both changes absorb or release a fixed amount of heat per kilogram without changing temperature during the change.
- **Numbers:** Water freezes and melts at 0 °C at 1 atm; latent heat of fusion 334 kJ/kg; ice density 917 kg/m³ against water's 1,000 kg/m³, so about 9% of an iceberg sits above the surface.
- **Check:** Freezing 1 kg of water at 0 °C must release 334 kJ (±10 kJ) with no temperature change, and the resulting ice must float with 91% submerged (±2%).

### 1.5 Materials

**41. Density is mass per volume**
- **Rule:** Density tells how much mass is packed into a given volume, and it decides whether a thing floats or sinks, how heavy it feels, and how much force it takes to move. Different materials have different densities because their atoms pack differently.
- **Numbers:** Water 1,000 kg/m³; wood 400–800 kg/m³; stone 2,500–3,000 kg/m³; iron 7,870 kg/m³; gold 19,300 kg/m³; air 1.225 kg/m³.
- **Check:** A test block of known mass and volume must report the density mass/volume within 1%; a larger error fails the material model.

**42. Hardness resists scratching**
- **Rule:** Hardness is a material's resistance to being scratched or dented by another material. A harder material scratches a softer one, never the reverse, and hardness is measured on a scale that ranks materials against each other.
- **Numbers:** Mohs scale 1–10: talc 1, fingernail 2.5, copper 3, iron 5, quartz 7, diamond 10; a material scratches every material below it on the scale.
- **Check:** A test sample of quartz (Mohs 7) must scratch copper (Mohs 3) and be scratched by diamond (Mohs 10); a reversed result fails.

**43. Strength resists breaking**
- **Rule:** Strength is how much force a material can take before it bends, cracks, or breaks. Tensile strength resists pulling apart, compressive strength resists being crushed, and shear strength resists being cut sideways; every material has different values for each.
- **Numbers:** Wood tensile strength about 40–100 MPa along the grain; stone compressive strength about 50–200 MPa; iron tensile strength about 200–400 MPa; steel about 400–1,000 MPa.
- **Check:** A test beam of known cross-section loaded to its tabulated breaking force must fail within 10% of that force, or the strength model fails.

**44. Elasticity and spring-back**
- **Rule:** An elastic material stretches or compresses under load and returns to its original shape when the load is removed, as long as the load stays below its elastic limit. Past that limit the change becomes permanent, and past the breaking point it fails.
- **Numbers:** Hooke's law F = k·x; Young's modulus: steel 200 GPa, wood 10 GPa, rubber 0.01–0.1 GPa; elastic limit is the load where permanent deformation begins.
- **Check:** A test spring stretched by a known force must extend by the amount Hooke's law predicts within 5% and return fully when released; a permanent set below the elastic limit fails.

**45. Brittleness and toughness**
- **Rule:** A brittle material breaks suddenly with little bending, while a tough material absorbs energy by bending before it breaks. Glass is hard and brittle; leather is soft and tough; steel is both hard and tough, which is why it is used for tools.
- **Numbers:** Fracture energy: glass about 10 J/m², steel about 100,000 J/m²; a brittle test sample breaks with less than 1% strain, a tough one with more than 5%.
- **Check:** A test sample struck with a known impact energy must break or survive exactly as its tabulated fracture energy predicts, within 20%, or the model fails.

**46. Thermal conduction through solids**
- **Rule:** Heat moves through solids by conduction, and different materials conduct at very different rates: metals conduct fast, wood and stone conduct slowly, and air trapped in a material conducts slowest of all. Good conductors feel cold to the touch because they carry heat away from skin quickly.
- **Numbers:** Thermal conductivity: copper 400 W/(m·K), iron 80, stone 2–3, wood 0.1–0.2, still air 0.026; a 1 cm iron plate passes far more heat than a 1 cm wood plate under the same temperature difference.
- **Check:** Two test plates (iron and wood) of the same size under the same temperature difference must pass heat at rates within 10% of their tabulated conductivities, or the conduction model fails.

**47. Materials expand when heated**
- **Rule:** Most materials expand when heated and contract when cooled, because hotter particles vibrate more widely and need more room. The change is small per degree but adds up over long lengths and large temperature swings, and it can crack rigid structures if it has nowhere to go.
- **Numbers:** Linear expansion coefficient: steel 12×10⁻⁶ per °C, wood about 5×10⁻⁶, stone about 8×10⁻⁶; a 10 m steel bar heated by 50 °C grows by 6 mm.
- **Check:** A 1 m test bar heated by 50 °C must grow by the tabulated amount within 10%; a bar that does not grow, or grows the wrong way, fails.

**48. Porous materials soak up water**
- **Rule:** Porous materials (wood, cloth, unglazed clay, some stone) contain tiny holes that soak up water by capillary action, getting heavier and weaker when wet. Non-porous materials (glass, metal, glazed clay) do not absorb water at all.
- **Numbers:** Dry wood absorbs 10–30% of its weight in water; unglazed clay absorbs 10–20%; glass and metal absorb 0%; soaked wood loses about half its strength.
- **Check:** A dry test block of wood soaked for 24 hours must gain 10–30% of its weight in water, and a glass block must gain 0% (±0.1%); a wrong result fails.

**49. Materials wear and weather**
- **Rule:** Materials degrade over time: wood rots when wet, iron rusts when exposed to water and air, stone crumbles under frost and rain, and cloth frays with use. The rate depends on the material, the exposure, and the climate, and nothing lasts forever without maintenance.
- **Numbers:** Iron rusts at about 0.1 mm per year in damp air; untreated wood outdoors lasts about 5–20 years; stone weathers at about 0.01–0.1 mm per year; rates set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A test sample exposed to damp air for a measured period must lose material at the tabulated rate within 30%, or the weathering model fails.

**50. Mixtures and composites**
- **Rule:** Mixing materials can make something better than either alone: fibres in a matrix, clay with straw, or two metals melted together. The mixture's properties come from the combination and the proportions, not from either part alone, and the mixture is a new material with its own numbers.
- **Numbers:** Clay with 10% straw is stronger in tension than plain clay by about 50%; bronze (copper + tin) is harder than copper alone; mixture ratios are set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A test mixture made to a stated ratio must measure the strength and density predicted for that ratio within 15%, or the mixture model fails.

### 1.6 Collisions and friction

**51. Elastic collisions bounce**
- **Rule:** In an elastic collision, two bodies bounce off each other and both momentum and kinetic energy are conserved, so nothing is lost to heat or deformation. Real collisions are never perfectly elastic, but hard, fast impacts come close.
- **Numbers:** Two equal masses colliding head-on swap velocities; a light body hitting a heavy stationary body rebounds at nearly its incoming speed; energy loss in a near-elastic test must be under 1%.
- **Check:** Two test spheres of equal mass colliding head-on must swap speeds within 2% and lose less than 1% of kinetic energy, or the collision model fails.

**52. Inelastic collisions stick or deform**
- **Rule:** In an inelastic collision, bodies deform, stick together, or both, and kinetic energy is lost to heat and permanent deformation while momentum is still conserved. A lump of clay hitting a wall is fully inelastic; a car crash is mostly inelastic.
- **Numbers:** A fully inelastic collision of two equal masses ends with both moving at half the incoming speed; kinetic energy loss is 50% in that case; the lost energy appears as heat.
- **Check:** Two test lumps of clay colliding head-on must stick and move at half the incoming speed (±5%), with the lost kinetic energy appearing as heat within 20%.

**53. Restitution measures bounciness**
- **Rule:** The coefficient of restitution is the ratio of the speed after a bounce to the speed before it. A value of 1 is a perfect bounce, 0 is no bounce at all, and every real material sits somewhere in between.
- **Numbers:** Steel on steel about 0.9; wood on wood about 0.5; clay on a wall about 0; a ball dropped from 1 m with restitution 0.8 rebounds to 0.64 m.
- **Check:** A test ball dropped from 1 m onto a test surface must rebound to the height predicted by its restitution coefficient within 5%, or the bounce model fails.

**54. Static friction holds things still**
- **Rule:** Static friction is the force that stops a resting body from sliding, and it can match any applied push up to a maximum set by the surfaces and the weight pressing them together. Once the push exceeds that maximum, the body starts to slide.
- **Numbers:** Maximum static friction F = μ_s·N; wood on wood μ_s ≈ 0.5; rubber on stone μ_s ≈ 0.8; ice on ice μ_s ≈ 0.03; N is the normal force (weight on flat ground).
- **Check:** A 10 kg test block on wood must start sliding when the push reaches 49 N (±5 N); a block that slides at half that force, or never slides, fails.

**55. Kinetic friction slows sliding**
- **Rule:** Once a body is sliding, kinetic friction opposes the motion with a roughly constant force that is usually slightly less than the maximum static friction. It turns kinetic energy into heat at the contact, and it does not depend on the contact area or the sliding speed (to first order).
- **Numbers:** Kinetic friction F = μ_k·N; wood on wood μ_k ≈ 0.3; a 10 kg block sliding on wood feels about 29 N of friction and stops from 1 m/s in about 0.17 m.
- **Check:** A test block sliding on wood from a known speed must stop within 10% of the predicted distance, or the kinetic friction model fails.

**56. Rolling friction is small**
- **Rule:** A round body rolling on a surface loses far less energy to friction than a sliding body, because the contact point is briefly at rest and the resistance comes from deformation of the surfaces, not from sliding. This is why wheels and round stones move easily.
- **Numbers:** Rolling resistance coefficient for a wheel on hard ground is about 0.01–0.02, against 0.3 for sliding; a 100 kg cart needs about 10–20 N to keep rolling, against 300 N to keep sliding.
- **Check:** A test wheel of known load rolling on hard ground must need a push within 20% of the predicted rolling resistance, or the rolling model fails.

**57. Friction needs a normal force**
- **Rule:** Friction is proportional to the force pressing the surfaces together, not to the weight of the body alone. On a slope the normal force is less than the weight, so friction is weaker; pressing down harder makes friction stronger.
- **Numbers:** Normal force on a slope N = m·g·cos(θ); on a 30° slope the normal force is 87% of the weight; on a vertical wall it is zero unless something presses the body against it.
- **Check:** A test block on a 30° slope must show a maximum static friction of 87% of its flat-ground value (±5%); a slope-independent result fails.

**58. Impacts transfer impulse**
- **Rule:** An impact is a large force acting for a short time, and the change in momentum (impulse) equals force times time. A soft surface stretches the impact over a longer time and so lowers the peak force, while a hard surface stops the body fast and hits harder.
- **Numbers:** Impulse J = F·Δt = Δ(m·v); a 1 kg body stopping from 5 m/s in 0.01 s feels 500 N; stopping in 0.1 s it feels 50 N; the momentum change is 5 kg·m/s either way.
- **Check:** A test body stopped by a soft pad and by a hard plate must show the same total impulse (±5%) but a peak force at least 5× lower on the pad, or the impact model fails.

**59. Collisions conserve angular momentum**
- **Rule:** A spinning body keeps spinning unless a torque acts on it, and when bodies collide off-centre, the total angular momentum (spin) is conserved just like linear momentum. An off-centre hit makes a body spin as well as move.
- **Numbers:** Angular momentum L = I·ω; a body hit off-centre gains spin proportional to the offset; a spinning body struck head-on keeps its spin unless friction at the contact slows it.
- **Check:** A test sphere struck off-centre by a known impulse must gain the spin predicted by the offset within 10%, or the angular model fails.

**60. Contact forces resolve every tick**
- **Rule:** When two bodies touch, the simulation must resolve the contact every tick: push them apart so they do not overlap, apply the friction and restitution forces, and conserve momentum. Contacts that are missed or resolved late let bodies sink through each other or gain energy from nothing.
- **Numbers:** Contact resolution runs every simulation tick; allowed overlap after resolution is less than 1 mm; energy gain from contact resolution must be zero within 0.1% per tick.
- **Check:** A test stack of 10 blocks left for 1,000 ticks must stay standing with no block sinking more than 1 mm and no block gaining energy; a sinking or jittering stack fails.

### 1.7 Time and scale

**61. Time advances in fixed steps**
- **Rule:** The world advances in small, fixed time steps (ticks), and every physical process — motion, heat flow, chemistry, growth — is updated once per tick in the same order. A fixed step keeps the simulation deterministic: the same starting state and the same steps always give the same result.
- **Numbers:** Tick length is a starting value set by experiment — Freebuff proposes, Muse reviews; a human-scale tick of 0.1 s and a cell-scale tick of 1 s are starting points; tick count is recorded in every log.
- **Check:** The same seed run twice must produce identical state at every logged tick (bit-identical or within documented floating-point tolerance); any difference fails.

**62. The world has a day and a night**
- **Rule:** The planet rotates, so any point on its surface passes through daylight and darkness once per rotation. Light, temperature, and the behaviour of anything that depends on light all follow this cycle, and the cycle is driven by the planet's rotation, not by a scripted clock.
- **Numbers:** Day length is set by experiment — Freebuff proposes, Muse reviews; an Earth-like starting point is a 24 h day with roughly equal day and night at the equator; the run clock starts at dawn.
- **Check:** A light sensor at a fixed point must record a light curve with one rise and one fall per rotation, matching the predicted sunrise and sunset times within 5 minutes.

**63. Seasons come from tilt and orbit**
- **Rule:** The planet's axis is tilted relative to its orbit, so as it travels around its star the same place gets more or less direct sunlight through the year. This produces seasons: warmer when the sun is higher and the days are longer, colder when it is lower and the days are shorter.
- **Numbers:** Axial tilt is a starting value set by experiment — Freebuff proposes, Muse reviews; Earth-like starting point is 23.4°; year length and season timing follow from the orbit.
- **Check:** A temperature sensor at a fixed latitude must show a yearly cycle with one warm peak and one cold trough, matching the tilt-predicted amplitude within 20%.

**64. The world has one clock**
- **Rule:** Every part of the world — physics, chemistry, bodies, minds — reads the same simulation clock, so cause always comes before effect and nothing can act on a future state. The clock is the single source of time for the whole world.
- **Numbers:** Simulation time is measured in seconds from t = 0; wall-clock time is logged separately and never drives the world; the clock advances by exactly one tick per step, never by a variable amount.
- **Check:** Two events logged in different systems must have timestamps that order correctly (the cause's tick is never after the effect's tick); a single out-of-order pair fails.

**65. Small scales run faster**
- **Rule:** Small, fast processes (a cell's chemistry, a collision) happen on shorter timescales than large, slow ones (a body's growth, a season). The simulation must resolve the fastest process it claims to model, or that process will be wrong — a tick too long smears fast events into mush.
- **Numbers:** Collision resolution needs a tick shorter than the contact time (about 0.001–0.01 s for hard impacts); cell chemistry can run on ticks of 1 s or longer; the tick is chosen per scale, set by experiment — Freebuff proposes, Muse reviews.
- **Check:** A test collision run at the chosen tick must match the analytic result within 5%; doubling the tick must not change the result by more than 5%, or the tick is too long.

**66. Large scales run slower**
- **Rule:** Large structures change slowly: a mountain does not move in a day, a forest does not grow in an hour. The simulation can update slow processes less often than fast ones, but it must never let a slow process skip a change that a fast process caused.
- **Numbers:** Terrain changes are updated on timescales of days to years; weather on hours; a body's growth on hours to days; the update schedule is recorded per system.
- **Check:** A test event that changes a slow system (for example, a fire scorching ground) must appear in that system's state within its stated update interval, or the scheduling fails.

**67. Scale is consistent**
- **Rule:** The world uses one set of units — metres, kilograms, seconds — at every scale, from a cell to a planet. A length measured at cell scale and the same length measured at human scale must agree, and a force computed at one scale must be the same force at another.
- **Numbers:** All lengths in metres, masses in kilograms, times in seconds; a cell of 10 µm is 0.00001 m; a human-scale world of 128 m is 12,800,000 cell widths; unit conversions are tested, never assumed.
- **Check:** A test object measured at two scales must give the same length within 0.1%; a unit-conversion error of any size fails.

**68. The world is bounded, with an edge rule**
- **Rule:** The simulated region has a boundary, and the rule for what happens at the edge is fixed and recorded: bodies cannot leave, and nothing enters unrecorded. The edge is impassable natural terrain (water, cliffs, dense growth), not an invisible wall, and generation beyond it comes with scale-out.
- **Numbers:** Experiment 1 is one bounded 128 m locale; the edge rule is enforced every tick; any body reaching the edge is stopped or turned by the terrain, never deleted silently.
- **Check:** A test body driven at the edge for 1,000 ticks must never leave the region and must never vanish; a body found outside the boundary fails.

**69. History is kept**
- **Rule:** The world keeps a record of what happened — births, deaths, discoveries, changes to the land — and that record is never rewritten. A dead body stays dead in the record, an extinct lineage stays extinct, and the past can be read back but not changed.
- **Numbers:** Every event is logged with tick, time, and cause; the log is append-only; checkpoint files store the full state so a run can be resumed and re-read.
- **Check:** A run resumed from a checkpoint must continue exactly as the uninterrupted run did (bit-identical state at the next logged tick); a mismatch fails.

**70. The simulation runs continuously**
- **Rule:** The world runs 24/7 with no end date: it does not stop after a fixed number of days, and it does not need an observer to keep running. Tests and pilots are bounded, but the world itself has no time limit — inhabitants get unlimited time to evolve.
- **Numbers:** No total runtime cap on the world; test runs use explicit caps (for example, 45 min or 300 min) that apply only to the test, never to the world; uptime and tick count are logged continuously.
- **Check:** A world instance left running with no observer connected must keep advancing its tick count and logging events; a stalled tick count with no error recorded fails.

### 1.8 The fixed laws

**71. The laws do not change**
- **Rule:** The physical laws are fixed for the whole life of the world: gravity, conservation of mass and energy, the speed of light, and the rest never change value, never get patched mid-run, and never bend for a special case. Discovery is new understanding of fixed laws, never a new law.
- **Numbers:** Constants are recorded once at t = 0 (g = 9.81 m/s², c = 299,792,458 m/s, and the rest) and stored read-only; any change requires a new world, not an edit to a running one.
- **Check:** A test that reads the constants at t = 0 and at a later tick must find identical values; any difference fails, and a run whose constants changed is discarded.

**72. No free energy, no free mass**
- **Rule:** Nothing in the world creates energy or mass from nothing. Every gain in one place is a loss somewhere else, and any process that appears to create energy or mass is a bug, not a discovery. The conservation checks catch it.
- **Numbers:** Mass and energy drift limits are 0.01% per simulated day (see topics 2 and 11); a process that gains more than it takes in is flagged the moment it is measured.
- **Check:** A closed test system run for 1,000 ticks must show total mass and total energy constant within the drift limits; a gain beyond the limits fails.

**73. No omniscience**
- **Rule:** Nothing in the world can know the world's state directly. Every inhabitant learns only through its own senses, and every sensor reads only the local environment — no peeking at the simulation's internal state, no global view, no knowledge of things it has not sensed.
- **Numbers:** A sensor's range is a recorded value per sense (for example, peer range 15 m); any reading that depends on a state outside that range is a bug; sensor cost per tick is logged.
- **Check:** A test inhabitant placed with food hidden behind an obstacle must behave identically to one with no food present until the food enters its sensor range; a difference before that moment fails.

**74. Cause comes before effect**
- **Rule:** Every effect has a cause that happened earlier in simulation time, and no effect can reach back and change its own cause. The tick order enforces this: senses read the state at the start of the tick, actions apply during the tick, and the results are visible only from the next tick onward.
- **Numbers:** State at tick N is a function of state at tick N − 1 and the actions taken in tick N − 1 only; no system reads a value from tick N + 1.
- **Check:** A test that inspects the update order must find no system reading a value written later in the same tick; a single forward read fails.

**75. The laws are the same everywhere**
- **Rule:** The same physics applies in every part of the world — at the shore, in the forest, underground, and at every scale. There are no local exceptions, no special zones where gravity is different, and no place where conservation stops applying.
- **Numbers:** Constants are global, not per-region; a test run in two different regions must give the same result for the same setup within measurement error.
- **Check:** The same drop test run in two different regions must give fall times within 1% of each other; a region-dependent result fails.

**76. Randomness comes from a seed**
- **Rule:** All randomness in the world comes from a recorded random-number generator with a recorded seed. The same seed always gives the same sequence, so any run can be replayed exactly, and any surprise can be traced back to the seed that produced it.
- **Numbers:** Seed is a recorded integer (for example, 20261105); the generator type and its state are stored in every checkpoint; the same seed run twice must be identical.
- **Check:** Two runs from the same seed must produce identical logged state at every checkpoint; any difference fails the determinism check.

**77. Determinism is checkable**
- **Rule:** Because the laws are fixed and the randomness is seeded, the world is deterministic: the same starting state and the same seed always produce the same history. This is what makes every claim testable — a result can be re-run and re-checked by anyone.
- **Numbers:** Determinism is verified by re-running a recorded seed and comparing the full state digest at each checkpoint; the digest must match exactly.
- **Check:** Re-run a 1,000-tick test from its seed; the state digest at tick 1,000 must match the original exactly; a mismatch fails.

**78. The world does not know it is watched**
- **Rule:** Observation never changes the world. A viewer, a log reader, or a measurement tool reads state and nothing else — it does not add energy, move bodies, or feed information back into any inhabitant. The world cannot sense a watcher.
- **Numbers:** The Gateway feed is read-only with no write path; a viewer connected or disconnected must not change the tick rate, the state digest, or any inhabitant's behaviour.
- **Check:** Two identical runs, one with a viewer attached and one without, must produce identical state digests; any difference fails.

**79. Nothing is placed after t = 0**
- **Rule:** After the starting conditions are set, nothing is added to the world by hand — no new food, no new bodies, no new land, no new species. Everything that appears later comes from the rules: birth, growth, chemistry, or generation from the same rules as the world expands.
- **Numbers:** Every object in the world has a logged origin (starting condition, birth, chemical reaction, or procedural generation); an object with no logged origin is a placement and fails the check.
- **Check:** An audit of the world state at any tick must find every object traceable to a logged origin; a single untraceable object fails.

**80. The laws are the ceiling on discovery**
- **Rule:** Inhabitants can only discover what is inside the rules, so the depth of the simulation sets the ceiling on what can be discovered. A shallow simulation can only hold shallow discoveries; deeper laws, when added, open deeper discoveries — but the laws themselves never change mid-discovery.
- **Numbers:** The discovery ceiling is recorded per system (for example, the current kernel holds only shallow discoveries); a claimed discovery is tested by asking whether the owner could have predicted it — if yes, it was placed; if no, it was discovered.
- **Check:** For any claimed discovery, the pre-run prediction list must not contain it; a discovery that appears on the prediction list is reclassified as placed, not discovered.

### 1.9 Measuring the world

**81. Every quantity has a unit**
- **Rule:** Every number the world reports carries a unit — metres, kilograms, seconds, joules, kelvin — and no number is ever logged bare. A measurement without a unit cannot be checked, compared, or trusted, so the logging format rejects unitless values.
- **Numbers:** Units follow the SI system; the log format records value, unit, tick, and source for every measurement; a bare number in a log is a format error.
- **Check:** A scan of any run log must find a unit attached to every numeric measurement; a single unitless number fails the format check.

**82. Sensors measure, they do not guess**
- **Rule:** A sensor reports what it actually detects, with noise and limits, and it never reports a value it did not measure. A chemical sensor reports a concentration it sampled; a light sensor reports the light that reached it; neither reports the true world value directly.
- **Numbers:** Sensor noise is a recorded value per sensor type (for example, ±5% on a chemical reading); sensor range is recorded; readings outside the range are reported as out-of-range, never as a guessed value.
- **Check:** A test sensor placed in a known concentration must report within its stated noise band; a reading outside the band, or a guessed value beyond its range, fails.

**83. Instruments are calibrated**
- **Rule:** Every measuring instrument is calibrated against a known standard before it is trusted, and the calibration is recorded with its date and its error. An uncalibrated instrument's readings are treated as unknown, not as data.
- **Numbers:** Calibration error is recorded per instrument (for example, ±0.5 K for a thermometer, ±1% for a scale); recalibration is scheduled whenever the error drifts beyond its limit.
- **Check:** A calibrated test instrument measuring a known standard must read within its stated error; a reading outside the error band fails and the instrument is recalibrated.

**84. Measurements are logged with time**
- **Rule:** Every measurement is logged with the simulation tick and time at which it was taken, so a result can be placed in the world's history and compared with other measurements from the same moment. A measurement without a timestamp cannot be ordered against anything else.
- **Numbers:** Log entries carry tick (integer), simulation time in seconds, and the measured value with its unit; logs are append-only and stored with the run's seed.
- **Check:** A scan of any run log must find a tick and a time on every entry; an entry missing either fails the format check.

**85. Error is reported with every result**
- **Rule:** No result is reported without its error — the range within which the true value is expected to lie. A number without an error bar is a guess, and a claim built on a number without an error bar is not a claim.
- **Numbers:** Error is reported as a range (for example, 9.81 ± 0.05 m/s²) or as a percentage (±1%); the method used to estimate the error is recorded with the result.
- **Check:** Any reported result in a run record must carry an error estimate; a result without one is rejected and must be re-measured.

**86. Controls separate signal from noise**
- **Rule:** Every experiment runs with a control — a run identical in every way except for the one thing being tested — so a result can be blamed on the tested change and not on chance, the weather, or a bug. A result without a control is a story, not a measurement.
- **Numbers:** Controls use the same seed and the same starting conditions; the protocell criterion uses a neutral control and a no-catalysis control; a control that behaves differently from its expectation invalidates the run.
- **Check:** A test experiment must show its control behaving as expected (for example, the no-catalysis control shows zero catalysed births); a control that fails invalidates the experiment.

**87. Repeats beat single runs**
- **Rule:** A single run can be a fluke, so important results are measured across several seeds. The spread across seeds is part of the result: a result that holds on five seeds is worth more than one that holds on one.
- **Numbers:** Key results use at least 5 seeds; the result is reported as the median across seeds with the range; a result that appears on fewer than 3 of 5 seeds is reported as weak, not as a pass.
- **Check:** A claimed pass must show the numbers for every seed, not just the best one; a claim reported from a single seed is marked unconfirmed.

**88. The world can be re-run**
- **Rule:** Any run can be replayed from its seed and its starting conditions to produce the same history, so any claim can be checked by re-running it. The seed, the starting conditions, and the code version are all recorded with every run.
- **Numbers:** Run records carry seed, starting conditions, code version, and tick count; a re-run from the same record must reproduce the same state digest.
- **Check:** Re-run a recorded run from its record; the state digest at the final tick must match the original exactly; a mismatch fails.

**89. Checkpoints save the whole state**
- **Rule:** A checkpoint stores the complete state of the world — every body, every chemical, every mind, the random generator's state, and the clock — so the world can be stopped and resumed without losing anything or changing anything.
- **Numbers:** Checkpoints are taken at recorded intervals (for example, every 100 ticks); a resumed run must be bit-identical to an uninterrupted run at the next logged tick.
- **Check:** Stop a test run at a checkpoint, resume it, and compare the state digest at the next logged tick with the uninterrupted run; any difference fails.

**90. Falsifiers decide, not opinions**
- **Rule:** Every claim in the world carries a falsifier — a measurement that would prove it wrong, stated before the measurement is made. If the falsifier fires, the claim is wrong and the record says so; the claim is never quietly reworded to survive.
- **Numbers:** A falsifier is a concrete threshold (for example, "hybrid beats random on first-drink day AND median survival across ≥5 seeds, or the claim fails"); the threshold is recorded before the run, never after.
- **Check:** Every experiment record must name its falsifier and report whether it fired; a record without a falsifier is incomplete and its claim is unconfirmed.

### 1.10 The world holds together

**91. Conservation is checked every run**
- **Rule:** Mass and energy conservation are not assumed — they are measured on every run, in every test, and the numbers are logged. A run that cannot show its conservation numbers is not a valid run, whatever else it claims.
- **Numbers:** Mass drift limit 0.01% per simulated day, energy drift limit 0.01% per simulated day; the conservation check runs at every checkpoint and its result is logged.
- **Check:** A run's log must contain a conservation result at every checkpoint, all within limits; a missing check or a breach fails the run.

**92. Determinism is checked every run**
- **Rule:** Determinism is not assumed either — it is measured by re-running the seed and comparing the state digest. A run that cannot be replayed exactly cannot be trusted, because its results cannot be checked by anyone else.
- **Numbers:** State digest compared at every checkpoint; the digest must match exactly on re-run; the comparison result is logged with the run.
- **Check:** Re-run any recorded run from its seed; every checkpoint digest must match; a single mismatch fails the run's determinism check.

**93. The world survives its own edge cases**
- **Rule:** The world must not crash, freeze, or produce nonsense when it meets an edge case — a body at the boundary, a zero-energy cell, an empty dish, a division by a tiny number. Edge cases are tested deliberately, and the world's behaviour in each one is recorded.
- **Numbers:** Edge-case tests cover at least: empty world, single body, body at the boundary, zero energy, maximum population; each must complete without an error and with a logged outcome.
- **Check:** Run the edge-case suite; every case must finish with a logged result and no crash; a crash or an unlogged outcome fails.

**94. The world runs without an observer**
- **Rule:** The world does not need anyone watching it to keep running: no website, no viewer, no agent online. It advances its own clock, logs its own events, and keeps its own history, and it keeps doing so whether or not anyone is looking.
- **Numbers:** Uptime and tick count are logged continuously; a run with no observer attached must advance at the same tick rate as a run with one, within 5%.
- **Check:** Run the world for 1,000 ticks with no observer and 1,000 ticks with one; the state digests must match and the tick counts must agree; a difference fails.

**95. The world recovers from interruption**
- **Rule:** If the machine stops, the power fails, or the process is killed, the world can be restored from its last checkpoint and continue as if nothing happened. The interruption is logged, the resume is verified, and the history shows no gap and no repeat.
- **Numbers:** Checkpoints are written atomically (a partial checkpoint is discarded, never loaded); resume is verified by comparing the state digest at the next logged tick with the uninterrupted run.
- **Check:** Kill a test run mid-run, resume from the last checkpoint, and compare the next logged state digest with the uninterrupted run; a mismatch fails.

**96. Performance is measured, not guessed**
- **Rule:** The world's speed is measured in ticks per second at stated population sizes, and the measurement is recorded with the hardware it ran on. A claim about how many inhabitants the world can hold is a measured number at a measured speed, never a guess.
- **Numbers:** Tick rate is recorded at 100, 1,000, and 10,000 bodies; population is the maximum the hardware can carry at a usable tick rate, measured not guessed; the hardware is recorded with the number.
- **Check:** A reported tick rate must be reproducible on the same hardware within 10%; a rate that cannot be reproduced is withdrawn.

**97. The world is honest about what it is not**
- **Rule:** The world reports its own limits plainly: what is simulated and what is scenery, what is measured and what is assumed, what the photoreal bar still lacks. A label that says "design" or "scenery" is never removed to make something look more real than it is.
- **Numbers:** Every scene and view carries a label stating whether it shows live simulation, a design, or scenery; the photoreal bar (ray-traced lighting, textured materials, no low-poly) is checked by eye-level screenshot review.
- **Check:** An audit of the site and the viewer must find a correct label on every scene; a live label on a designed scene fails the audit.

**98. The world keeps its history**
- **Rule:** The world's history — births, deaths, extinctions, discoveries, changes to the land — is kept forever in an append-only record, and nothing in it is ever edited or deleted. The past is what it was, even when it is inconvenient.
- **Numbers:** The historical record is append-only with one entry per event, each carrying tick, time, and cause; the record survives checkpoint and resume; its size is logged per run.
- **Check:** A test that writes an event, checkpoints, resumes, and reads the record back must find the event intact; a missing or altered entry fails.

**99. The world is ready for life**
- **Rule:** Phase 1 is done when the fixed laws are in place, measured, and holding: gravity, energy, light, sound, fluids, materials, collisions, time, and scale all behave as in real life, and the checks in this phase all pass. Only then can chemistry and life be built on top of them without the ground shifting underneath.
- **Numbers:** Every Check in topics 1–99 must have a recorded pass with its numbers; a single failing check blocks the phase; the sign-off records the pass count.
- **Check:** The phase sign-off lists all 99 checks with their measured results; a sign-off missing a check, or claiming a pass without numbers, fails.

**100. Phase 1 closes**
- **Rule:** Phase 1 closes when the laws are fixed, the measurements are logged, and the sign-off is recorded: the world now holds together under real physics, and the next phase can build chemistry on a ground that will not move. The closing decision names what the world is ready for and what it is not yet ready for.
- **Numbers:** Closing requires the 99 checks passed, the constants recorded, the determinism and conservation logs complete, and the sign-off message recorded with the date.
- **Check:** The closing record must contain the pass count (99/99), the constants, and the date; a closing record without any of these is not a close.

## Phase 2 — The real world: the planet

### 2.1 The planet (size, spin, tilt, orbit)

**101. Planet radius and mass**
- **Rule:** The planet is a near-sphere whose size and mass set its gravity, surface area, and how much air and water it can hold. Radius and mass are fixed starting values, not tuned during a run; everything else that depends on them is computed from them.
- **Numbers:** Mean radius 6,371 km; mass 5.97 × 10²⁴ kg; surface area 510 million km²; surface gravity 9.81 m/s² at sea level.
- **Check:** A test mass dropped from rest accelerates at 9.81 ± 0.05 m/s² at sea level, and the computed surface area matches 4πr² within 0.1%.

**102. Planet density and composition of the bulk planet**
- **Rule:** Mean density follows directly from mass divided by volume, and it constrains what the interior can be made of: a dense metal core plus a lighter rocky mantle and crust. No interior layer is placed by hand; the density value is the check the layer model must satisfy.
- **Numbers:** Mean density 5,515 kg/m³; core density ~10,000–13,000 kg/m³; mantle ~3,300–5,500 kg/m³; crust ~2,700–3,000 kg/m³.
- **Check:** The layered model's mass-weighted mean density reproduces 5,515 kg/m³ within 1%, and total mass matches 5.97 × 10²⁴ kg within 1%.

**103. Spin period and the length of a day**
- **Rule:** The planet spins once on its axis per day, and that spin defines day and night, the Coriolis effect on winds and currents, and the local solar time used by the Gateway sun geometry. Spin is a fixed rate, not a scripted clock; light and heat follow from the geometry.
- **Numbers:** Sidereal spin period 23 h 56 min; solar day 24 h; equatorial spin speed 465 m/s; angular speed 7.29 × 10⁻⁵ rad/s.
- **Check:** The sun returns to the same meridian after 24.0 ± 0.05 h, and a point on the equator moves 465 ± 5 m/s in the spin direction.

**104. Axial tilt**
- **Rule:** The spin axis is tilted against the orbit plane, so each hemisphere leans toward the sun for half the year and away for the other half. Tilt is the cause of the seasons; without it there would be no seasonal cycle at all.
- **Numbers:** Axial tilt 23.4°; tilt held constant within a run; seasonal solar declination ranges from −23.4° to +23.4°.
- **Check:** Solar declination at the solstices measures +23.4° and −23.4° within 0.2°, and noon sun elevation at latitude 35° swings by 46.8° between solstices.

**105. Orbit size and the length of a year**
- **Rule:** The planet travels once around its star per year on a near-circular path, and the orbit distance sets how much sunlight arrives. Orbit size is a fixed starting value; the year length follows from it and the star's mass by gravity.
- **Numbers:** Mean orbit radius 149.6 million km (1 AU); orbital period 365.25 days; mean orbital speed 29.8 km/s.
- **Check:** The planet returns to the same point in its orbit after 365.25 ± 0.5 days, and mean orbital speed measures 29.8 ± 0.2 km/s.

**106. Orbit shape**
- **Rule:** The orbit is slightly elliptical, so the planet is a little closer to the star at one end of the year and a little farther at the other. That changes sunlight by a few percent across the year, on top of the much larger seasonal effect from tilt.
- **Numbers:** Eccentricity 0.0167; closest approach (perihelion) 147.1 million km; farthest (aphelion) 152.1 million km; sunlight varies ±3.4% between them.
- **Check:** Orbit distance measures 147.1 ± 0.5 million km at perihelion and 152.1 ± 0.5 million km at aphelion, and sunlight varies by 6.8% peak to peak.

**107. Sunlight at the orbit**
- **Rule:** Sunlight arrives as a near-parallel flow whose strength falls with the square of the distance from the star. The top of the atmosphere receives a fixed flux at the mean orbit distance, and every climate, weather, and day-night value downstream is computed from that flux.
- **Numbers:** Solar constant 1,361 W/m² at 1 AU; planetary albedo 0.30; absorbed flux averaged over the sphere 238 W/m².
- **Check:** Flux at the top of the atmosphere measures 1,361 ± 10 W/m² at 1 AU, and the global absorbed mean is 238 ± 5 W/m².

**108. Planet shape: flattening at the poles**
- **Rule:** Spin flattens the planet slightly, so the equator bulges outward and the poles sit closer to the centre. The shape is a consequence of spin and gravity, not a chosen outline, and it sets sea level as an equipotential surface.
- **Numbers:** Equatorial radius 6,378 km; polar radius 6,357 km; flattening 1/298; equatorial gravity 9.78 m/s², polar gravity 9.83 m/s².
- **Check:** Radius measures 6,378 ± 2 km at the equator and 6,357 ± 2 km at the poles, and sea-level gravity rises from equator to pole by 0.05 m/s².

**109. Axis stability and precession**
- **Rule:** The spin axis slowly traces a cone in space, so the direction it points changes over thousands of years while the tilt angle stays near its starting value. Precession is slow enough to ignore inside one run, but it must be present in the long-term model so the seasons drift as they do in real life.
- **Numbers:** Precession period ~26,000 years; axis direction shifts ~50 arcseconds per year; tilt stays within 22.1°–24.5° over 41,000 years.
- **Check:** Axis direction shifts by 50 ± 5 arcseconds per year in the long model, and tilt stays inside 22.1°–24.5° over a 41,000-year integration.

**110. Planet starting values are fixed and recorded**
- **Rule:** Radius, mass, spin, tilt, orbit size, and orbit shape are recorded once with the run seed before the world starts, and they do not change during a run. Any later planet must use the same recording rule, so two runs from the same seed start from the same planet.
- **Numbers:** All six starting values from topics 101–106 recorded to three significant figures with the seed; no value changes by more than 0% during a run.
- **Check:** Two runs from the same seed report identical starting values, and a determinism test re-running the first 1,000 ticks reproduces the planet state exactly.

### 2.2 Land

**111. Continents from plate rules**
- **Rule:** Land appears where thick, light continental crust rides high on the mantle, and oceans sit where thin, dense crust lies low. Continents are the outcome of crust thickness and plate history, never drawn by hand; their shapes come from the same plate rules as the mountains and coasts.
- **Numbers:** Continental crust 30–50 km thick, density ~2,700 kg/m³; oceanic crust 5–10 km thick, density ~3,000 kg/m³; land covers 29% of the surface, 148 million km².
- **Check:** Land fraction measures 29 ± 1% of the surface, and sampled crust thickness is 30–50 km under land and 5–10 km under ocean.

**112. Plate motion**
- **Rule:** The crust is broken into plates that drift over the mantle, carrying continents, opening oceans, and closing them again. Plates move because hot mantle rises and cold slabs sink; the motion is continuous, slow, and driven by heat, not by any schedule.
- **Numbers:** Plate speeds 2–10 cm/year; fastest plates ~10 cm/year; a plate crosses 1,000 km in 10–50 million years.
- **Check:** Plate velocities measured from fixed markers fall in 2–10 cm/year, and no plate moves faster than 12 cm/year or stands still for a full million years.

**113. Mountains from collision**
- **Rule:** Where two plates converge, crust thickens and is pushed upward into mountain ranges, with the highest ground where the thickening is greatest. Mountains grow by collision and are worn down by erosion at the same time, so height is a balance, not a fixed value.
- **Numbers:** Collision uplift 0.5–5 mm/year; highest peaks ~8,000–8,850 m; range widths 100–500 km; crust under high ranges 50–70 km thick.
- **Check:** The highest peak in a mature collision zone measures 7,000–9,000 m, and crust thickness beneath it is 50–70 km.

**114. Rifts and valleys**
- **Rule:** Where plates pull apart, the crust thins, drops down along faults, and forms a rift valley, which can later fill with water or become a new ocean. Valleys also form where rivers cut down through rock, so a valley's shape records whether faulting or flowing water made it.
- **Numbers:** Rift valleys 30–100 km wide, 1–2 km deep; spreading rate at a rift 2–10 cm/year; river valleys deepen 0.1–1 mm/year.
- **Check:** A spreading rift measures 30–100 km wide with fault-bounded walls, and its floor drops as the plates separate at the recorded rate.

**115. Coastlines**
- **Rule:** A coastline is simply where the land surface meets sea level, so it moves whenever sea level changes or the land rises or sinks. Coasts are therefore computed from elevation and sea level at every step, never stored as a fixed line.
- **Numbers:** Sea level is the reference (0 m); coast length scales with measurement resolution; land within 10 km of the coast is lowland below 200 m in most regions.
- **Check:** The computed coastline matches the 0 m elevation contour within one terrain cell, and it shifts measurably when sea level is raised or lowered by 1 m in a test.

**116. Elevation distribution**
- **Rule:** Most land sits low and a small fraction sits very high, because erosion wears high ground down faster than low ground and because most crust is only modestly thick. The elevation histogram is a result of uplift and erosion together, and it must look Earth-like without any target height being imposed.
- **Numbers:** Mean land elevation 840 m; 50% of land below 500 m; less than 2% of land above 4,000 m; deepest ocean floor −11,000 m.
- **Check:** The land elevation histogram has a median below 600 m, a mean of 840 ± 100 m, and under 2% of land above 4,000 m.

**117. Procedural terrain generation**
- **Rule:** Terrain is generated from seeded noise plus the plate rules, at the resolution the viewer needs, so new land beyond the explored edge is produced by the same rules rather than built in advance. The same seed always produces the same terrain, and no terrain is placed by hand.
- **Numbers:** Base terrain grid 1 km per cell at planet scale, refining to 1 m per cell in a locale; noise octaves 6–8; seed recorded with the run.
- **Check:** Two runs from the same seed produce identical terrain cell by cell, and terrain generated beyond the initial edge matches the same statistical distribution as terrain inside it.

**118. Erosion by water and wind**
- **Rule:** Rain, rivers, and wind remove rock and soil from high ground and deposit it lower down, rounding sharp terrain over time. Erosion rate depends on slope, rainfall, and rock hardness, so soft rock under heavy rain wears fastest and hard rock on flat ground barely changes.
- **Numbers:** Typical erosion 0.01–1 mm/year; steep soft slopes up to 5 mm/year; flat hard rock below 0.01 mm/year; sediment carried to the sea in rivers.
- **Check:** A steep soft slope loses 0.5–5 mm/year in a test catchment while a flat hard surface loses under 0.02 mm/year, and eroded mass appears as sediment downstream.

**119. Slope stability and landslides**
- **Rule:** A slope fails when gravity pulling material down exceeds friction and cohesion holding it in place, which happens after heavy rain, shaking, or undercutting at the base. The failed mass slides, falls, or flows downhill until it reaches a gentler angle, and the scar and deposit remain as landforms.
- **Numbers:** Stable slopes below ~30° in soil, below ~45° in rock; failure triggered when pore water pressure rises after 50–100 mm of rain in 24 h; slide volumes 10³–10⁷ m³.
- **Check:** In a test, slopes above 35° in wet soil fail at least 10× more often than slopes below 20°, and every failure leaves a mapped scar and deposit.

**120. Land area and the land–sea balance**
- **Rule:** The share of the surface that is land is set by crust thickness, sea level, and the volume of ocean water together, so changing any one of them moves the balance. The balance is an output to measure, not an input to choose, and it constrains where life on land can ever live.
- **Numbers:** Land 29%, ocean 71%; ocean volume 1.33 billion km³; mean ocean depth 3,700 m; sea level set by ocean volume and basin capacity.
- **Check:** Land fraction measures 29 ± 1%, ocean volume 1.33 ± 0.05 billion km³, and raising ocean volume by 1% in a test raises sea level and shrinks land measurably.

### 2.3 Water

**121. Oceans: depth and volume**
- **Rule:** Oceans fill the low basins between continents, and their depth is the difference between the basin floor and sea level. Ocean volume is fixed by how much water exists and how deep the basins are; basins are made by plate rules, not dug by hand.
- **Numbers:** Ocean volume 1.33 billion km³; mean depth 3,700 m; deepest trench ~11,000 m; shelf seas under 200 m deep cover 8% of ocean area.
- **Check:** Mean ocean depth measures 3,700 ± 100 m, total volume 1.33 ± 0.05 billion km³, and the deepest sounding is 10,500–11,000 m.

**122. Lakes and inland seas**
- **Rule:** A lake forms where a basin on land has no outlet to the sea, or where a river is dammed by landforms, so water collects until inflow balances evaporation and outflow. Lake level rises and falls with that balance, and a lake that loses its inflow dries to a salt flat.
- **Numbers:** Lakes cover ~3% of land; largest lakes 10⁴–10⁵ km²; depths 1–1,600 m; lake level moves 0.1–2 m per year with the water balance.
- **Check:** Every mapped lake sits in a closed or dammed basin, and its level change over a year matches inflow minus evaporation and outflow within 10%.

**123. Rivers: flow downhill**
- **Rule:** Rivers carry water downhill from high ground to the sea or a lake, following the steepest descent of the terrain. Flow speed rises with slope and depth, and the river cuts its channel deeper where flow is fastest, so the channel shape and the flow shape each other.
- **Numbers:** River speeds 0.5–3 m/s; discharge from under 1 m³/s in headwaters to over 200,000 m³/s in the largest rivers; channel gradients 0.01–10 m/km.
- **Check:** Flow direction in every river cell follows the steepest downhill direction, and discharge at a river mouth matches the summed upstream runoff within 10%.

**124. Drainage basins**
- **Rule:** Every point on land belongs to exactly one drainage basin: the catchment whose rivers carry its runoff to a single outlet. Basin boundaries are ridges, computed from the terrain, so a basin's size and shape are outputs of the elevation field.
- **Numbers:** Basins range from under 1 km² to over 7 million km²; the largest river basins drain 5–7 million km²; basin count is set by terrain resolution.
- **Check:** Every land cell is assigned to one basin, basin boundaries lie on ridge lines, and the largest basin measures 5–7 million km².

**125. Groundwater**
- **Rule:** Rain that soaks into the ground fills pore spaces in rock and soil, forming groundwater that flows slowly downhill and feeds springs and rivers from below. Groundwater moves far more slowly than rivers, so it smooths out wet and dry periods.
- **Numbers:** Groundwater flow 0.01–1 m/day; water table 1–100 m below the surface; aquifers 10–1,000 m thick; groundwater supplies ~30% of river flow in dry periods.
- **Check:** The water table sits below the surface in every test borehole, groundwater flow measures 0.01–1 m/day, and river base flow persists through a 30-day dry spell.

**126. Ice: glaciers and polar caps**
- **Rule:** Where snowfall exceeds melting year after year, snow compacts into ice that flows slowly downhill under its own weight, carving valleys as it goes. Ice caps on the poles and glaciers in mountains store water on land, and their melting returns it to the sea.
- **Numbers:** Ice covers ~10% of land; Antarctic ice up to 4,800 m thick; glacier flow 10–1,000 m/year; ice stores ~24 million km³ of water.
- **Check:** Ice thickness measures up to 4,000–4,800 m in the polar cap, glacier flow falls in 10–1,000 m/year, and total stored ice is 24 ± 2 million km³.

**127. Ocean salinity**
- **Rule:** Seawater is salty because rivers carry dissolved minerals from weathered rock into the sea, and evaporation leaves the salt behind while removing pure water. Salinity rises where evaporation exceeds rainfall and falls near river mouths and melting ice.
- **Numbers:** Mean ocean salinity 35 g/kg (35 parts per thousand); open ocean 33–37 g/kg; river water under 0.5 g/kg; saltier basins reach 40 g/kg.
- **Check:** Open-ocean salinity measures 33–37 g/kg in samples, river mouths measure under 5 g/kg, and total ocean salt inventory stays constant within 0.1% per year.

**128. Waves**
- **Rule:** Wind blowing over water drags the surface into waves, whose height grows with wind speed, duration, and the fetch — the distance the wind blows over open water. Waves carry energy, not water, and they break when they reach shallow water near the shore.
- **Numbers:** Typical open-ocean waves 1–3 m high; storm waves 10–15 m; wave periods 5–15 s; fetch of 1,000 km under a 20 m/s wind builds 5–8 m waves.
- **Check:** Wave height rises with wind speed and fetch in the measured relation, and waves break when depth falls below about 1.3 times the wave height.

**129. Ocean currents**
- **Rule:** Surface currents are driven by wind and turned by the planet's spin, while deep currents are driven by differences in temperature and salinity that make some water sink. Currents carry heat from the equator toward the poles and return cold water the other way, linking every ocean basin.
- **Numbers:** Surface currents 0.1–2 m/s; deep currents 0.01–0.1 m/s; the strongest western boundary currents reach 2 m/s; a full deep circuit takes ~1,000 years.
- **Check:** Surface current direction matches wind plus spin deflection in every test region, and deep water at a known sinking site is colder and saltier than the water above it.

**130. Water temperature and layering**
- **Rule:** Sunlight warms the top of the ocean and lakes, while deeper water stays cold, so a warm surface layer sits over cold deep water with a sharp transition between them. Wind and winter cooling mix the layers; calm summer heat stratifies them, and the layering controls what can live at each depth.
- **Numbers:** Surface ocean 0–30°C by latitude; deep ocean 2–4°C; surface mixed layer 10–100 m deep; the transition layer spans 100–1,000 m.
- **Check:** Temperature profiles show a warm mixed layer over a cold deep layer with a transition in between, and deep water measures 2–4°C at every latitude.

### 2.4 Air and weather

**131. Atmosphere composition**
- **Rule:** The air is a mixture of gases held by gravity, dominated by nitrogen and oxygen, with small amounts of water vapour, carbon dioxide, and other trace gases. Composition changes only through physical exchange with land and sea and through the chemistry of Phase 3; no gas is added or removed by hand.
- **Numbers:** Nitrogen 78%, oxygen 21%, argon 0.93%, carbon dioxide 0.042% (420 ppm); water vapour 0–4% by place and season; total air mass 5.15 × 10¹⁸ kg.
- **Check:** Dry-air samples measure 78 ± 0.5% nitrogen and 21 ± 0.5% oxygen, and total air mass is 5.15 ± 0.05 × 10¹⁸ kg.

**132. Atmospheric pressure**
- **Rule:** Air pressure at any height is the weight of the air above that point, so it falls with altitude and varies with temperature and weather. Pressure differences drive wind, and the vertical fall of pressure is set by gravity and temperature together.
- **Numbers:** Sea-level pressure 101,325 Pa (1,013 hPa); pressure halves near 5,500 m; weather systems vary sea-level pressure by ±3,000 Pa.
- **Check:** Pressure at sea level measures 101,325 ± 3,000 Pa, pressure at 5,500 m is half the sea-level value within 5%, and pressure falls smoothly with height.

**133. Air temperature with height**
- **Rule:** Air cools with height because the surface is heated by sunlight and the air above it is heated from below, while the thin upper air radiates heat away. Temperature falls steadily through the lowest layer, then behaves differently above it, and the rate of fall sets whether air rises or stays put.
- **Numbers:** Temperature falls 6.5°C per km in the lowest 11 km; surface mean 15°C; temperature at 11 km about −56°C; the layer above warms again with height.
- **Check:** Temperature profiles fall by 6.5 ± 1°C per km in the lowest 11 km, and the 11 km temperature measures −56 ± 5°C.

**134. Wind and the global circulation**
- **Rule:** Air heated at the equator rises and flows toward the poles, cools, sinks, and returns toward the equator near the surface, forming three circulation cells per hemisphere. The planet's spin turns these flows sideways, producing the trade winds, westerlies, and polar winds.
- **Numbers:** Trade winds 5–10 m/s from the east; mid-latitude westerlies 10–20 m/s; jet streams 30–60 m/s at 10 km height; cells span 0–30°, 30–60°, 60–90° latitude.
- **Check:** Surface winds blow from the east in the tropics and from the west in mid-latitudes, and jet-stream winds at 10 km measure 30–60 m/s.

**135. Clouds**
- **Rule:** A cloud forms when rising air cools until its water vapour condenses onto tiny particles, making droplets or ice crystals. Clouds form where air rises — over warm ground, up mountain slopes, and in weather systems — and they shade the ground and return water as rain.
- **Numbers:** Cloud base 500–2,000 m for low clouds, up to 12,000 m for high clouds; droplets 10–20 μm across; cloud cover averages 60–70% of the sky.
- **Check:** Cloud base height matches the level where rising air reaches saturation within 200 m, and mean cloud cover measures 60–70% over a year.

**136. Rain and other precipitation**
- **Rule:** Precipitation falls when cloud droplets grow heavy enough to overcome rising air, by colliding and merging or by freezing and growing as ice. Rain falls from warm clouds, snow from cold ones, and the amount depends on how much water the air carried and how strongly it rose.
- **Numbers:** Global mean rainfall ~1,000 mm/year over land; wettest places over 10,000 mm/year; driest under 25 mm/year; raindrops 0.5–5 mm across.
- **Check:** Rainfall in a test region matches the measured water-vapour inflow minus outflow within 10%, and rain falls only from clouds whose droplets exceed 100 μm.

**137. Storms and cyclones**
- **Rule:** A storm is a rotating low-pressure system fed by warm moist air rising over a warm ocean or heated land. The rising air spins because of the planet's rotation, winds strengthen as pressure falls, and the storm dies when it moves over cold water or land and loses its heat supply.
- **Numbers:** Tropical cyclone winds 33–90 m/s; central pressure down to 870–950 hPa; storm diameter 200–1,000 km; rainfall 100–500 mm in a day near the centre.
- **Check:** Every cyclone in the record forms over water warmer than 26.5°C, spins counter-clockwise in the north and clockwise in the south, and weakens within 24 h of landfall.

**138. Lightning and thunder**
- **Rule:** Inside a tall storm cloud, ice crystals collide and separate charge, leaving the top of the cloud positive and the base negative. When the charge difference grows large enough, the air breaks down and a lightning bolt discharges it, heating the air so fast that it expands as thunder.
- **Numbers:** Lightning channel temperature ~30,000°C; bolt duration under 1 s; typical flash rate 40–50 per second worldwide; thunder heard up to 25 km away.
- **Check:** Lightning occurs only in clouds taller than ~8 km with ice present, and thunder follows the flash by about 3 s per km of distance.

**139. Humidity, dew, and fog**
- **Rule:** Air holds water vapour up to a limit that rises steeply with temperature, and when air cools to that limit, vapour condenses as dew on surfaces or as fog in the air. Humidity is therefore a temperature story: the same air is dry when warm and wet when cold.
- **Numbers:** Saturation vapour rises from 6 hPa at 0°C to 23 hPa at 20°C; relative humidity 100% at the dew point; fog forms when visibility falls below 1 km.
- **Check:** Dew appears only when the surface cools to the measured dew point within 1°C, and fog is recorded only when relative humidity reaches 100% and visibility falls below 1 km.

**140. Dust and natural aerosols**
- **Rule:** Wind lifts dust from dry ground, salt from sea spray, and ash from volcanoes into the air, where the particles scatter sunlight, seed cloud droplets, and eventually settle or wash out in rain. Aerosol loading is an output of wind, dryness, and eruptions, never a set value.
- **Numbers:** Dust particles 0.1–100 μm; desert dust storms raise particle counts 10–100×; particles stay airborne for hours to weeks; volcanic ash reaches 10–30 km high.
- **Check:** Particle counts rise 10–100× downwind of a dry source during a storm, and counts return to background within two weeks after the source stops.

### 2.5 Climate and seasons

**141. Climate zones by latitude**
- **Rule:** Climate is the long-term average of weather, and its broad pattern is set by latitude: hot and wet near the equator where air rises, dry in the subtropics where air sinks, mild in mid-latitudes, and cold near the poles. Local climate then shifts with altitude, distance from the sea, and mountains.
- **Numbers:** Equatorial mean 25–28°C; subtropical deserts 20–30°C with under 250 mm/year rain; mid-latitudes 5–15°C; polar means below −10°C.
- **Check:** Mean temperature falls by roughly 0.5–0.7°C per degree of latitude from equator to pole, and rainfall peaks at the equator and near 50–60° latitude.

**142. Seasons from tilt**
- **Rule:** Because the axis is tilted, each hemisphere receives more direct sunlight and longer days for half the year and less for the other half. The seasons are the swing in sunlight and day length, not a change in distance from the star, which is the smaller effect.
- **Numbers:** Day length at latitude 50° ranges from ~8 h in winter to ~16 h in summer; noon sun elevation there swings by 47°; seasonal temperature swing 10–25°C at mid-latitudes.
- **Check:** Day length at latitude 50° measures 8 ± 0.5 h at the winter solstice and 16 ± 0.5 h at the summer solstice, and the two hemispheres are six months out of phase.

**143. Seasonal temperature swing**
- **Rule:** Land heats and cools faster than water, so places far from the sea swing widely between summer and winter while coastal places swing little. The swing is a lagged response to sunlight: the warmest days come weeks after the longest day, because the ground and sea take time to warm.
- **Numbers:** Continental interiors swing 25–40°C between January and July means; coastal places swing 5–15°C; warmest month lags the solstice by 4–8 weeks.
- **Check:** January-to-July mean difference measures 25–40°C in a continental interior and 5–15°C on a coast at the same latitude, with the peak lagging the solstice by 4–8 weeks.

**144. Monsoons**
- **Rule:** A monsoon is a seasonal wind reversal: in summer, hot land draws moist ocean air inland, bringing heavy rain; in winter, cold land pushes dry air back out to sea. The reversal is driven by the land–sea temperature contrast, so it is strongest where a large continent faces a warm ocean.
- **Numbers:** Monsoon rainfall 1,000–3,000 mm in a summer season; wind reversal 5–15 m/s; onset within a few weeks of the land reaching ~30°C.
- **Check:** Wind direction in a monsoon region reverses by more than 120° between January and July, and summer rainfall exceeds winter rainfall by at least 5×.

**145. Maritime and continental climates**
- **Rule:** The sea stores heat and releases it slowly, so coastal climates stay mild, while inland climates swing between hot summers and cold winters. The difference is the heat capacity of water against land, and it grows steadily with distance from the coast.
- **Numbers:** Water heat capacity 4,180 J/kg/°C against ~800 J/kg/°C for dry soil; annual temperature range rises ~0.5°C per 100 km inland at mid-latitudes; coasts within 50 km of the sea stay within 15°C annual range.
- **Check:** Annual temperature range at a coastal station is under 15°C while a station 1,000 km inland at the same latitude measures over 30°C.

**146. Climate with altitude**
- **Rule:** Temperature falls with height, so a mountain's climate is colder and wetter than the lowland beside it, and the same sequence of climate bands appears going up a mountain as going toward the poles. Altitude therefore creates stacked climates in a small area.
- **Numbers:** Temperature falls 6.5°C per km of altitude; snow line at ~5,000 m in the tropics and ~1,000 m at high latitudes; rainfall rises with height up to 1–2 km, then falls.
- **Check:** A station 1 km above a lowland station at the same latitude measures 6.5 ± 1°C colder, and the snow line sits higher in the tropics than at high latitudes.

**147. Deserts and arid zones**
- **Rule:** Deserts form where air sinks and warms, drying out as it descends — in the subtropics under the sinking branch of the circulation, and in the rain shadow behind mountains that strip moisture from the wind. A desert is defined by its water balance, not by heat alone.
- **Numbers:** Deserts receive under 250 mm/year of rain; subtropical deserts span roughly 15–30° latitude; rain-shadow deserts sit within 100 km downwind of a range over 2,000 m high.
- **Check:** Every mapped desert receives under 250 mm/year, and its location matches either the 15–30° sinking zone or a rain shadow behind a range over 2,000 m.

**148. Polar climates**
- **Rule:** Near the poles the sun stays low all year, so little heat arrives, snow and ice reflect most of what does arrive, and the ground stays frozen. The cold is self-reinforcing: ice reflects sunlight, which keeps the air cold, which keeps the ice.
- **Numbers:** Polar mean temperatures −10 to −50°C; winter darkness lasts up to 6 months at the pole; summer sun stays above the horizon for up to 6 months; ice albedo 0.8–0.9.
- **Check:** Mean temperature poleward of 70° stays below −10°C, winter darkness at the pole lasts 5–6 months, and ice albedo measures 0.8–0.9.

**149. Year-to-year climate variability**
- **Rule:** Climate varies from year to year because the ocean and atmosphere shift heat around in slow patterns, so a place can have a warm year and a cold year without any change in the planet's starting values. Variability is part of the system, and a single year never defines a climate.
- **Numbers:** Annual mean temperature varies ±0.5–1°C year to year at a place; rainfall varies ±20–40%; ocean heat patterns shift on 2–7 year timescales.
- **Check:** A 30-year record at one place shows annual means varying by ±0.5–1°C with no trend, and no single year's mean is used as the climate value.

**150. Climate as an average, not a setpoint**
- **Rule:** Climate is computed by averaging weather over decades, never by setting a temperature target for a region. If the average is wrong, the weather rules or the sunlight rules are wrong, and the fix belongs there, not in a climate adjustment.
- **Numbers:** Climate means use 30-year averages; a climate value is reported with its year-to-year spread; no region has a prescribed temperature.
- **Check:** Every reported climate value is a 30-year mean with its spread stated, and changing the averaging window from 30 to 20 years moves the value by under 0.5°C.

### 2.6 Day, night, moon, tides

**151. The day–night cycle**
- **Rule:** As the planet spins, each place turns toward the star and then away, so the sun rises, crosses the sky, and sets once per spin. Day length depends on latitude and season, and the cycle is the same geometry that drives the Gateway sun direction, computed from declination and hour angle.
- **Numbers:** Day length 12 h at the equator all year; 0–24 h at the poles by season; solar noon is when the sun crosses the local meridian.
- **Check:** Day length at the equator measures 12.0 ± 0.2 h at every season, and the Gateway sun elevation at solar noon matches the geometric value within 1°.

**152. Dawn, dusk, and twilight**
- **Rule:** Before sunrise and after sunset, sunlight scattered by the upper air still lights the sky, so the change from day to night is gradual rather than sudden. Twilight is longest where the sun sets at a shallow angle, near the poles and in summer at high latitudes.
- **Numbers:** Twilight lasts ~30 min at the equator and 1–2 h at latitude 50° in summer; civil twilight ends when the sun is 6° below the horizon; the sky stays lit while the sun is above −18°.
- **Check:** Measured light at a station falls to night levels only after the sun passes 18° below the horizon, and twilight duration grows with latitude as predicted.

**153. Shadows and solar noon**
- **Rule:** The sun's position in the sky sets the direction and length of every shadow, and at solar noon the sun stands due south in the northern hemisphere and due north in the southern one. Shadow length is a direct measurement of sun elevation, so it checks the solar geometry without any other instrument.
- **Numbers:** At latitude 35°, noon shadow length ranges from 0.7× object height at the summer solstice to 2.0× at the winter solstice; solar noon shifts 4 minutes per degree of longitude.
- **Check:** Noon shadow length at latitude 35° matches the geometric prediction within 5% at both solstices, and solar noon moves 4 minutes per degree of longitude.

**154. The Moon's orbit**
- **Rule:** The Moon circles the planet once per month, held by gravity, and its orbit sets the monthly rhythm of moonlight and tides. The orbit is slightly tilted against the planet's orbit, so the Moon usually passes above or below the star's line and eclipses are rare.
- **Numbers:** Moon distance 384,400 km; orbital period 27.3 days; orbit tilt 5.1°; Moon radius 1,737 km; Moon mass 7.35 × 10²² kg.
- **Check:** The Moon returns to the same stars after 27.3 ± 0.1 days, its distance measures 384,400 ± 5,000 km, and its orbit tilt is 5.1 ± 0.2°.

**155. Moon phases**
- **Rule:** The Moon shines by reflected sunlight, so the phase seen from the planet is the fraction of its sunlit half that faces the planet. Phases run new, crescent, half, gibbous, full, and back again over one synodic month, driven only by the geometry of star, planet, and Moon.
- **Numbers:** Synodic month 29.5 days; full Moon illumination 100%, new Moon 0%; phase advances ~12° per day.
- **Check:** Phase matches the sun–Moon angle within 5°, the full Moon falls 14–15 days after the new Moon, and the cycle repeats in 29.5 ± 0.2 days.

**156. Moonlight**
- **Rule:** Moonlight is sunlight reflected off the Moon's grey surface, far dimmer than direct sunlight but bright enough to see by at full Moon. Its brightness follows the phase and the Moon's height in the sky, and it is the main light source on a clear night.
- **Numbers:** Full Moon light ~0.25 lux against 100,000 lux for sunlight; Moon albedo 0.12; moonlight varies 10× between new and full Moon.
- **Check:** Night light at full Moon measures 0.2–0.3 lux under a clear sky, and it falls by at least 10× at new Moon.

**157. Lunar tides**
- **Rule:** The Moon's gravity pulls the ocean toward it, raising a bulge on the near side, and the planet's spin carries each coast through the bulges, so most places see two high tides per day. The tide is a real water movement, not a water-level setting, and it moves with the Moon.
- **Numbers:** Two high tides per lunar day (24 h 50 min); open-ocean tide range 0.5–1 m; coastal ranges up to 15 m in funnel-shaped bays; tidal currents 1–3 m/s.
- **Check:** High tides at a coastal station recur every 12 h 25 min ± 15 min, and the tide range grows toward the Moon's overhead passage.

**158. Spring and neap tides**
- **Rule:** The star also raises tides, smaller than the Moon's, and the two add when star, planet, and Moon line up at new and full Moon, and partly cancel when they stand at right angles at the quarter Moons. The monthly spring–neap cycle is therefore a geometry check on both tides at once.
- **Numbers:** Spring tides ~20% higher than the mean range; neap tides ~20% lower; solar tide is 46% of the lunar tide; cycle period 14.8 days.
- **Check:** Tide range peaks within 2 days of new and full Moon and is smallest within 2 days of the quarter Moons, with spring range about 1.5× the neap range.

**159. Eclipses**
- **Rule:** An eclipse happens when the three bodies line up closely enough that one shadow falls on another: the Moon blocks the star during a solar eclipse, and the planet's shadow covers the Moon during a lunar eclipse. Eclipses are rare because the Moon's orbit is tilted, so line-ups usually miss.
- **Numbers:** Solar eclipses 2–5 per year somewhere on the planet, totality lasting up to 7.5 min; lunar eclipses 2–4 per year; eclipse seasons recur every 173 days.
- **Check:** Every recorded eclipse falls within an eclipse season, the Moon is new at a solar eclipse and full at a lunar one, and totality never exceeds 7.5 min.

**160. The night sky and the stars**
- **Rule:** At night the sky shows the distant stars, whose positions shift with the seasons as the planet moves around the star, while the Moon and planets move against them on their own schedules. The star field is a fixed background for navigation, consistent with the same orbit geometry as day and night.
- **Numbers:** Stars visible to the naked eye ~6,000 over the whole sky; the sky rotates 360° per sidereal day; seasonal star shift 360° per year.
- **Check:** A star's rising time shifts earlier by ~4 minutes per night, and the same constellations return to the same place in the sky after one year.

### 2.7 The water cycle

**161. Evaporation from oceans**
- **Rule:** Sunlight heats the sea surface, and water molecules escape into the air as vapour, faster when the water is warm, the air is dry, and the wind is strong. Evaporation is the water cycle's main source, and the vapour it makes is pure water — the salt stays behind.
- **Numbers:** Ocean evaporation ~425,000 km³/year; warm tropical seas evaporate 1,500–2,000 mm/year; cold polar seas under 200 mm/year; evaporation rises ~7% per °C of warming.
- **Check:** Evaporation over a test ocean patch matches the measured heat input divided by the latent heat of vaporisation within 10%, and the vapour contains no salt.

**162. Evaporation from land surfaces**
- **Rule:** Water on soil, in puddles, and on wet surfaces evaporates by the same rule as the sea, limited by how much water is actually there. Dry soil stops evaporating once its surface dries, even under hot sun, so land evaporation is capped by supply as well as by heat.
- **Numbers:** Land evaporation ~70,000 km³/year; wet soil evaporates 3–6 mm/day in summer sun; dry soil under 0.5 mm/day; a puddle 10 mm deep dries in 2–5 days of sun.
- **Check:** A wet soil tray loses 3–6 mm/day under summer sun while a dry tray loses under 0.5 mm/day, and evaporation stops when the surface moisture reaches zero.

**163. Condensation and cloud water**
- **Rule:** When moist air rises and cools to its dew point, vapour condenses into droplets, releasing the heat that evaporation absorbed. Condensation is therefore the mirror of evaporation: it returns heat to the air and turns invisible vapour into visible cloud water.
- **Numbers:** Condensation releases 2.5 MJ per kg of water; cloud water content 0.1–1 g/m³; droplets grow from 10 μm to 100 μm before they can fall.
- **Check:** Rising air cools at the dry rate until saturation, then at the slower wet rate, and the heat released matches 2.5 MJ per kg condensed within 5%.

**164. Precipitation returns water to the ground**
- **Rule:** When cloud droplets or ice grow heavy enough, they fall as rain, snow, or hail, returning water to land and sea. Where the falling water lands decides the rest of the cycle: on the sea it is back at the start, on land it runs off, soaks in, or freezes.
- **Numbers:** Global precipitation ~505,000 km³/year; about 80% falls on the oceans, 20% on land; snow falls where air is below 0°C; hail needs updrafts over 10 m/s.
- **Check:** Total precipitation over a closed test region matches the measured vapour inflow minus outflow within 10%, and snow is recorded only where air temperature is below 0°C.

**165. Runoff to rivers and sea**
- **Rule:** Rain that does not soak in flows downhill over the surface, joining streams and rivers that carry it to the sea or a lake. Runoff is fast after heavy rain on steep ground and slow where the ground is flat and porous, so the same rainfall can produce a flood or a gentle rise.
- **Numbers:** Global runoff ~40,000 km³/year from land; runoff is 10–60% of rainfall depending on soil and slope; flood peaks arrive hours after heavy rain in small catchments.
- **Check:** Runoff at a catchment outlet matches rainfall minus infiltration and evaporation within 10% over a month, and the flood peak follows the heaviest rain by hours, not days.

**166. Infiltration into soil and rock**
- **Rule:** Rain soaks downward through soil pores under gravity, filling the soil first and then draining to groundwater below. Infiltration is fastest in sandy soil and slowest in clay, and it stops when the soil is saturated, after which extra rain must run off.
- **Numbers:** Infiltration rates 5–50 mm/h in sand, 1–5 mm/h in clay; soil holds 100–300 mm of water per metre of depth; a saturated soil takes in no more water.
- **Check:** A sand column takes in 5–50 mm/h while a clay column takes in 1–5 mm/h, and infiltration falls to zero once the soil reaches saturation.

**167. Snow accumulation and melt**
- **Rule:** Snow piles up where it falls faster than it melts, storing water through winter as a solid reservoir, and releases it in spring when temperatures rise above freezing. Melt water runs off or soaks in, so the spring melt is the largest flow event of the year in snowy regions.
- **Numbers:** Snow density 100–300 kg/m³ fresh, up to 500 kg/m³ old; a 1 m snowpack holds 100–300 mm of water; melt rates 5–30 mm/day in spring sun.
- **Check:** A snowpack's water content matches its depth times its measured density within 10%, and melt begins only when air temperature rises above 0°C.

**168. Water residence times**
- **Rule:** A water molecule stays in each part of the cycle for a characteristic time: days in the air, weeks in a river, years in a lake, centuries in deep groundwater, and thousands of years in ice. Residence time is volume divided by flow, so it is computed from the cycle, not assumed.
- **Numbers:** Atmosphere ~9 days; rivers ~2 weeks; lakes 1–100 years; shallow groundwater 10–100 years; deep groundwater 1,000–10,000 years; polar ice 10,000+ years.
- **Check:** Atmospheric water content divided by global precipitation gives 9 ± 2 days, and a tracer released in a river reaches the sea within the predicted weeks.

**169. Water-cycle mass balance**
- **Rule:** Water is neither created nor destroyed in the cycle: evaporation plus inflow must equal precipitation plus outflow plus the change in storage, for every region and for the planet as a whole. The balance is the conservation check for the whole water system, and any gap is a bug, not a rounding choice.
- **Numbers:** Global evaporation 505,000 km³/year equals global precipitation 505,000 km³/year within measurement error; land precipitation 110,000 km³/year against land evaporation 70,000 km³/year and runoff 40,000 km³/year.
- **Check:** The global balance closes within 1%, and every regional balance closes within 5% over a year, with storage change accounted for.

**170. Droughts and floods as cycle extremes**
- **Rule:** A drought is the cycle running dry — evaporation and outflow exceeding inflow for months — and a flood is the cycle running over — rainfall exceeding what soil and rivers can take. Both are outputs of the same balance rules, with return times measured from the record.
- **Numbers:** Drought is rainfall below 50% of the 30-year mean for 3+ months; a flood is river flow above the 10-year level; a 100-year flood has a 1% chance in any year.
- **Check:** Droughts in the record match months where inflow fell below half the mean, floods match flows above the 10-year level.

### 2.8 Soil and minerals

**171. Soil formation by weathering**
- **Rule:** Soil forms where rock weathers in place: water, temperature swings, and physical breakage split rock into grains, and the grains mix with mineral matter over time. Soil is therefore rock that has been broken and sorted where it lies, and its depth grows as weathering works downward.
- **Numbers:** Soil forms at 0.01–0.1 mm/year; typical soil depth 0.5–2 m; weathering is fastest in warm, wet climates and slowest in cold, dry ones.
- **Check:** Soil depth over a known-age surface matches the formation rate within a factor of two, and the soil's mineral grains match the rock beneath it.

**172. Soil layers**
- **Rule:** A mature soil is layered: a dark top layer rich in broken-down material, a middle layer where minerals collect, and a lower layer of partly weathered rock above solid rock. The layers form because water carries fine material downward, so the profile records the direction water has moved.
- **Numbers:** Top layer 0–30 cm; middle layer 30–100 cm; weathered rock 100–200 cm; layer boundaries are gradual over 5–20 cm.
- **Check:** A soil pit shows three distinct layers in the stated depth ranges, and the middle layer contains more fine mineral grains than the top layer.

**173. Soil texture: sand, silt, and clay**
- **Rule:** Soil texture is the share of sand, silt, and clay grains, set by the parent rock and by how far water has carried and sorted them. Texture decides how fast water drains, how much water the soil holds, and how easily roots and burrowing bodies can move through it.
- **Numbers:** Sand grains 0.05–2 mm; silt 0.002–0.05 mm; clay under 0.002 mm; sandy soil drains 10× faster than clay soil and holds half as much water.
- **Check:** Sieve and settling tests place every sampled soil in the sand–silt–clay triangle, and measured drainage matches the texture class within a factor of two.

**174. Soil water holding**
- **Rule:** Soil holds water in its pores against gravity, more in fine clay soils and less in coarse sand, and the held water is what land surfaces can evaporate and what roots can draw on. Water above the holding capacity drains away to groundwater, so holding capacity caps the soil's water store.
- **Numbers:** Holding capacity 100–300 mm per metre of soil; sand holds ~100 mm/m, clay ~250 mm/m; water drains from a saturated soil to holding capacity within 1–3 days.
- **Check:** A saturated soil column drains to its measured holding capacity within 3 days, and sand holds about half the water clay holds per metre.

**175. Rock types: igneous, sedimentary, metamorphic**
- **Rule:** Rock comes in three families by how it formed: cooled from molten rock, laid down as sediment and pressed into stone, or changed by heat and pressure deep underground. Each family has its own hardness and grain, and the rock map records the planet's volcanic, surface, and deep history.
- **Numbers:** Igneous rock forms above 700°C; sedimentary layers 0.1–10 mm/year of deposition; metamorphic change needs 200–800°C and high pressure; crust is roughly 65% igneous, 25% metamorphic, 10% sedimentary by volume at the surface.
- **Check:** Every sampled outcrop is classified into one of the three families by grain and structure, and its formation temperature or deposition rate falls in the stated range.

**176. Mineral deposits and ores**
- **Rule:** Useful minerals concentrate where water, heat, or settling sorts them: hot water deposits metals in cracks near volcanoes, heavy minerals settle in river beds, and evaporation leaves salts in drying lakes. A deposit is therefore found by following the process that made it, never by placing it.
- **Numbers:** Ore-grade rock holds 0.5–5% metal by mass against 0.001–0.01% in ordinary rock; vein deposits are 0.1–10 m wide and 100–1,000 m long; placer deposits sit in river bends and deltas.
- **Check:** Metal concentration in a sampled vein is 100× the background rock value, and the deposit's location matches a fault, a river bend, or a dried lake as the process predicts.

**177. Weathering exposes fresh minerals**
- **Rule:** As erosion strips the surface away, deeper rock is exposed and begins to weather, releasing fresh mineral grains into the soil. Exposure is therefore a conveyor: uplift and erosion bring new rock up, weathering breaks it down, and rivers carry the products away.
- **Numbers:** Erosion exposes 0.01–1 mm/year of fresh rock; a mountainside stripped by 1 m exposes rock last at the surface 1,000–100,000 years ago; river sediment is 50–90% freshly weathered grains.
- **Check:** Sediment in a mountain river matches the rock now exposed upstream, and the exposure rate matches the measured erosion rate within a factor of two.

**178. Soil loss by erosion**
- **Rule:** Soil is lost when rain and wind carry its top layer away faster than weathering makes new soil below, which happens on steep bare slopes and in heavy rain. Lost soil becomes river sediment and, eventually, new sedimentary rock, so soil loss in one place is soil gain downstream.
- **Numbers:** Natural soil loss 0.01–0.1 mm/year; bare steep slopes lose 1–10 mm/year; a soil 1 m deep is gone in 100–1,000 years at that rate.
- **Check:** A bare steep plot loses 1–10 mm/year of topsoil while a flat covered plot loses under 0.1 mm/year, and the lost mass appears as sediment in the stream below.

**179. Salt flats and evaporite minerals**
- **Rule:** Where a lake has no outlet and evaporation exceeds inflow, the water shrinks and the dissolved minerals it carried are left behind as salt crusts. The crust thickens layer by layer as the lake dries and refills, recording wet and dry years in its bands.
- **Numbers:** A lake evaporating 1 m/year leaves 1–35 kg of salt per m² per year depending on salinity; salt crusts reach 1–100 m thick over thousands of years; halite forms above 350 g/l salinity.
- **Check:** A drying test lake leaves a salt crust whose mass matches the evaporated water volume times its measured salinity within 10%.

**180. Soil and mineral maps are outputs, not inputs**
- **Rule:** The map of soils and minerals is computed from rock type, weathering, erosion, water flow, and deposition, and re-computed whenever any of those change. No soil type or ore body is drawn by hand; the map measures the processes, and changes as they do.
- **Numbers:** Maps are stored at 1 km per cell; every cell carries its parent rock, texture class, and deposit flag; maps are regenerated from process state, not edited.
- **Check:** Deleting the map and regenerating it from process state reproduces the same map cell by cell, and a change in rainfall or erosion changes the map in the predicted direction.

### 2.9 The deep earth (volcanoes, quakes)

**181. The interior layers**
- **Rule:** The planet is layered by density: a solid inner core, a liquid outer core, a solid but slowly flowing mantle, and a thin brittle crust on top. The layers are the result of the planet sorting itself by density as it cooled, and each layer's depth and state constrain the others.
- **Numbers:** Inner core radius 1,220 km, solid; outer core 1,220–3,480 km, liquid; mantle 3,480–6,371 km; crust 5–70 km; core temperature 5,000–6,000°C.
- **Check:** Seismic waves speed up, slow down, and bend at the measured layer boundaries, and the layer depths reproduce the observed travel times within 1%.

**182. Heat from the interior**
- **Rule:** Heat flows outward from the deep interior, where it comes from the planet's original formation heat and from radioactive decay in the rocks. The heat flow is small compared with sunlight at the surface, but it drives mantle motion, volcanoes, and hot springs from below.
- **Numbers:** Mean surface heat flow 87 mW/m²; temperature rises 25–30°C per km of depth; total interior heat output ~47 TW against ~173,000 TW of absorbed sunlight.
- **Check:** Borehole temperatures rise 25–30°C per km, and the integrated surface heat flow measures 47 ± 5 TW.

**183. Mantle convection and plate driving**
- **Rule:** Hot mantle rock rises, cools near the surface, and sinks again in a slow overturn, and the plates ride on that motion while cold sinking slabs pull them along. Convection is the heat transport of the interior made visible as plate motion, and its speed sets the plate speeds.
- **Numbers:** Mantle flow 1–10 cm/year; a full overturn takes 100–500 million years; mantle viscosity 10²⁰–10²² Pa·s.
- **Check:** Plate speeds fall in the same 2–10 cm/year range as mantle flow, and the direction of plate motion matches the direction of the underlying mantle flow.

**184. Volcanoes**
- **Rule:** A volcano forms where molten rock rises to the surface: at plate boundaries where plates pull apart or one sinks beneath another, and at hot spots where a plume rises through a plate. The molten rock erupts as lava and ash, builds a cone, and the cone's shape records the lava's thickness and the eruption style.
- **Numbers:** Magma temperature 700–1,200°C; eruption rates 0.1–1,000 m³/s; cones 100–4,000 m high; about 1,500 volcanoes have erupted in the last 10,000 years.
- **Check:** Every mapped volcano sits on a plate boundary or a hot spot, its lava temperature falls in 700–1,200°C, and its cone height matches the erupted volume.

**185. Eruption styles**
- **Rule:** Runny lava flows quietly and builds broad shields, while thick, gas-rich magma explodes, throwing ash high into the air and building steep cones. The style is set by the magma's silica content and gas, so the same volcano can change style if its magma changes.
- **Numbers:** Low-silica lava (under 52% SiO₂) flows at 1–10 m/s; high-silica magma (over 63%) explodes; ash columns reach 10–40 km; explosive eruptions eject 0.1–1,000 km³ of material.
- **Check:** Eruptions with lava under 52% silica are recorded as flows and those over 63% as explosions, and ash-column height rises with the measured gas content.

**186. Earthquakes: fault slip**
- **Rule:** An earthquake is a sudden slip on a fault, where plates have been stuck while stress built up, and the stored elastic energy is released as shaking. The slip is fast, the stress build-up is slow, and the fault's location and orientation decide which way the ground moves.
- **Numbers:** Fault slip 0.1–10 m per event; stress builds at 0.01–0.1 MPa/year; shaking lasts 10–100 s; most quakes occur at 0–70 km depth, deep ones to 700 km.
- **Check:** Ground displacement across a fault after a quake matches the measured slip within 10%, and the shaking direction matches the fault's orientation.

**187. Earthquake size and frequency**
- **Rule:** Earthquake size follows a strict pattern: for each step up in magnitude, there are about ten times fewer events, and each event releases about thirty-two times more energy. Small quakes are common and large ones rare, by the same rule everywhere, and the pattern is the check that the fault system is behaving naturally.
- **Numbers:** Magnitude 0–9.5; a magnitude 5 releases ~2 × 10¹² J; magnitude 9 releases ~2 × 10¹⁸ J; about 100 magnitude 6+ quakes per year worldwide, one magnitude 8+ per year.
- **Check:** The recorded quake counts follow the ten-to-one rule within 20% per magnitude step, and the largest recorded quake does not exceed magnitude 9.5.

**188. Tsunamis**
- **Rule:** When a quake lifts or drops the sea floor, it displaces the whole water column above it, launching a wave that travels fast in deep water and grows tall as it reaches the shore. A tsunami is a water wave made by the sea floor moving, not by wind, and its arrival time is set by ocean depth.
- **Numbers:** Tsunami speed 500–800 km/h in deep water, slowing to 30–50 km/h near shore; open-ocean height under 1 m, shore height 1–30 m; travel time across an ocean 5–20 h.
- **Check:** Arrival times at coastal stations match depth-based speed predictions within 10%, and the wave height grows as the water shallows, as the rule predicts.

**189. Hot springs and geothermal surface heat**
- **Rule:** Where groundwater sinks deep enough to be heated by the interior, it rises again as a hot spring, carrying heat and dissolved minerals to the surface. Hot springs mark places where deep heat reaches shallow water, and their temperature records how deep the water went.
- **Numbers:** Hot spring temperatures 30–100°C; water circulates to 1–5 km depth; heat output per spring 0.1–100 MW; geysers erupt when water flashes to steam.
- **Check:** Spring water temperature matches the depth it circulated to at 25–30°C per km, and springs cluster where heat flow is above the 87 mW/m² mean.

**190. The magnetic field from the core**
- **Rule:** The liquid outer core flows as the planet spins, and the moving conductive fluid generates a magnetic field that shields the surface from charged particles from the star. The field is a product of core motion and spin, and it changes slowly as the core flow changes.
- **Numbers:** Surface field strength 25–65 μT; field is roughly a dipole tilted 11° from the spin axis; the dipole drifts and reverses every 200,000–300,000 years on average.
- **Check:** Compass readings match a dipole tilted 11 ± 1° from the spin axis, surface strength measures 25–65 μT, and the field direction matches the core-flow model within 5°.

### 2.10 The planet is one system

**191. Planetary energy balance**
- **Rule:** The planet warms until the heat it radiates back to space equals the sunlight it absorbs, so its mean temperature is the balance point of incoming and outgoing energy. If absorption rises or radiation falls, the planet warms until balance returns; nothing sets the temperature directly.
- **Numbers:** Absorbed sunlight 238 W/m²; outgoing radiation 238 W/m² at balance; mean surface temperature 15°C; a 1 W/m² imbalance warms the planet ~0.5–1°C over decades.
- **Check:** Global absorbed and outgoing fluxes match within 1 W/m² over a year, and the mean temperature sits at the value the balance predicts within 1°C.

**192. Land, water, and air are coupled**
- **Rule:** No part of the planet acts alone: the sea warms the air above it, the air carries water to the land, the land returns water and sediment to the sea, and the land's height steers the wind. A change in any one part propagates through the others, so the planet must be simulated as one system.
- **Numbers:** Ocean-to-air heat transfer 50–200 W/m²; land rainfall depends on upwind sea evaporation within 1,000 km; river sediment delivery 20 billion tonnes/year to the sea.
- **Check:** In a test, warming a sea region by 1°C raises downwind rainfall measurably, and cutting a river's flow changes the coastal sediment deposit within a year.

**193. Feedbacks: ice, clouds, and water vapour**
- **Rule:** Feedbacks amplify or dampen change: ice reflects sunlight, so less ice means more warming; warmer air holds more water vapour, which traps more heat; clouds both shade the ground and trap heat, with the net effect depending on their height. Feedbacks are computed from the physics, never tuned to produce a chosen climate.
- **Numbers:** Ice albedo 0.8–0.9 against ocean 0.06; water vapour rises 7% per °C; low clouds cool by ~20 W/m², high clouds warm by ~10 W/m².
- **Check:** A test that melts 10% of the ice raises absorbed sunlight by the albedo difference times the area, and vapour content rises 7 ± 1% per °C of warming.

**194. Sea level as a coupled output**
- **Rule:** Sea level is set by ocean volume, ocean temperature, and water stored as ice on land, so it rises when ice melts or the ocean warms and expands, and falls when ice grows. Sea level is therefore an output of climate and ice, not an input, and the coastline moves with it.
- **Numbers:** Thermal expansion ~1.5 mm/year per °C of ocean warming; melting all land ice would raise sea level ~70 m.
- **Check:** In a test, warming the ocean by 1°C raises sea level by the expansion amount within 10%, and melting a measured ice volume raises it by volume divided by ocean area.

**195. Timescales: weather, climate, and geology together**
- **Rule:** The planet runs on nested timescales — weather in hours, seasons in months, climate in decades, ice in millennia, plates in millions of years — and the slow systems set the stage the fast ones play on. A run must carry all of them at once, with the slow ones changing the background while the fast ones respond.
- **Numbers:** Weather 1–10 days; seasons 90 days; climate means 30 years; ice sheets respond over 1,000–10,000 years; plates move 2–10 cm/year.
- **Check:** A 30-year run shows weather varying daily, seasons repeating yearly, and the plate positions moved by the recorded 2–10 cm/year, all in the same run.

**196. Regional coupling: coasts**
- **Rule:** A coast is where every system meets: tides and waves shape the shore, rivers deliver sediment, sea air brings rain, and the land's height decides what grows and lives there. Change the tide, the river, or the wind, and the coast changes — the coast is the test case for coupling, not a separate topic.
- **Numbers:** Coastal erosion 0.1–10 m/year; deltas grow 10–100 m/year where sediment supply is high; salt spray reaches 100 m–1 km inland.
- **Check:** A test coast with doubled river sediment grows its delta measurably within a year, while a coast with the river cut off erodes at the measured wave rate.

**197. Ocean–atmosphere coupling**
- **Rule:** The ocean stores heat through the seasons and returns it to the air, while the wind drives the surface currents and the currents carry the heat. Warm ocean water feeds storms, cold water calms them, and the exchange is two-way at every step: neither the sea nor the sky leads on its own.
- **Numbers:** Ocean heat capacity per square metre is ~1,000× the air above it; sea-surface temperature anomalies of 1°C shift rainfall by 10–30%; storm formation needs water above 26.5°C.
- **Check:** A 1°C warm patch in the test ocean raises rainfall downwind by 10–30% and increases storm formation, while a cold patch does the opposite.

**198. The planet's state is observable through the Gateway**
- **Rule:** The planet's state — sun position from real solar geometry, world snapshot, tick, population, and field values — is served read-only through the Gateway contract (GET /api/world, /api/stream, /api/health, loopback only), as specified in docs/implementation/GATEWAY_CONTRACT.md. Observation is one-way: watching changes nothing, and the world never senses a watcher.
- **Numbers:** Snapshot contract version 1; stream ~20 Hz; a client marks data stale after 3 s without a new frame; sun elevation and azimuth come from declination and hour angle; latitude 35°, longitude 0° are viewer initial conditions, stated in the payload.
- **Check:** GET /api/health returns {"ok": true} with a strictly increasing tick, /api/world sun elevation matches geometry within 1°, and no write path exists.

**199. The protocell pond sits inside the planet**
- **Rule:** The live protocell pond is the served baseline and the origin-of-life bar: six criteria (origin, replication, compartment, metabolism, variation, selection) must all pass 3/3 with clean controls, per docs/implementation/PROTOCELL_LIFE_CRITERION.md. The pond is a bounded water body inside the planet's water system, not a separate world, and follows the same water, heat, and light rules as the rest of the planet.
- **Numbers:** Validation seeds 20261105, 20261106, 20261107; first catalyst at ticks 265/289/282; first copy at 353/330/285; generation 67/67/69; criterion 6 margin +0.15/+0.14/+0.18 over the neutral control.
- **Check:** All six criteria pass 3/3 with the no-catalysis control at zero catalysed births, and the pond's temperature and light follow the planet's day–night and seasonal rules.

**200. Phase 2 sign-off: the whole planet, tested as one system**
- **Rule:** Phase 2 is done when the planet runs as one coupled system — land, water, air, climate, day and night, tides, soil, and deep earth all active at once — with mass and energy conserved, the same seed reproducing the same planet, and every topic's check recorded with its measured number. Nothing is claimed done from one subsystem test alone.
- **Numbers:** Global mass balance closes within 1%; energy balance within 1 W/m²; a determinism re-run reproduces the planet state exactly over 1,000 ticks; all 100 topics have a recorded check.
- **Check:** A 30-day integrated run passes the mass and energy balances, the determinism re-run matches exactly, and the sign-off lists the measured result for each topic.

## Phase 3 — The real world: energy, materials, and living chemistry

### 3.1 Sunlight

**201. The sun as the energy source**
- **Rule:** A star like Earth's sun shines on the planet, and its light is the main energy input to the world. Light travels in straight lines, is blocked by solid ground, and falls on surfaces at an angle that depends on the time of day and the season. Nothing in the world creates light energy for free.
- **Numbers:** Solar constant at the top of the atmosphere ~1,361 W/m²; about 1,000 W/m² reaches the ground at noon on a clear day; the planet's mean absorbed flux is ~240 W/m² after reflection and night.
- **Check:** Measure top-of-atmosphere flux and ground flux at noon over 5 clear days; ground flux must be 800–1,100 W/m² and the daily mean within 10% of the value predicted from latitude and season, or the light model is wrong.

**202. Day and night from rotation**
- **Rule:** The planet turns once per day, so each place faces the sun for about half the day and faces away for the other half. Sunrise and sunset move with the seasons because the planet's axis is tilted. Light and dark are set by geometry alone, never by a scripted clock.
- **Numbers:** Day length 24 h; axial tilt 23.4°; rotation gives a solar day of 24 h and a night of roughly 12 h at the equator, varying from ~0 to 24 h at the poles by season.
- **Check:** Record sunrise and sunset times at latitude 35° for 30 days; they must match the geometric prediction within 10 minutes, and total darkness must occur on the night side, or the rotation model fails.

**203. Seasons from tilt and orbit**
- **Rule:** The tilted axis means each hemisphere leans toward the sun for half the year and away for the other half, so summers are warmer and longer and winters cooler and shorter. The orbit is nearly circular, so tilt, not distance, drives the seasons. The year is one full orbit.
- **Numbers:** Tilt 23.4°; year 365.25 days; at latitude 35°, noon sun elevation ranges from ~31.6° at winter solstice to ~78.4° at summer solstice; day length ranges from ~9.8 h to ~14.4 h.
- **Check:** Measure noon elevation and day length at the solstices and equinoxes; both must match the tilt geometry within 1° and 15 minutes, or the seasonal model is wrong.

**204. Light colour and spectrum**
- **Rule:** Sunlight is a mix of wavelengths: ultraviolet, visible light, and infrared. Short wavelengths carry more energy per photon; infrared is felt mainly as heat. The sky looks blue because air scatters short wavelengths more strongly, and sunsets look red because the light travels through more air.
- **Numbers:** Visible band 380–750 nm; peak solar output near 500 nm; UV below 400 nm is ~8% of surface energy; scattering strength scales roughly as wavelength to the power −4.
- **Check:** Measure the spectrum at noon and at sunset; the blue-to-red ratio must fall by at least a factor of 3 at sunset, and UV must be present at noon, or the spectrum model fails.

**205. Sun shadows and shadow length**
- **Rule:** Solid objects block light and cast shadows on the side away from the sun. A shadow is dark but not black, because scattered sky light still reaches it. Shadows move as the sun moves, lengthen near dawn and dusk, and shrink at noon.
- **Numbers:** Shadow length equals object height divided by the tangent of sun elevation; at 10° elevation a 1 m object casts a ~5.7 m shadow; shadowed ground receives ~10–30% of direct sunlight as scattered sky light.
- **Check:** Place a 1 m post and measure its shadow length at three sun elevations; lengths must match the tangent rule within 5%, or the light-blocking rule is wrong.

**206. Reflection and albedo**
- **Rule:** Every surface reflects some light and absorbs the rest. Bright surfaces such as snow and sand reflect most light and stay cooler; dark rock and water absorb most and warm faster. Reflected light still carries energy and can light shaded places.
- **Numbers:** Albedo: fresh snow 0.8–0.9, sand 0.3–0.4, grass 0.2–0.25, forest 0.1–0.15, ocean 0.06–0.10; planetary mean albedo ~0.30.
- **Check:** Measure reflected flux over snow, sand, grass, and water at noon; albedos must fall in the stated ranges within 0.05, or the reflection model fails.

**207. Light in water**
- **Rule:** Light entering water is bent, scattered, and absorbed, so it fades with depth and loses red wavelengths first. Shallow clear water is bright and blue-green; deep water is dark. Anything living in water gets less light the deeper it sits.
- **Numbers:** In clear water, light falls to ~10% at ~10 m and ~1% at ~20–30 m; red light is absorbed within the first few metres; the photic zone extends to roughly 100 m in the clearest water.
- **Check:** Measure light at 0, 5, 10, and 20 m depth in clear water; values must fall within a factor of 2 of exponential decay with the stated depths, or the water-light model is wrong.

**208. Light as a signal, not just heat**
- **Rule:** Light level, direction, and colour are information a living thing can sense, separate from the warmth light brings. A creature can tell day from night, find the sun's direction, and sense shade without measuring temperature. Light sensing uses the same photons that warm the world.
- **Numbers:** Daylight is 10,000–100,000 lux; twilight is 1–100 lux; full moonlight is ~0.1–0.3 lux; a light sensor must distinguish at least a 100-fold range to tell day from twilight.
- **Check:** Log light level every hour for 5 days; day must exceed 1,000 lux, night must fall below 1 lux, and the sensor reading must track the solar elevation curve, or the light signal is wrong.

**209. Solar energy budget**
- **Rule:** All solar energy that enters the world is accounted for: part is reflected back to space, part warms the ground and air, part evaporates water, and part is stored in chemical bonds by any process that captures it. Energy is conserved; the books must balance.
- **Numbers:** Of ~340 W/m² arriving at the top of the atmosphere, ~100 W/m² is reflected, ~160 W/m² is absorbed by the surface, and ~80 W/m² by the air; evaporation carries ~80 W/m² as latent heat.
- **Check:** Run a 30-day energy audit: incoming minus reflected minus stored minus outgoing must close within 5 W/m², or the budget leaks energy.

**210. The sun in the Gateway feed**
- **Rule:** The Gateway reports the sun's real position from solar geometry — declination and hour angle from latitude, longitude, and time — so the viewer and the world agree on where the sun is. The feed carries elevation, azimuth, direction, and whether it is day; it never invents a sun position.
- **Numbers:** Gateway sun fields: elevation_deg, azimuth_deg, direction as a unit vector, is_day, latitude_deg 35.0, longitude_deg 0.0; clock starts at dawn, 06:20 local solar time, advancing 1:1.
- **Check:** Compare the Gateway sun elevation and azimuth against the geometric prediction for the same time and place over 24 h; both must agree within 1°, and is_day must flip at sunrise and sunset, or the feed is wrong.

### 3.2 Heat and temperature

**211. Temperature as molecular motion**
- **Rule:** Temperature measures how fast molecules move on average. Heat flows from warmer things to cooler things until they match. Nothing warms without an energy source, and nothing cools without losing energy to something colder.
- **Numbers:** Absolute zero is −273.15 °C (0 K); water freezes at 0 °C and boils at 100 °C at 1 atm; a 1 K rise in 1 kg of water needs 4,186 J.
- **Check:** Heat a known mass of water with a known energy input and measure the rise; the rise must match energy divided by mass times 4,186 J/kg·K within 5%, or the heat model fails.

**212. Specific heat of materials**
- **Rule:** Different materials need different amounts of energy to warm by one degree. Water needs far more than rock or metal, so seas warm and cool slowly while land swings fast. This difference shapes climates, shores, and daily temperature ranges.
- **Numbers:** Specific heat: water 4,186 J/kg·K; dry soil ~800; granite ~790; iron 449; sand ~830; air at constant pressure ~1,005 J/kg·K.
- **Check:** Warm equal masses of water, sand, and iron with equal energy and measure the rises; the ratios must match the specific heats within 10%, or the material heat model is wrong.

**213. Conduction through solids**
- **Rule:** Heat travels through a solid by molecules passing motion to their neighbours, from warm to cool. Metals conduct fast; rock and wood conduct slowly; still air is a poor conductor and insulates. A temperature difference drives the flow, and the flow stops when temperatures match.
- **Numbers:** Thermal conductivity: copper 401 W/m·K; iron 80; granite 2.5–3; wood 0.1–0.2; still air 0.026; a 1 m granite slab with a 10 K difference passes ~25–30 W/m².
- **Check:** Hold a granite slab with a steady 10 K difference across it and measure the heat flow; it must be 20–35 W/m², or the conduction rule is wrong.

**214. Convection in air and water**
- **Rule:** Warm fluid rises and cool fluid sinks, carrying heat with it. This is how the air and the sea move heat around the planet: warm air rises at the equator, cool air sinks elsewhere, and the same pattern stirs lakes and oceans. Convection moves far more heat than conduction in fluids.
- **Numbers:** A 1 K density difference in air drives vertical motion of centimetres to metres per second; ocean surface currents move 0.1–1 m/s; convective heat transfer in air is typically 5–25 W/m²·K.
- **Check:** Warm a water tank from below and track dye or temperature probes; warm water must rise and cool water must sink, with a full overturn in minutes, or the convection rule fails.

**215. Radiation: heat without touch**
- **Rule:** Every object gives off infrared radiation according to its temperature, and absorbs radiation from its surroundings. Hot things glow visibly; warm things glow in infrared. Radiation is how the planet loses heat to space and how the sun's energy arrives in the first place.
- **Numbers:** Stefan–Boltzmann constant 5.67×10⁻⁸ W/m²·K⁴; a black surface at 288 K (15 °C) radiates ~390 W/m²; Earth radiates ~240 W/m² to space on average.
- **Check:** Measure the infrared output of a black surface at two known temperatures; the ratio must follow the fourth power of absolute temperature within 5%, or the radiation rule is wrong.

**216. The greenhouse effect**
- **Rule:** Greenhouse gases such as water vapour and carbon dioxide let visible sunlight in but absorb some outgoing infrared, warming the surface above the temperature it would have with no atmosphere. More greenhouse gas means a warmer surface, all else equal; the effect is a property of the gases, not a setting.
- **Numbers:** Without greenhouse gases Earth's mean surface would be about −18 °C; with them it is about 15 °C, a warming of ~33 K; carbon dioxide is ~420 ppm in the present-day reference atmosphere.
- **Check:** Run the radiation model with greenhouse gases removed; the modelled mean surface temperature must fall by 25–40 K, or the greenhouse rule is wrong.

**217. Freezing and melting move heat**
- **Rule:** When water cools to 0 °C it freezes into ice, releasing heat; when ice warms to 0 °C it melts, absorbing the same heat. Ice floats because it is less dense than liquid water, so frozen surfaces insulate the water below. The temperature stays at 0 °C while the change of state is happening.
- **Numbers:** Latent heat of fusion 334 kJ/kg; ice density 917 kg/m³ against water at 1,000 kg/m³; melting 1 kg of ice needs as much energy as warming 1 kg of water by ~80 K.
- **Check:** Melt a known mass of ice with a known energy input and measure the time at 0 °C; the energy absorbed must match 334 kJ/kg within 10%, or the phase-change rule fails.

**218. Evaporation cools and condensation warms**
- **Rule:** Liquid water evaporates from any wet surface, taking heat with it and cooling the surface; water vapour condenses back to liquid on cool surfaces, releasing that heat. Evaporation needs energy; condensation returns it. This is how the world moves heat and water together.
- **Numbers:** Latent heat of vaporisation 2,260 kJ/kg at 100 °C (2,450 kJ/kg at 20 °C); evaporation of 1 mm of water per day carries ~28 W/m²; saturation vapour pressure doubles roughly every 10 K.
- **Check:** Evaporate a measured mass of water at 20 °C and measure the cooling; the heat removed must match 2,450 kJ/kg within 10%, or the evaporation rule is wrong.

**219. Temperature gradients and microclimates**
- **Rule:** Temperature is not the same everywhere: sunny slopes are warmer than shaded ones, low ground collects cold air at night, water edges stay milder than inland ground, and high ground is cooler than low ground. These local differences are real places with different conditions, not noise.
- **Numbers:** Temperature falls about 6.5 K per kilometre of height; a sunny south-facing slope can be 3–5 K warmer than a shaded slope at noon; night air in a hollow can be 2–5 K colder than the ridge above it.
- **Check:** Measure temperature at the same hour on a sunny slope, a shaded slope, a hollow, and a ridge; the differences must follow the stated ranges within 1 K, or the microclimate model fails.

**220. Thermal inertia and daily lag**
- **Rule:** The warmest time of day comes after noon, and the warmest time of year comes after the summer solstice, because ground and water store heat and release it slowly. Large water bodies lag the most; thin dry soil lags the least. The lag is a measurable property of the material, not a delay added by hand.
- **Numbers:** Daily temperature peak lags noon by 2–4 h over land and 4–6 h over water; the yearly peak lags the solstice by 3–6 weeks over land and 6–8 weeks over water.
- **Check:** Log air temperature hourly for 30 days and yearly for one full year; the daily peak must fall 2–6 h after noon and the yearly peak 3–8 weeks after the solstice, or the thermal-inertia model is wrong.

### 3.3 The chemistry set (elements)

**221. The element set is fixed**
- **Rule:** The world uses the real periodic table: the same elements as Earth, with the same atoms, the same charges, and the same bonding rules. No new element is invented, and no element behaves differently here than in real life. What changes is which elements are present, where, and in what amounts.
- **Numbers:** 94 naturally occurring elements; the crust is ~46% oxygen, ~28% silicon, ~8% aluminium, ~5% iron by mass; hydrogen and helium dominate the sun, not the ground.
- **Check:** List every element present in the world model and its atomic number; the list must be a subset of the real periodic table with correct atomic numbers, and any element used in a reaction must appear in the list, or the chemistry set is wrong.

**222. Hydrogen and oxygen**
- **Rule:** Hydrogen is the lightest element and the most abundant in the universe; oxygen is the reactive partner that makes water and rust. Hydrogen burns in oxygen to make water, releasing energy; oxygen alone does not burn, but it lets other things burn. Both are gases at ordinary temperatures.
- **Numbers:** Hydrogen atomic mass 1.008, oxygen 15.999; H₂ burns in O₂ to give 2H₂O, releasing 286 kJ per mole of H₂; air is ~21% oxygen by volume.
- **Check:** Burn a measured amount of hydrogen in oxygen in a closed vessel and measure the water formed; the mass must match the reaction stoichiometry within 5%, or the hydrogen–oxygen rule fails.

**223. Carbon, the backbone**
- **Rule:** Carbon bonds to itself and to hydrogen, oxygen, and nitrogen in chains and rings, which is why it can build the huge variety of compounds that later life uses. Carbon dioxide is a gas; diamond and graphite are pure carbon solids; charcoal is mostly carbon. Carbon is neither created nor destroyed in the world, only rearranged.
- **Numbers:** Carbon atomic mass 12.011; C–C bond energy ~348 kJ/mol; CO₂ is ~420 ppm in air; diamond density 3,510 kg/m³, graphite 2,260 kg/m³.
- **Check:** Burn a known mass of charcoal in excess oxygen and measure the CO₂ produced; the carbon mass must balance within 5%, or the carbon rule is wrong.

**224. Nitrogen, the inert majority**
- **Rule:** Nitrogen gas makes up most of the air but reacts with almost nothing at ordinary temperatures, because its triple bond is very strong. It becomes chemically useful only when lightning, heat, or later living processes break that bond and fix it into compounds such as ammonia and nitrate.
- **Numbers:** Air is ~78% nitrogen by volume; N≡N bond energy 945 kJ/mol; lightning fixes roughly 5–10 million tonnes of nitrogen per year on Earth; ammonia NH₃ and nitrate NO₃⁻ are the useful forms.
- **Check:** Measure the nitrogen fraction of the air and the rate of nitrogen fixation during a simulated storm; air nitrogen must be 77–79% and fixation must be zero without lightning or heat above 1,500 K, or the nitrogen rule fails.

**225. Silicon, the rock builder**
- **Rule:** Silicon bonds with oxygen to make silica, the backbone of most rocks and sand. Quartz is silicon dioxide; clays are layered silicates; glass is melted silica. Silicon chemistry is slow and stable at ordinary temperatures, which is why rocks last.
- **Numbers:** Silicon atomic mass 28.085; quartz SiO₂ density 2,650 kg/m³; silica melts at 1,710 °C; silicon is ~28% of the crust by mass.
- **Check:** Analyse a sample of sand and granite; both must be mostly silicon and oxygen by mass, with quartz identifiable as SiO₂, or the silicon rule is wrong.

**226. Iron, the working metal**
- **Rule:** Iron is strong, magnetic, and common, and it rusts when iron, oxygen, and water meet. Iron can be smelted from its ores with heat and carbon, and it alloys with carbon to make steel. Iron's willingness to give up and take back electrons makes it useful in chemistry as well as in tools.
- **Numbers:** Iron atomic mass 55.845; density 7,874 kg/m³; melting point 1,538 °C; rust is hydrated iron(III) oxide, roughly Fe₂O₃·nH₂O; steel is iron with 0.05–2% carbon.
- **Check:** Leave iron in water and air for 30 days and weigh the rust formed; rust mass must exceed the iron lost by the oxygen and water taken up, matching the oxide stoichiometry within 10%, or the iron rule fails.

**227. Copper, tin, and bronze**
- **Rule:** Copper is soft, reddish, and easy to work; tin is soft and low-melting. Heated together, they form bronze, an alloy harder than either metal alone. Bronze is not a recipe placed in the world; it is what copper, tin, and heat do under fixed chemistry, and it can be discovered by anyone who tries the combination.
- **Numbers:** Copper melts at 1,085 °C, tin at 232 °C; bronze is typically ~88% copper and ~12% tin; bronze is roughly twice as hard as pure copper on a simple hardness test.
- **Check:** Heat copper and tin together in the stated ratio and test the product; it must be a single alloy phase harder than copper alone, and the same result must occur without any label or instruction, or the alloy rule is wrong.

**228. Sodium, potassium, and salts**
- **Rule:** Sodium and potassium are soft metals that react violently with water, but their compounds are stable and common: table salt is sodium chloride, and potassium salts sit in soils and rocks. Salts dissolve in water into charged ions, which is why salty water conducts electricity and why salt matters to living things later.
- **Numbers:** Sodium atomic mass 22.990, potassium 39.098; NaCl melts at 801 °C; seawater is ~3.5% salt by mass, mostly NaCl; pure water conducts almost nothing, seawater conducts ~5 S/m.
- **Check:** Dissolve a known mass of salt in a known volume of water and measure conductivity and mass; conductivity must rise to the seawater range and the dissolved mass must balance within 2%, or the salt rule fails.

**229. Calcium and phosphorus, the builders**
- **Rule:** Calcium and phosphorus are the mineral builders: calcium carbonate makes limestone, shells, and chalk; calcium phosphate makes bone and teeth later; phosphorus is scarce and limits growth wherever it runs short. Both cycle slowly through rock, water, and soil.
- **Numbers:** Calcium atomic mass 40.078, phosphorus 30.974; limestone CaCO₃ density ~2,710 kg/m³; apatite, the phosphate mineral, is Ca₅(PO₄)₃(OH,F,Cl); crustal phosphorus is ~0.1% by mass.
- **Check:** Analyse limestone and a phosphate rock sample; limestone must be mostly CaCO₃ and the phosphate rock must contain measurable phosphate, with calcium and phosphorus present in the stated ratios within 10%, or the mineral rule is wrong.

**230. Trace elements and limits**
- **Rule:** Many elements are needed only in tiny amounts but are still required: magnesium sits at the centre of the green pigment that later captures sunlight, zinc and copper catalyse reactions, iodine and selenium matter in small doses. Too much of a trace element is poison; too little starves the chemistry that needs it.
- **Numbers:** Magnesium is ~2% of the crust; zinc ~70 ppm; copper ~60 ppm; iodine ~0.5 ppm in crust; a trace element is typically needed at parts-per-million levels and toxic at parts-per-thousand.
- **Check:** Measure the trace-element concentrations in soil and water samples; they must fall within an order of magnitude of the stated crustal values, and a reaction that needs a trace element must stop without it, or the trace rule fails.

### 3.4 Water chemistry

**231. Water the molecule**
- **Rule:** A water molecule is two hydrogen atoms joined to one oxygen atom at an angle, which makes one side slightly positive and the other slightly negative. That polarity lets water dissolve salts, stick to itself, and carry heat. Water is the same molecule everywhere in the world.
- **Numbers:** H₂O molar mass 18.015 g/mol; bond angle 104.5°; dipole moment 1.85 debye; liquid density 1,000 kg/m³ at 4 °C, maximum density at 4 °C.
- **Check:** Measure the density of water from 0 to 20 °C; it must peak at 4 °C and fall on both sides, and the freezing point must be 0 °C at 1 atm, or the water model is wrong.

**232. Water as a solvent**
- **Rule:** Water dissolves salts, sugars, gases, and many other compounds by surrounding their charged or polar parts. Non-polar oils do not dissolve. Dissolved substances change the water's properties: salt water freezes lower, boils higher, and conducts electricity.
- **Numbers:** NaCl solubility ~360 g per litre at 20 °C; seawater freezes at about −1.9 °C; pure water conductivity ~0.05 µS/cm, seawater ~50,000 µS/cm.
- **Check:** Dissolve salt in water until no more dissolves and weigh it; solubility must be 340–380 g/L at 20 °C, and the freezing point of the saturated solution must be below −15 °C, or the solvent rule fails.

**233. Acidity and pH**
- **Rule:** Water can split into hydrogen ions and hydroxide ions, and the balance between them sets pH. Acids add hydrogen ions and lower pH; bases remove them and raise it. Most natural water sits near neutral, and small pH shifts change which minerals dissolve and which reactions run.
- **Numbers:** pH is −log₁₀ of hydrogen-ion concentration in mol/L; neutral is pH 7 at 25 °C; rainwater is ~pH 5.6 from dissolved CO₂; seawater is ~pH 8.1.
- **Check:** Measure pH of rainwater, river water, and seawater samples; they must read 5.0–6.0, 6.5–8.5, and 7.8–8.3 respectively, or the pH model is wrong.

**234. Dissolved gases**
- **Rule:** Air dissolves in water in proportion to its pressure above the water, and cold water holds more gas than warm water. Oxygen dissolved in water is what later water life breathes; carbon dioxide dissolved in water forms carbonic acid. Gas leaves water when it warms or when the pressure drops.
- **Numbers:** At 20 °C and 1 atm, water holds ~9 mg/L of oxygen and ~1.5 g/L of CO₂ at equilibrium with air; oxygen solubility falls to ~7 mg/L at 30 °C; Henry's law sets the proportionality.
- **Check:** Measure dissolved oxygen in cold and warm water at the same air pressure; cold water must hold at least 20% more oxygen, and both must match Henry's law within 15%, or the gas rule fails.

**235. Carbon dioxide in water**
- **Rule:** Carbon dioxide dissolves in water and forms carbonic acid, which lowers pH and can dissolve limestone. The same reaction runs backwards when CO₂ leaves the water, depositing carbonate again. This is the link between the air, the water, and the rocks.
- **Numbers:** CO₂ + H₂O ⇌ H₂CO₃; at 400 ppm CO₂ in air, rainwater equilibrates near pH 5.6; limestone dissolves measurably below pH 6 and deposits above pH 8.
- **Check:** Bubble CO₂ through water and measure the pH fall, then leave limestone in that water for 7 days; pH must fall below 6 and the limestone must lose measurable mass, or the carbonic-acid rule fails.

**236. Hard and soft water**
- **Rule:** Water that has passed through limestone picks up calcium and magnesium and becomes hard; water from granite or rain stays soft. Hard water leaves scale when heated and needs more soap to lather; soft water does neither. Hardness is a property of the rock the water crossed, not a setting.
- **Numbers:** Hardness is measured as mg/L of CaCO₃ equivalent; soft is below 60, hard is above 120, very hard is above 180; heating hard water deposits CaCO₃ scale.
- **Check:** Measure hardness of water from a limestone catchment and a granite catchment; limestone water must be at least twice as hard, and boiling it must leave visible scale, or the hardness rule is wrong.

**237. Salinity and the sea**
- **Rule:** The sea is salty because rivers carry dissolved salts from rocks into it and evaporation leaves the salts behind. Salt water is denser than fresh water, so fresh river water floats over the sea where they meet. Salt concentration changes freezing, boiling, density, and which chemistry can happen.
- **Numbers:** Seawater is ~35 g of salt per kg of water; density ~1,025 kg/m³; freezing point −1.9 °C; sodium ~10.8 g/kg and chloride ~19.4 g/kg dominate the salt.
- **Check:** Measure salinity, density, and freezing point of a sea sample; they must be 33–37 g/kg, 1,020–1,030 kg/m³, and −1.5 to −2.5 °C, or the seawater model is wrong.

**238. Water movement: currents and mixing**
- **Rule:** Water moves because wind drags the surface, because temperature and salt make some water heavier than other water, and because rivers flow downhill. Heavy water sinks, light water rises, and the result is currents that carry heat, salts, and nutrients. Still water stratifies; stirred water mixes.
- **Numbers:** Wind-driven surface currents move at ~1–3% of wind speed; a 1 g/kg salinity difference changes density by ~0.8 kg/m³; river flow follows gravity at speeds set by slope and depth, typically 0.1–2 m/s.
- **Check:** Track a dye patch in a wind-blown tank and in a tank with a salt gradient; the dye must move downwind and the salty layer must sink below the fresh layer, or the water-movement rule fails.

**239. Ice, snow, and frozen water**
- **Rule:** Ice forms on the surface of still water because it is less dense than liquid water, and the ice layer insulates the water below. Snow is ice crystals that fall from cold air. Frozen ground locks water in place until it thaws, and freeze–thaw cycles crack rock.
- **Numbers:** Ice density 917 kg/m³; snow density 50–300 kg/m³ when fresh; freezing releases 334 kJ/kg; permafrost is ground below 0 °C for at least two years.
- **Check:** Freeze a tank of water from the top and measure temperatures below the ice; water under the ice must stay near 0–4 °C while the air above falls below −5 °C, or the ice-insulation rule fails.

**240. Water quality as a measured state**
- **Rule:** Every body of water has a measurable state: temperature, pH, salinity, dissolved oxygen, and the concentrations of the main dissolved ions. That state is set by the rocks, the air, the weather, and the flows that feed it — never by a label. Two waters with the same measured state behave the same.
- **Numbers:** Report temperature to 0.1 K, pH to 0.1, salinity to 0.1 g/kg, dissolved oxygen to 0.1 mg/L; a complete water record carries all four plus calcium, magnesium, and bicarbonate concentrations.
- **Check:** Sample the same pond on 5 days and compare the records; values must be reproducible within the stated precision, and a change in any one value must be traceable to a change in inflow, weather, or rock contact, or the water-state model fails.

### 3.5 Rocks and ores

**241. Rock from cooling melt**
- **Rule:** Molten rock cools into igneous rock: slow cooling underground makes large crystals, as in granite; fast cooling at the surface makes small crystals or glass, as in basalt and obsidian. The chemistry of the melt sets which minerals form; the cooling rate sets their size.
- **Numbers:** Granite is ~70% silica with quartz, feldspar, and mica; basalt is ~50% silica; granite cools over thousands of years underground, basalt in days to weeks at the surface; magma is 700–1,300 °C.
- **Check:** Identify granite and basalt samples by mineral content and crystal size; granite must show crystals larger than 1 mm and basalt smaller than 1 mm, with the stated silica ranges, or the igneous rule is wrong.

**242. Sediment and sedimentary rock**
- **Rule:** Wind and water wear rock into grains, carry them downhill, and drop them where the flow slows. Buried grains are pressed and cemented into sandstone, shale, or limestone. Layers record the order they were laid down: lower layers are older, unless the ground has been folded or overturned.
- **Numbers:** Sand grains are 0.06–2 mm; silt is 0.004–0.06 mm; clay is below 0.004 mm; burial to lithify sand takes thousands to millions of years under 100 m or more of overburden.
- **Check:** Sieve a sediment sample and measure the grain-size distribution; the named rock type must match the dominant grain size, and a layered outcrop must show lower layers older than upper ones, or the sediment rule fails.

**243. Metamorphic rock from heat and pressure**
- **Rule:** Buried rock that is heated and squeezed without melting changes into metamorphic rock: shale becomes slate, then schist; limestone becomes marble; sandstone becomes quartzite. The minerals rearrange into new forms that record the temperature and pressure they endured.
- **Numbers:** Slate forms at ~200–300 °C, schist at ~400–600 °C, marble from limestone above ~300 °C; pressures reach hundreds of megapascals at depths of 10–30 km.
- **Check:** Identify slate, schist, and marble samples by texture and mineral content; each must match its parent rock's chemistry with a foliated or recrystallised texture, or the metamorphic rule is wrong.

**244. Weathering: rock breaks down**
- **Rule:** Rock breaks down where it meets air and water: water freezes in cracks and wedges them open, acids dissolve limestone, and oxygen rusts iron-bearing minerals. Weathering makes soil and sand and frees the elements locked in rock. It is slow, but it never stops.
- **Numbers:** Freeze–thaw widens a crack by ~9% each time water in it freezes; limestone dissolves at ~0.01–0.1 mm per year in rainwater; granite weathers at ~0.001–0.01 mm per year.
- **Check:** Leave limestone and granite blocks in rainwater for 90 days and weigh them; limestone must lose measurably more mass than granite, and a water-filled crack must widen after repeated freezing, or the weathering rule fails.

**245. Erosion and transport**
- **Rule:** Moving water, wind, and ice carry weathered grains away, sorting them by size as they go: fast flows carry boulders, slow flows carry only silt and clay. Where the flow slows, grains settle in order of size, heaviest first. Erosion moves rock; it does not destroy it.
- **Numbers:** A river at 1 m/s moves sand; at 2 m/s it moves pebbles; wind at 10 m/s moves sand by saltation; a grain settles at a speed set by its size and density, roughly 0.01 m/s for fine sand.
- **Check:** Run water at two speeds over a mixed bed and measure what moves; the faster flow must move larger grains, and a settling column must show coarse grains landing before fine ones, or the transport rule is wrong.

**246. Ores: where metals concentrate**
- **Rule:** Metals are spread thinly through most rock, but hot water, cooling melts, and weathering can concentrate them into ores rich enough to be worth gathering. Copper, tin, iron, and gold each concentrate by different processes, so each ore is found in different rocks and places. An ore is a concentration, not a placement.
- **Numbers:** Crustal copper is ~60 ppm; a copper ore is ~0.5–2% copper; iron ore is 30–65% iron; gold ore is 1–10 g per tonne; tin ore is ~0.2–1% tin.
- **Check:** Assay rock samples from different settings; at least one sample must exceed the ore threshold for its metal while ordinary rock stays near crustal values, or the ore rule is wrong.

**247. Iron ore and smelting**
- **Rule:** Iron ore is mostly iron oxide — hematite or magnetite — and smelting removes the oxygen with carbon and heat, leaving metal iron. The furnace must be hot enough and the air supply controlled, or the ore stays oxide. Charcoal is the carbon source at this stage of the world.
- **Numbers:** Hematite Fe₂O₃ is ~70% iron; magnetite Fe₃O₄ is ~72% iron; smelting needs ~1,200–1,500 °C; roughly 1 kg of charcoal reduces about 1 kg of ore to ~0.5 kg of iron.
- **Check:** Smelt a known mass of hematite with charcoal at the stated temperature and weigh the metal produced; the iron yield must be 50–70% of the ore's iron content, or the smelting rule fails.

**248. Copper and tin ores**
- **Rule:** Copper ore is often a sulphide or carbonate that must be roasted and smelted; tin ore is cassiterite, a heavy oxide found in stream gravels and veins. Copper melts at a temperature a good charcoal fire can reach; tin melts far lower. Both metals are soft alone and harder together as bronze.
- **Numbers:** Cassiterite SnO₂ is ~78% tin; malachite Cu₂CO₃(OH)₂ is ~57% copper; copper melts at 1,085 °C, tin at 232 °C; a charcoal fire with forced air reaches 1,100–1,300 °C.
- **Check:** Smelt cassiterite and malachite samples and weigh the metal; each must yield metal at 40–70% of the ore's metal content, and the copper must melt in a forced-air charcoal fire, or the ore rule fails.

**249. Stone for tools and building**
- **Rule:** Not all stone is equal: flint and obsidian break with a sharp conchoidal edge and can cut; granite is hard and heavy and suits grinding and building; sandstone is soft and easy to shape but wears fast. The right stone for a job is the one whose fracture and hardness fit it, discovered by trying.
- **Numbers:** Flint hardness ~7 on the Mohs scale; granite ~6–7; sandstone ~6 but weakly cemented; obsidian fractures with an edge sharper than 1 micrometre; a flint edge cuts hide and wood, granite does not.
- **Check:** Strike flint, granite, and sandstone and test the edges on wood; flint must produce a cutting edge, granite a blunt hammer face, and sandstone must wear visibly after 100 strokes, or the stone rule is wrong.

**250. The rock record is honest**
- **Rule:** Every rock in the world has a history that can be read from it: its minerals, its grain size, its layers, and its chemistry record how it formed. Nothing is labelled by the owner; the record is in the rock itself, and two rocks with the same measured properties have the same history.
- **Numbers:** A complete rock record carries mineral percentages, grain size in millimetres, density to 10 kg/m³, and the concentrations of silicon, iron, calcium, and aluminium to 1% by mass.
- **Check:** Take two samples from the same outcrop and one from a different rock type; the same-outcrop pair must agree within the stated tolerances and differ from the other type, or the rock record is wrong.

### 3.6 Fire

**251. What fire is**
- **Rule:** Fire is a rapid chemical reaction between a fuel and oxygen that releases heat and light. It is not a substance and not a thing placed in the world; it is what happens when fuel, oxygen, and enough heat meet. Remove any one of the three and the fire stops.
- **Numbers:** Wood burns at roughly 600–900 °C in open air; a candle flame is ~1,000 °C at its hottest point; fire needs at least ~16% oxygen in the air to sustain ordinary burning.
- **Check:** Light wood in air, then cover it and starve it of oxygen; the flame must die within seconds of oxygen falling below the threshold, and relight only with fuel, oxygen, and heat together, or the fire rule fails.

**252. Ignition: heat to start it**
- **Rule:** A fuel does not burn until part of it is heated to its ignition temperature, where it releases flammable gases that catch fire. Friction, a spark, a hot ember, or focused sunlight can supply that heat. Once burning, the fire heats the next fuel itself and sustains the chain.
- **Numbers:** Dry wood ignites at ~300 °C; paper at ~233 °C; charcoal at ~350 °C; a friction fire must raise a small point of wood above 300 °C before any flame appears.
- **Check:** Heat wood samples to 250 °C and 350 °C in air; the 250 °C sample must not ignite and the 350 °C sample must, within a minute, or the ignition rule is wrong.

**253. Fuel: what burns**
- **Rule:** Anything with carbon and hydrogen in it can burn if it is dry enough: wood, grass, leaves, charcoal, fat, oil. Wet fuel does not burn until its water is driven off, which costs heat. Different fuels burn at different rates and temperatures, and charcoal burns hotter and cleaner than raw wood.
- **Numbers:** Dry wood holds ~15–18 MJ/kg; charcoal ~28–33 MJ/kg; dry grass ~15 MJ/kg; wood above ~30% moisture will not sustain a flame without drying first.
- **Check:** Burn equal masses of dry wood, wet wood, and charcoal and measure heat released; charcoal must release roughly twice the heat of wood, and wet wood must release less and burn slower, or the fuel rule fails.

**254. Air supply and the fire triangle**
- **Rule:** A fire's size is set by its air supply as much as by its fuel: too little air smothers it, too much air cools it and blows it out. A sheltered fire with a steady draught burns hottest. Wind feeds a fire until it is strong enough to scatter the fuel and break the flame.
- **Numbers:** Complete burning of wood needs about 6 kg of air per kg of wood; a fire in still air burns at roughly half the rate of the same fire with a gentle draught; wind above ~10 m/s can blow out a small open flame.
- **Check:** Burn the same fuel in still air and in a gentle draught and measure the burn rate; the draught-fed fire must burn at least 50% faster, or the air-supply rule is wrong.

**255. Flames, smoke, and incomplete burning**
- **Rule:** A flame is hot gas giving off light; smoke is unburned fuel, soot, and ash carried up by hot air. A fire starved of air makes more smoke and less heat, because the fuel cannot finish burning. Complete burning leaves mainly carbon dioxide and water; incomplete burning leaves carbon monoxide and soot.
- **Numbers:** Complete burning of carbon gives CO₂ and 394 kJ/mol; incomplete burning gives CO and 111 kJ/mol; a smoky fire can release 10–100 times more soot than a clean-burning one.
- **Check:** Burn wood with restricted air and with free air and measure smoke and CO; the restricted fire must produce at least 5 times more CO and visible smoke, or the incomplete-burning rule fails.

**256. Heat from fire**
- **Rule:** A fire warms by radiation, by hot air rising, and by conduction into what it touches. Radiant heat falls with distance and is blocked by solid objects; hot air rises and warms what is above. A fire warms a person nearby and cooks food placed in or over it, and the same heat can dry wet fuel.
- **Numbers:** A 1 kW campfire radiates roughly 300 W; radiant heat at 1 m is ~25 W/m²; a person needs ~100 W of heat to feel warm in cold air; water boils at 100 °C over a fire that reaches 600 °C.
- **Check:** Measure temperature at 0.5, 1, and 2 m from a steady fire; temperatures must fall with distance roughly as the inverse square, and water in a pot over the fire must boil, or the fire-heat rule is wrong.

**257. Fire spreads**
- **Rule:** Fire spreads when heat from a burning patch dries and ignites the fuel next to it. Dry grass and leaves carry fire fast; green wood and bare ground stop it. Wind pushes the flame forward and throws embers ahead, so a fire runs faster downwind than upwind.
- **Numbers:** Grass fire spreads at 0.1–1 m/s in still air and faster with wind; a firebreak of bare ground must be at least 2–3 times the flame height to stop a grass fire; embers can travel 10–100 m in strong wind.
- **Check:** Light a measured strip of dry grass in still air and in a 3 m/s wind and measure the spread rate; the downwind rate must exceed the still-air rate by at least 50%, or the spread rule fails.

**258. Charcoal: fire made into fuel**
- **Rule:** Wood heated with little air does not burn away; it turns into charcoal, which is mostly carbon with the water and volatile gases driven off. Charcoal burns hotter and with less smoke than wood, and it is the fuel that makes smelting possible. Making charcoal costs wood and time, and the yield is a fixed fraction.
- **Numbers:** Charcoal is made at 300–500 °C with restricted air; 1 kg of dry wood yields ~0.2–0.3 kg of charcoal; charcoal holds ~28–33 MJ/kg against wood's ~15–18 MJ/kg.
- **Check:** Heat a known mass of wood with restricted air and weigh the charcoal; the yield must be 15–35% of the dry wood mass, and the charcoal must burn hotter than the wood it came from, or the charcoal rule is wrong.

**259. Fire's dangers: burns and smoke**
- **Rule:** Fire harms living things by heat and by smoke: skin burns above about 44 °C with prolonged contact, and smoke carries carbon monoxide that blocks oxygen in the blood. A fire that is useful at a distance is deadly up close, and the same fire that cooks food can kill the cook who falls into it.
- **Numbers:** Skin burns in seconds at 60 °C and in minutes at 50 °C; carbon monoxide at 400 ppm causes headache in hours, at 1,600 ppm it is lethal in hours; a campfire's hot zone extends ~0.5 m from the flame.
- **Check:** Measure temperature and CO at 0.5 and 2 m from a fire; temperature must fall below 50 °C and CO below 50 ppm at 2 m in open air, or the fire-danger model is wrong.

**260. Fire leaves a record**
- **Rule:** Fire leaves charcoal, ash, and heat-cracked rock that persist after the flame is gone. Ash is alkaline and changes the soil; charcoal lasts for centuries in the ground. A burned patch can be read long after the fire: what burned, how hot it got, and when.
- **Numbers:** Wood ash is ~10–25% calcium compounds by mass and has a pH of 10–12 in water; charcoal is ~80–90% carbon; a hot fire cracks surface rock to a depth of 1–5 cm.
- **Check:** Examine a burned patch 7 days after a fire; charcoal and ash must be present, the ash-water pH must be above 9, and the underlying rock must show heat cracking, or the fire-record rule fails.

### 3.7 Cycles (carbon, nitrogen, oxygen, phosphorus)

**261. The carbon cycle: air, water, rock, life**
- **Rule:** Carbon moves between the air as CO₂, the water as dissolved CO₂ and bicarbonate, the rocks as carbonate, and living things as organic carbon. Burning and decay return carbon to the air; dissolving in water and forming limestone lock it away. The total carbon is conserved; only its location changes.
- **Numbers:** Air holds ~850 Gt of carbon as CO₂; the ocean holds ~38,000 Gt, mostly as bicarbonate; the crust holds far more as carbonate rock; photosynthesis and respiration each move ~120 Gt of carbon per year on Earth.
- **Check:** Run a 30-day carbon audit across air, water, and rock; total carbon must balance within 1% while the air–water exchange moves measurable amounts both ways, or the carbon-cycle rule fails.

**262. The nitrogen cycle: fixing, using, returning**
- **Rule:** Nitrogen gas is fixed into ammonia and nitrate by lightning and later by living processes, taken up into organic matter, and returned to the air by decay and denitrification. Without fixation, nitrogen stays locked in the air and unavailable; with it, nitrogen becomes the nutrient that most often limits growth.
- **Numbers:** Lightning fixes ~5–10 Mt of nitrogen per year on Earth; the air holds ~4,000,000 Gt of nitrogen; soil nitrate is typically 1–50 mg/kg; denitrification returns N₂ to the air in waterlogged soil.
- **Check:** Measure nitrate in soil before and after a storm season; nitrate must rise after lightning events and fall where waterlogging sets in, or the nitrogen-cycle rule is wrong.

**263. The oxygen cycle: breathing and burning**
- **Rule:** Oxygen is released when carbon dioxide is split by sunlight-driven chemistry in living things, and consumed again by breathing, decay, and burning. The air's oxygen stays near 21% because release and consumption balance over time; a large imbalance would shift it measurably.
- **Numbers:** Air is 20.95% oxygen by volume; the air holds ~1,200,000 Gt of oxygen; burning 1 kg of carbon consumes ~2.7 kg of oxygen; the oxygen residence time in the air is thousands of years.
- **Check:** Measure air oxygen over 30 days in a closed test volume with burning and photosynthesis; oxygen must fall when burning dominates and rise when photosynthesis dominates, tracking the carbon exchanged, or the oxygen-cycle rule fails.

**264. The phosphorus cycle: slow rock to sea**
- **Rule:** Phosphorus has no gas phase: it weathers out of rock into soil and water, is taken up by living things, and is carried by rivers to the sea, where it settles into sediment and returns to rock over geological time. Because it moves slowly and has no shortcut through the air, phosphorus is often the scarcest nutrient.
- **Numbers:** Crustal phosphorus is ~0.1% by mass; river water carries ~0.01–0.1 mg/L of phosphate; seawater holds ~0.07 mg/L; the phosphorus residence time in soil is hundreds to thousands of years.
- **Check:** Measure phosphate in rock, soil, river, and sea samples along one catchment; concentrations must fall from rock to soil to river, and the river must carry phosphate to the sea, or the phosphorus-cycle rule is wrong.

**265. The water cycle: evaporation, rain, return**
- **Rule:** Sunlight evaporates water from seas, lakes, and land; the vapour rises, cools, and condenses into clouds; rain falls, runs downhill in rivers, soaks into the ground, and returns to the sea. The same water is used again and again; the cycle is driven by solar heat and gravity.
- **Numbers:** Global evaporation is ~500,000 km³ per year on Earth; about 80% falls back on the sea; a 1 mm rainfall is 1 litre per square metre; rivers return ~40,000 km³ per year to the sea.
- **Check:** Measure evaporation, rainfall, and river flow in one catchment over 30 days; evaporation plus runoff must balance rainfall plus inflow within 10%, or the water-cycle rule fails.

**266. Rock weathering in the cycles**
- **Rule:** Weathering is the slow leak that feeds the cycles: rain and acids dissolve rock, releasing calcium, magnesium, potassium, and phosphorus into soil and water. Without weathering, the cycles would run down as nutrients were locked into sediment; with it, fresh rock keeps supplying them.
- **Numbers:** Chemical weathering releases roughly 0.01–0.1 mm of rock per year in temperate climates; a litre of rainwater in equilibrium with CO₂ dissolves ~50 mg of limestone; silicate weathering consumes CO₂.
- **Check:** Pass rainwater over limestone and granite for 30 days and measure dissolved calcium; limestone water must carry at least 10 times more calcium, and the CO₂ in the water must fall as silicate dissolves, or the weathering-cycle rule is wrong.

**267. Sediment burial and return**
- **Rule:** Rivers carry sediment to the sea, where it settles, buries, and over long times becomes rock again, locking carbon, phosphorus, and other elements away. Uplift and erosion later expose that rock and weathering releases the elements once more. The loop is slow — thousands to millions of years — but it closes.
- **Numbers:** Rivers carry ~20 Gt of sediment to the sea per year on Earth; burial locks ~0.1–0.2 Gt of organic carbon per year; uplift exposes rock at ~0.01–1 mm per year in active regions.
- **Check:** Measure sediment load in a river and the sedimentation rate where it meets still water; the load must settle in still water and the deposited layer must grow measurably over 30 days, or the burial rule fails.

**268. Cycle timescales differ**
- **Rule:** The cycles run on very different clocks: water turns over in days to years, carbon in years to centuries, nitrogen in years to decades, and phosphorus in centuries to millennia. A fast cycle can be watched directly; a slow cycle is measured by its rates, not by watching it finish.
- **Numbers:** Atmospheric water residence time is ~9 days; carbon in the air turns over in ~5 years; nitrogen in soil in ~10–100 years; phosphorus in the ocean in ~10,000–100,000 years.
- **Check:** Tag a parcel of water and a parcel of carbon and track them; the water must leave the air within weeks while the carbon remains traceable in the air–water exchange for months, or the timescale rule is wrong.

**269. Cycles have limits and bottlenecks**
- **Rule:** Each cycle has a limiting step that sets its pace: phosphorus supply limits growth where rock is poor, nitrogen fixation limits it where lightning is rare, and water limits everything where rain is scarce. Adding more of a non-limiting nutrient changes nothing; adding the limiting one changes everything.
- **Numbers:** The limiting nutrient is the one present at the lowest ratio to demand; doubling a non-limiting nutrient changes growth by less than 5%, while doubling the limiting nutrient can double it; Liebig's law of the minimum states the rule.
- **Check:** Add nitrogen to one plot, phosphorus to another, and neither to a third, and measure growth; only the plot given the truly limiting nutrient must grow measurably more, or the limiting-factor rule fails.

**270. Cycles are measured, not assumed**
- **Rule:** Every cycle is checked by a mass balance: what enters a reservoir, what leaves it, and what stays. A cycle that cannot be balanced is not understood. The balances are kept in the run log, with the numbers, so any later change can be traced to a real flow.
- **Numbers:** Each cycle audit reports inputs, outputs, and storage change in the same units (kg or mol per day) with an error term; a balance that closes within 5% passes, one that closes worse than 10% is investigated.
- **Check:** Produce a 30-day audit for carbon, nitrogen, and water; all three must close within 5%, or the cycle bookkeeping is wrong.

### 3.8 Energy flows

**271. Energy in, energy out**
- **Rule:** The world takes in solar energy and gives out infrared energy to space. In between, energy is stored briefly as heat, as moving air and water, and as chemical bonds. The inflow and the outflow must balance over time, or the world warms or cools.
- **Numbers:** Inflow ~340 W/m² averaged over the planet; outflow ~240 W/m² as infrared plus ~100 W/m² reflected; a sustained imbalance of 1 W/m² warms the surface by roughly 0.5–1 K over decades.
- **Check:** Measure incoming solar and outgoing infrared over 30 days; the difference must match the measured change in stored heat within 10%, or the energy-flow rule fails.

**272. Heat flows downhill in temperature**
- **Rule:** Heat always flows from warmer to cooler: from sunlit ground to shaded ground, from warm water to cold water, from a fire to the air around it. The flow rate grows with the temperature difference and stops when the difference is gone. No flow ever runs uphill without work.
- **Numbers:** Conductive flow is proportional to the temperature gradient; a 10 K difference across 1 m of granite drives ~25 W/m²; convective flow in air is 5–25 W/m² per kelvin of difference.
- **Check:** Place a warm block against a cool block and measure the heat flow and the temperatures; flow must go warm-to-cool and fall to zero as the temperatures meet, or the heat-flow rule is wrong.

**273. Kinetic energy: motion carries energy**
- **Rule:** Moving air, water, and solid objects carry kinetic energy set by their mass and speed. Wind can push, water can wear rock, and a falling stone can break what it hits. When motion stops, its energy becomes heat or is transferred to what stopped it.
- **Numbers:** Kinetic energy is ½mv²; 1 kg of air at 10 m/s carries 50 J; 1 kg of water at 1 m/s carries 0.5 J; a 1 kg stone falling 10 m gains ~98 J.
- **Check:** Drop a 1 kg mass from 1 m and 10 m onto a target and measure the impact; the 10 m impact must deliver roughly 10 times the energy of the 1 m impact, or the kinetic-energy rule fails.

**274. Potential energy: height stores energy**
- **Rule:** Water held high, a stone on a cliff, and a stretched branch all store potential energy that is released when they fall, flow, or snap back. Rivers run downhill because gravity converts height into motion; a dammed lake stores the same energy until it is released.
- **Numbers:** Potential energy is mgh; 1 kg of water 10 m up stores ~98 J; a river falling 100 m over its course converts that height into flow energy, minus friction losses.
- **Check:** Release a known mass of water from a known height through a wheel or turbine and measure the work done; it must be 50–90% of mgh, the rest lost to friction, or the potential-energy rule is wrong.

**275. Chemical energy: bonds store energy**
- **Rule:** Chemical bonds store energy: breaking some bonds and forming others releases or absorbs it. Burning wood releases the energy stored in its bonds; forming limestone from dissolved ions stores a little. The energy in a fuel is the difference between the bonds broken and the bonds formed.
- **Numbers:** Wood holds ~15–18 MJ/kg; coal ~24–30 MJ/kg; fat ~37 MJ/kg; forming a mole of CaCO₃ from ions releases ~1,207 kJ/mol in lattice energy terms.
- **Check:** Burn a known mass of wood and measure the heat; the heat must match 15–18 MJ/kg within 15%, and the ash mass must be far smaller than the wood mass, or the chemical-energy rule fails.

**276. Energy losses: friction and waste heat**
- **Rule:** Every real process wastes some energy as heat: friction warms rubbing surfaces, turbulence warms moving fluids, and no conversion is perfectly efficient. The wasted energy is not lost from the world — it becomes heat — but it is no longer available to do the same work.
- **Numbers:** Friction converts motion to heat at a rate set by force times speed; a sliding block loses all its kinetic energy to heat over its stopping distance; typical mechanical efficiencies are 50–90%, the rest becoming heat.
- **Check:** Slide a block across a surface and measure the temperature rise of the block and surface; the heat gained must match the kinetic energy lost within 20%, or the friction-loss rule is wrong.

**277. Energy storage: heat, height, chemistry**
- **Rule:** The world stores energy in three main ways: as heat in ground and water, as height in lakes and snow, and as chemical bonds in wood, coal, and oil. Heat storage is short-lived; height storage lasts until the water flows; chemical storage lasts until the fuel burns or decays.
- **Numbers:** 1 m³ of water stores 4.2 MJ per kelvin of warming; 1 m³ of water 10 m up stores ~98 kJ; 1 kg of dry wood stores ~16 MJ; a warm rock cools to air temperature within hours to days.
- **Check:** Warm a water tank and a rock of equal mass by the same energy and track cooling; the water must stay warm at least 5 times longer than the rock, or the storage rule is wrong.

**278. Energy flows through food webs later**
- **Rule:** Once living things exist, energy flows from sunlight into chemical bonds, then from eater to eaten, losing most of its energy as heat at each step. Only about a tenth of the energy at one level reaches the next. This rule is stated here as the abiotic frame: the energy is already flowing before life arrives, and life taps into it.
- **Numbers:** Roughly 10% of energy transfers between feeding levels; sunlight-to-chemical conversion by later photosynthesis is ~1–2% efficient overall; the rest becomes heat.
- **Check:** Measure the energy in sunlight falling on a patch and the chemical energy stored by any capturing process on it; the stored fraction must be below 5%, and the remainder must appear as heat, or the flow rule is wrong.

**279. Night, clouds, and energy gaps**
- **Rule:** Solar energy stops at night and falls under cloud, so the world must ride through gaps on stored heat. Ground and water release their stored heat after sunset, which is why nights are cooler but not freezing and why cloudy nights are warmer than clear ones. The gap is bridged by storage, not by new energy.
- **Numbers:** Clear-sky night cooling is ~50–100 W/m²; cloud cover cuts that to ~20–50 W/m²; the ground releases ~5–10 MJ/m² overnight from its stored daytime heat.
- **Check:** Log surface temperature on a clear night and a cloudy night with the same daytime sun; the cloudy night must stay at least 2 K warmer, and the ground heat released must match the night cooling, or the storage-gap rule fails.

**280. The energy audit**
- **Rule:** The whole world's energy is audited like a ledger: solar in, reflected out, infrared out, stored as heat, stored as height, stored as chemistry. Every flow is measured in the same units, watts per square metre, over the same period. An audit that does not close is a signal, not a rounding error.
- **Numbers:** Audit period 30 days; report solar in, reflected, infrared out, heat storage change, and chemical storage change, each to 1 W/m²; the books must close within 5 W/m².
- **Check:** Produce the 30-day audit; if it does not close within 5 W/m², find the missing flow and record it before any energy claim is made, or the audit fails.

### 3.9 Materials for building

**281. Wood: the first building material**
- **Rule:** Wood is strong along its grain and weak across it, light for its strength, and easy to cut and join with stone tools. Dry wood lasts; wet wood rots. Different trees give different wood: oak is hard and durable, pine is light and straight, willow bends without breaking.
- **Numbers:** Dry oak density ~700 kg/m³, pine ~500 kg/m³; wood is ~10 times stronger along the grain than across it; a 10 cm pine beam spans ~2 m under its own load plus a light roof.
- **Check:** Load beams of oak and pine along and across the grain until they break; along-grain strength must exceed across-grain strength by at least 5 times, and oak must carry more than pine, or the wood rule is wrong.

**282. Stone: weight and permanence**
- **Rule:** Stone is heavy, hard, and permanent: it carries weight in compression, resists fire and weather, and lasts far longer than wood. It is weak in tension, so stone spans short distances unless arched. Dry stone walls stand by weight and friction alone.
- **Numbers:** Granite density ~2,700 kg/m³, compressive strength ~100–250 MPa, tensile strength ~5–15 MPa; a dry stone wall 0.5 m thick stands ~2 m high without mortar.
- **Check:** Crush granite and sandstone samples and test them in tension; compressive strength must exceed tensile strength by at least 10 times, and granite must be stronger than sandstone, or the stone rule fails.

**283. Clay, mud, and daub**
- **Rule:** Clay is fine-grained, plastic when wet, and hard when dry; mixed with straw and sand it makes daub that fills gaps between wooden frames. Fired clay becomes brick and pottery, which hold water and resist weather. Clay is found where still water once settled its fine grains.
- **Numbers:** Clay particles are below 0.004 mm; unfired daub dries to a compressive strength of ~1–2 MPa; fired brick reaches ~10–30 MPa; clay shrinks ~5–10% on drying.
- **Check:** Make daub from clay, straw, and sand, dry it, and test it; it must hold its shape, shrink less than 10%, and resist crumbling under finger pressure, or the clay rule is wrong.

**284. Fibres: rope, cloth, and thatch**
- **Rule:** Plant fibres — flax, hemp, grass, bark — can be twisted into rope, woven into cloth, and layered into thatch. Rope is strong in tension and useless in compression; thatch sheds rain when laid steeply and thickly. Fibres rot when wet and burn when dry, so they need shelter and care.
- **Numbers:** Hemp rope breaks at ~500–900 N per square millimetre of cross-section; flax fibre is ~1.5 times stronger than cotton; thatch needs a slope of at least 45° and a thickness of 25–30 cm to shed rain.
- **Check:** Twist rope from hemp and grass and pull-test both; hemp rope must carry at least twice the load of grass rope at the same thickness, and a thatch sample at 45° must shed water without leaking, or the fibre rule fails.

**285. Hides and sinew**
- **Rule:** Animal hides, once scraped and dried, become leather: tough, flexible, and water-resistant. Sinew is strong cord for binding and lashing. Both come from animals that lived and died in the world; neither is placed. Raw hide rots; dried and worked hide lasts.
- **Numbers:** Leather tensile strength is ~20–30 MPa; a deer hide yields ~0.5–1 m² of leather; sinew cord is roughly as strong as hemp rope at the same thickness.
- **Check:** Prepare a hide by scraping and drying and test a strip; the finished leather must be flexible, resist tearing by hand, and shed water, while raw hide must rot within weeks, or the hide rule is wrong.

**286. Sand, lime, and mortar**
- **Rule:** Burned limestone makes quicklime, which slaked with water makes lime mortar; mixed with sand it binds stone and brick. Lime mortar sets slowly by absorbing CO₂ from the air, and it stays slightly flexible, which suits stone walls. Sand alone is fill, not a binder.
- **Numbers:** Limestone calcines at ~900 °C to CaO; slaking releases heat; lime mortar reaches ~2–5 MPa after months of curing; a 1:3 lime-to-sand mix is the working ratio.
- **Check:** Burn limestone, slake it, mix mortar, and build a small wall; the mortar must set over weeks, hold the stones together under hand pressure, and test at 1–5 MPa, or the lime rule fails.

**287. Glass from sand**
- **Rule:** Sand melted at high heat with an alkali flux becomes glass: hard, brittle, transparent, and waterproof. Glass is made from ordinary sand, not from a special ingredient, but it needs a hotter fire than smelting copper. Broken glass can be remelted; it does not rot or rust.
- **Numbers:** Pure silica melts at 1,710 °C; with soda ash as flux, glass melts at ~1,200–1,400 °C; glass density ~2,500 kg/m³; glass transmits ~90% of visible light.
- **Check:** Melt sand with soda ash at the stated temperature and cool it; the product must be transparent, hard enough to scratch with steel, and waterproof, or the glass rule is wrong.

**288. Metals for tools and structure**
- **Rule:** Copper is soft and easy to shape but dulls fast; bronze is harder and holds an edge; iron is stronger still once smelted and worked. Metal can be melted, cast, hammered, and sharpened, and it can be remelted and reused. Each metal's use follows its hardness and melting point, not a label.
- **Numbers:** Copper hardness ~3 on the Mohs scale, bronze ~3.5–4, iron ~4–5, steel ~5.5–6.5; copper melts at 1,085 °C, iron at 1,538 °C; bronze holds an edge roughly twice as long as copper.
- **Check:** Cast and hammer copper, bronze, and iron samples and test their edges on wood; bronze must outlast copper, and iron must outlast bronze, by a measured margin, or the metal rule is wrong.

**289. Joining: lashing, pegging, and fitting**
- **Rule:** Materials are joined by lashing with fibre or sinew, by wooden pegs, by fitting shapes together, and later by mortar and metal fasteners. A joint is as strong as its weakest part; a lashed joint flexes, a pegged joint locks, and a mortared joint sets hard. The join must suit the loads it carries.
- **Numbers:** A lashed joint carries ~50–70% of the rope's strength; a hardwood peg in a mortise carries ~5–10 kN in shear; a dry stone wall relies on friction alone, with a friction coefficient of ~0.5–0.7.
- **Check:** Build lashed, pegged, and mortared joints and load them to failure; each must fail at its joint, not in the middle of the member, and the failure loads must fall in the stated ranges, or the joining rule is wrong.

**290. Materials wear, rot, and return**
- **Rule:** Every building material ages: wood rots when wet, iron rusts, thatch thins, mortar cracks, and stone weathers. Nothing built lasts forever without repair. Worn material returns to the cycles — wood to soil, iron to rust, lime to limestone — so building is borrowing from the world, not taking from it permanently.
- **Numbers:** Untreated wood in wet ground rots in 2–5 years; thatch lasts 20–50 years; iron rusts at ~0.01–0.1 mm per year in damp air; stone weathers at ~0.001–0.01 mm per year.
- **Check:** Leave wood, iron, and thatch samples exposed for 90 days and measure the change; wood must show rot where wet, iron must show measurable rust, and thatch must thin, or the decay rule is wrong.

### 3.10 The world provides

**291. Water is found, not given**
- **Rule:** Water sits in springs, streams, rivers, lakes, and rain, and its location follows the land: it flows downhill, pools in hollows, and seeps from the ground where the water table meets the surface. Finding water means reading the land, not receiving it. A dry place has no water because the land gives none there.
- **Numbers:** A spring flows where the water table crosses the surface; a stream flows at 0.1–2 m/s; rain falls at 0–50 mm per hour in a storm; a person needs ~2–3 litres of drinking water per day.
- **Check:** Map every water source in a 128 m locale and trace each to a hollow, a spring line, or a catchment; every source must have a landform cause, and no source may appear without one, or the water-placement rule fails.

**292. Food grows where conditions allow**
- **Rule:** Edible plants grow where soil, water, light, and temperature suit them, and nowhere else. Fruit ripens in season; roots store food underground; seeds fall and sprout where they land. The world provides food in patches and seasons, not evenly and not all year.
- **Numbers:** A fruiting shrub yields ~0.5–5 kg per season; roots yield ~0.1–1 kg per square metre in rich soil; growing seasons run 100–200 days in temperate climates.
- **Check:** Survey food plants across a locale in two seasons; their distribution must follow soil and water, not a uniform grid, and yields must fall to near zero out of season, or the food rule is wrong.

**293. Shelter is in the land**
- **Rule:** The land itself shelters: caves, overhangs, dense trees, and lee slopes break wind and rain. A good shelter is dry, out of the wind, and above flood level. The five houses in the later human experiment are a starting condition, honestly labelled; before them, shelter is whatever the land offers.
- **Numbers:** A cave or overhang cuts wind speed by 80–100% and rain to near zero; a lee slope cuts wind by 50–70%; a shelter must stay dry in a 10 mm/h rain and above the 1-in-10-year flood line.
- **Check:** Measure wind and rain inside a cave, under trees, and on open ground during a storm; the sheltered places must be measurably drier and calmer, or the shelter rule fails.

**294. Fuel is gathered, not delivered**
- **Rule:** Firewood comes from dead wood on the ground, from fallen branches, and from trees that can be cut. Dead wood is dry and ready; green wood must dry first. A patch that is stripped of dead wood stays stripped until more falls, so fuel is a resource that can run out locally.
- **Numbers:** A temperate woodland drops ~1–3 tonnes of dead wood per hectare per year; dry dead wood is below 20% moisture; green wood is 40–60% moisture and needs weeks to months to dry.
- **Check:** Gather all dead wood from a marked hectare and weigh it; the yield must be 0.5–3 tonnes, and a second gathering a month later must yield far less, or the fuel rule is wrong.

**295. Stone and clay are where the rock is**
- **Rule:** Flint, clay, and good building stone are found where the geology puts them: flint in chalk, clay in old lake beds, granite where it cooled underground and was exposed. A locale without that geology has none of that material, and its people must travel, trade, or do without.
- **Numbers:** Flint nodules are 5–30 cm across in chalk beds; clay beds are 0.5–5 m thick in old lake deposits; a workable stone outcrop must expose at least 1 m² of sound rock.
- **Check:** Map flint, clay, and stone across three geologically different locales; each material must appear only where its geology predicts it, and be absent where it does not, or the material-placement rule fails.

**296. The world is patchy by design**
- **Rule:** Resources are patchy: water here, good stone there, fruit in one valley and none in the next. Patchiness is a consequence of geology, water, and climate, not a setting chosen to make the game interesting. Patchiness is what makes movement, memory, and sharing matter.
- **Numbers:** In a 128 m locale, water covers ~5% of the ground, food patches cover ~10–20%, and workable stone covers ~1–5%; patch sizes range from 1 to 20 m across.
- **Check:** Map water, food, and stone patches in a locale and measure their cover fractions; they must fall in the stated ranges and show clustering, not a uniform spread, or the patchiness rule is wrong.

**297. Seasons change what is provided**
- **Rule:** What the world provides changes with the seasons: fruit in summer, nuts in autumn, bare branches in winter, new growth in spring. Water freezes in winter and floods in spring. A creature that lives only on one season's food starves in the next; survival means tracking the year.
- **Numbers:** Fruit is available for 4–8 weeks per year; nuts for 4–6 weeks; green growth for 12–20 weeks; winter food availability falls to 10–30% of summer levels.
- **Check:** Survey food availability monthly for a full year; availability must peak in summer and fall by at least half in winter, or the seasonal-provision rule is wrong.

**298. Scarcity is real and measurable**
- **Rule:** Resources run out: a spring can run dry in drought, a food patch can be stripped, a woodlot can be cut over. Scarcity is not a punishment; it is what happens when use exceeds renewal. The world keeps count, and the count is visible in the measurements.
- **Numbers:** A food patch stripped to zero takes a full growing season to recover; a spring's flow falls by 50% or more in a dry month; dead wood renews at 1–3 tonnes per hectare per year.
- **Check:** Strip a marked food patch and a dead-wood plot and measure recovery over a season; both must recover at the stated rates and no faster, or the scarcity rule fails.

**299. Discovery, not delivery**
- **Rule:** Nothing in this phase is handed to anyone: no recipe, no label, no map, no instruction. Copper plus tin plus heat makes bronze because chemistry says so, not because anyone was told. A creature that tries combinations, remembers what worked, and teaches others is doing science; the world only provides the rules.
- **Numbers:** A combination is a discovery when it is found by trial and recorded by the finder; the Discovery Principle test applies: could the owner have predicted it? If yes, it was placed; if no, it was discovered.
- **Check:** Record the first bronze made in the world with its maker, method, and date; the record must show trial and error before success, with no prior label or instruction in the logs, or the discovery rule fails.

**300. Phase 3 closes when the world is measured**
- **Rule:** Phase 3 is done when sunlight, heat, the element set, water chemistry, rocks and ores, fire, the cycles, the energy flows, and the building materials are all implemented as rules and measured in the world — not when they are described. Every topic above has a Check, and the phase closes only when those checks pass.
- **Numbers:** 100 topics (201–300) across 10 milestones; each topic's Check must report a measured number or a falsifier result; the phase record lists which checks passed, which failed, and what changed.
- **Check:** Produce the Phase 3 record: the energy audit, the water audit, the carbon audit, and the material inventory, each closing within its stated tolerance, with every topic's Check marked pass or fail — or the phase is not closed.

## Phase 4 — Evolution rulebook: inheritance and variation

### 4.1 The genome

**301. What a genome is**
- **Rule:** A genome is the complete heritable instruction set an organism carries. Its chemistry reads it to build proteins, signals, and the copying machinery. The same genome can build different bodies in different conditions, and it outlives every body it builds.
- **Numbers:** Alphabet of 4 symbols (A, C, G, T, as in real DNA). Protocell strands 8–32 bases; cell genomes 1,000–10,000 bases; human-scale genomes up to 3.2 billion bases. One complete copy per cell at minimum.
- **Check:** A lineage query returns the full genome of any living organism and its ancestors to generation 0; a genome with any symbol missing fails the completeness test and is logged.

**302. The genome as a string**
- **Rule:** The genome is stored as one ordered string (or a small set of strings, one per chromosome). Every position has an address and every gene has a start and an end. Order matters: genes near each other are inherited together more often, and a change at one address affects only what that address codes for.
- **Numbers:** Protocell: 1 string. Cell scale: 1 string of 1,000–10,000 bases. Multicellular scale: 1–8 strings. Human scale: 46 strings (chromosomes), 3.2 billion bases total. Address range 0 to length − 1, no gaps.
- **Check:** Any genome read back from a living organism is a valid string over the 4-symbol alphabet with the recorded length; a length mismatch is a logged error, not a silent fix.

**303. Genes: the units the genome is read in**
- **Rule:** A gene is a contiguous run of bases that codes for one functional product: a protein, a structural RNA, or a regulatory signal. It has a start marker and a stop marker the reading chemistry recognises. Genes are the units selection acts on indirectly: a gene's product changes what the organism can do, and the gene is copied with the genome.
- **Numbers:** Protocell: 1 gene (the catalyst motif, GG start, ≥4 bases). Cell scale: 10–100 genes, each 50–500 bases. Human scale: ~20,000 protein-coding genes. Start marker 2 bases, stop marker 2 bases.
- **Check:** Every gene parses to a product with a measured effect (or a recorded neutral effect); a gene that parses to nothing is flagged as a pseudogene and counted, not hidden.

**304. Non-coding DNA is real DNA**
- **Rule:** Bases that do not code for a product still count. They hold binding sites, spacers, and regulatory switches that decide when and how strongly a gene is read. A mutation in a non-coding base can change behaviour as surely as one inside a gene, by changing a switch instead of a product.
- **Numbers:** Cell scale: 10–30% non-coding. Human scale: ~98% non-coding. Regulatory switch: 6–20 bases. A switch mutation changes expression by a measured factor, logged per event.
- **Check:** In ≥5 seeds, at least one recorded behavioural change traces to a non-coding mutation; if none ever does, the regulatory model is re-examined, not assumed correct.

**305. Genome size by scale**
- **Rule:** Genome size grows with the organism. More kinds of cell, more regulation, and more behaviour need more instructions. But size is a cost, since every base must be copied at every reproduction. The size ladder is a measured outcome of that trade-off, not a target set by hand.
- **Numbers:** Protocell strand 8–32 bases; simple cell 1,000–10,000; complex cell 100,000–1,000,000; small animal 10–100 million; fruit fly 180 million; human 3.2 billion. Copying cost scales linearly with length.
- **Check:** Median genome length per scale is logged per generation; a lineage whose genome grows >2× without a measured capability gain is flagged for review.

**306. Redundancy: backup copies**
- **Rule:** Some genes exist in more than one copy, so a mutation that breaks one copy leaves the other working. Redundancy is bought with copying cost: each extra copy is copied at every reproduction and can itself mutate. Redundant copies are free to drift and may later take on new roles. That is one route by which new functions appear.
- **Numbers:** Start with 1 copy per gene. Duplication events (see 324) create 2 copies. A lineage with ≥2 copies of a gene tolerates a breaking mutation in one copy with no measured fitness loss; with 1 copy the same mutation is lethal or costly.
- **Check:** In a run with duplication enabled, count lineages carrying ≥2 copies of at least one gene; report the fraction and whether any duplicated copy diverged in function.

**307. The genotype–phenotype map is fixed chemistry**
- **Rule:** The map from genome to organism is the organism's own reading chemistry. It is fixed rules, the same for every organism at a given scale — not a lookup table the owner edits per species. A given genome in a given environment produces a distribution of phenotypes. The map itself never changes to favour an outcome.
- **Numbers:** One map per scale, versioned. Protocell map: GG-start catalyst, efficiency 1 + 2 × GC fraction. Cell map: gene → protein → trait, each trait a number in a stated range. Map version recorded with every run.
- **Check:** Two runs with the same genome, same map version, and same seed produce the same phenotype distribution within documented numerical error; a mismatch is a bug, logged and fixed.

**308. One genome, many cells**
- **Rule:** In a multicellular body, every cell carries the same genome. What differs is which genes are switched on in each cell. The genome is therefore the body's shared instruction set, and a mutation in one body cell is not inherited. Only mutations in the reproductive line reach the next generation.
- **Numbers:** Body cells share 100% of the genome sequence at birth. Somatic (body-cell) mutation rate per division equals the germline rate, but 0% of somatic mutations are inherited. Germline cells: the named reproductive line, 1–10 cells per body at first.
- **Check:** Sequencing two cells from the same body shows identical genomes at birth; a body-cell mutation appears in that cell's descendants only, never in the offspring body.

**309. The genome is the organism's identity**
- **Rule:** An organism's genome is its heritable identity. Offspring are recognised as kin by genome similarity, lineages are traced by genome descent, and the species criterion (reproductive isolation OR genetic distance beyond a measured threshold) is computed from genomes. Two organisms with identical genomes in identical environments are the same kind of organism.
- **Numbers:** Genetic distance measured as fraction of differing bases over aligned length. Species threshold: to be set by experiment — Freebuff proposes the starting value, Muse reviews. Kin threshold for the social record: ≥99% identity.
- **Check:** The lineage tree built from genomes matches the recorded parent–offspring tree in ≥99% of links across ≥5 seeds; mismatches are investigated, not smoothed over.

**310. Genome completeness at birth**
- **Rule:** An offspring is born with one complete genome, copied from its parent (or combined from two parents where recombination applies). A birth with a truncated or unreadable genome does not happen. The copy is checked before the offspring is counted as alive, and a failed copy is a failed reproduction, recorded as such.
- **Numbers:** Completeness check: length matches parent length ± recorded indels, alphabet valid, all gene markers parse. Failed-copy rate target: <1% of attempted reproductions at cell scale. A failed copy costs the parent the reproduction energy.
- **Check:** Every birth log entry carries a completeness flag; the fraction of births with a failed check is reported per run, and a run with >5% failed copies is flagged as a copying-system failure.

### 4.2 Copying

**311. Replication: the copy rule**
- **Rule:** At reproduction the genome is copied base by base from the parent template, using the same chemistry that reads it. Copying needs energy and raw materials (monomers) and takes time proportional to genome length. A parent without enough energy or monomers does not reproduce.
- **Numbers:** Copying cost: 1 energy unit per 100 bases copied, plus 1 monomer per base. Copying speed: 100 bases per tick at cell scale. Energy below the copying cost blocks reproduction; the block is logged, not bypassed.
- **Check:** In a rich dish, a single cell reproduces and the offspring genome matches the parent within the measured error rate; energy spent per copy matches the cost rule within 5%.

**312. Copying fidelity: how faithful is faithful**
- **Rule:** Copying is not perfect. The chemistry misreads a base with a small probability at each position, and that misreading is a mutation (see 4.3). Fidelity is set by the copying chemistry: proofreading enzymes lower it, their absence raises it. Fidelity is a property of the organism, encoded in its own genome, so fidelity itself can evolve.
- **Numbers:** Baseline per-base error 1 × 10⁻³ at protocell scale (2% per-base in the validated protocell criterion, measured); 1 × 10⁻⁶ at cell scale; 1 × 10⁻⁸ at human scale. Proofreading improves fidelity 10–100× at 2× energy cost per base.
- **Check:** Measured per-base error rate per run, computed from parent–offspring genome pairs across ≥1,000 copies; reported against the stated baseline, with the proofreading state recorded.

**313. Proofreading: catching errors while copying**
- **Rule:** A proofreading step re-reads each newly copied base and corrects a mismatch before copying moves on. It costs extra time and energy per base. Proofreading is a gene product: organisms whose genome codes for it copy more faithfully, and organisms that lose it copy worse. Proofreading never corrects an error perfectly: its own error rate is part of the fidelity number.
- **Numbers:** Proofreading cuts the per-base error 10–100×. Cost: +1 energy unit per 100 bases, +20% copying time. Protocells have no proofreading (error 2% per base, as validated). Proofreading appears as a gene product at cell scale and above.
- **Check:** Lineages with the proofreading gene show a measured per-base error ≥10× lower than lineages without it, across ≥5 seeds; if not, the proofreading implementation is re-examined.

**314. Copying cost and the energy budget**
- **Rule:** Copying is the most expensive single act in a cell's life. It spends energy and monomers in proportion to genome length, and a lineage with a longer genome pays more at every reproduction. This cost is what keeps genomes from growing without limit: a base that earns nothing still costs something at every copy.
- **Numbers:** 1 energy per 100 bases + 1 monomer per base (see 311). A 10,000-base genome costs 100 energy + 10,000 monomers per copy. Monomer shortage stalls copying mid-way; the partial copy is discarded and the spent energy is lost.
- **Check:** Total energy and monomer accounts balance across a run within documented numerical error; a run where copying is free (cost not charged) fails the conservation check.

**315. Semi-conservative copying**
- **Rule:** Each new genome is built from one old strand and one new strand. The parent's double strand unzips, and each half templates a fresh half. The offspring therefore carries half of the parent's actual material and half newly made material. Damage on a template strand is copied into the offspring, while damage on a new strand is a fresh error.
- **Numbers:** 50% of each offspring genome is parental material, 50% newly synthesised. Template damage is inherited at 100% of its occurrences; new-strand errors occur at the per-base error rate. Strand identity (old vs new) is recorded per offspring.
- **Check:** In a run with induced template damage, offspring show the damage pattern at the predicted rate; the old/new strand split is 50/50 within 1% across ≥1,000 births.

**316. Copying time grows with the genome**
- **Rule:** Copying takes time, and time is generations. A longer genome means a longer minimum generation time, so short-genome lineages can out-reproduce long-genome ones in a rich environment. Copying speed is a property of the copying chemistry, not a free parameter tuned per organism. Parallel copying (multiple start points) is a gene-encoded capability that appears at larger scales.
- **Numbers:** 100 bases per tick at cell scale, single start point. A 10,000-base genome needs ≥100 ticks to copy. Human-scale genomes copy from ~10,000 start points in parallel, ~8 hours per copy in real life; the simulation scales this to its tick rate and records the conversion.
- **Check:** Generation time vs genome length is logged per lineage; the relationship is linear within 10% at a fixed copying speed, and any lineage beating it must show the parallel-copying gene.

**317. Copy failure: what happens when copying breaks**
- **Rule:** Copying can fail. Monomers run out, energy runs out, or the template is damaged beyond reading. A failed copy is not a mutant offspring: it is a failed reproduction. The parent keeps its genome, loses the spent energy, and may try again when resources return. Failed copies are logged with the cause, because a rising failure rate signals that the environment or the copying chemistry has changed.
- **Numbers:** Failure causes logged as: energy (target <1% of attempts in rich conditions), monomers (<1%), template damage (rate set by the damage rule, see 322). A run with >5% failed copies in rich conditions is a copying-system failure, not a result.
- **Check:** Failed-copy count and cause are reported per run; the failure rate in rich conditions stays below 5% across ≥5 seeds.

**318. Copying is the only inheritance channel for the genome**
- **Rule:** The genome reaches the next generation only by being copied at reproduction. There is no other route. No organism edits another's genome directly, no genome is downloaded from the world, no offspring is born with a genome that was not copied from a parent. Anything that looks like inheritance but is not genome copying must be named as a separate mechanism (see 4.7) and measured separately.
- **Numbers:** 100% of offspring genomes trace to a parent copy event in the lineage log. Zero genomes appear without a copy event; any such appearance is a logged anomaly and the run is flagged.
- **Check:** An audit query walks every living organism's genome back to a copy event and then to generation 0; the audit passes only if every link exists, across ≥5 seeds.

**319. Copy number: one copy, then two**
- **Rule:** Before reproduction an organism holds one genome copy. Copying produces a second, and the two separate into parent and offspring. At no point does an organism hold three copies by accident, and at no point is a genome copied twice for one birth. The count is enforced by the reproduction rule, not by hoping the chemistry behaves: an extra copy is a logged error.
- **Numbers:** Copy count per birth: exactly 1. Genome copies per organism: 1 (haploid) at cell scale; 2 (diploid, one from each parent) where sexual reproduction applies at animal scale and above. A count violation is a 0-tolerance check.
- **Check:** A random audit of ≥1,000 births finds exactly 1 copy event per birth; any deviation is reported as a defect with the seed and tick.

**320. Copying checkpoint: the genome is verified before birth**
- **Rule:** After copying and before the offspring is counted alive, the new genome is checked: right length, valid alphabet, all gene markers parse, no unreadable region. A genome that fails the check is discarded and the birth is recorded as failed, with the reason. This checkpoint is what keeps a broken copy from entering the population as if it were a viable mutant.
- **Numbers:** Check cost: 1 energy unit per birth, 1 tick. Failure modes logged separately: length, alphabet, markers, unreadable. Target failure rate <1% at cell scale in rich conditions.
- **Check:** Every birth log entry carries the checkpoint result; the fraction of failed checkpoints is reported per run and stays below 5% across ≥5 seeds.

### 4.3 Mutation

**321. Point mutation: one base changes**
- **Rule:** The commonest mutation is a single base swapped for another during copying: A becomes G, C becomes T. One changed base can change one amino acid in a protein, change nothing at all, or break the protein entirely. Point mutations are the raw material of most heritable variation, and their rate is the copying fidelity number from 312.
- **Numbers:** Per-base rate 1 × 10⁻³ protocell, 1 × 10⁻⁶ cell, 1 × 10⁻⁸ human scale. Roughly 1 in 3 point mutations in a coding region is silent; the rest change an amino acid or a stop signal. Rate measured from parent–offspring pairs.
- **Check:** Point mutations per generation match the per-base rate × genome length within 20% across ≥5 seeds; a mismatch means the fidelity number is wrong, not the data.

**322. Damage: mutation from the environment**
- **Rule:** Mutation is not only a copying error. Heat, light, and reactive chemicals damage bases in a living genome, and the damage is copied as a mutation at the next reproduction. Repair genes can fix the damage first. Damage rate rises with temperature and with exposure to reactive chemicals, so the environment sets part of the mutation rate.
- **Numbers:** Baseline damage 1 × 10⁻⁷ per base per generation at 20 °C in clean water; doubles per 10 °C rise; ×10 with a reactive chemical at 1% concentration. Repair genes cut damage 10–100× at 1 energy per 1,000 bases repaired.
- **Check:** Runs at 30 °C show ~2× the damage mutations of runs at 20 °C, and runs with repair genes show ≥10× fewer, both measured from parent–offspring pairs.

**323. Insertions and deletions: bases added or lost**
- **Rule:** Copying sometimes adds a base or skips one, shifting everything after it by one position. A single insertion or deletion inside a gene shifts the reading frame, so every amino acid after it changes — usually breaking the gene. Outside genes, indels shift spacing and can move a regulatory switch closer to or further from its gene.
- **Numbers:** Indel rate ~1 × 10⁻⁷ per base per generation at cell scale (about one-tenth the point rate). A frameshift inside a gene breaks the gene's product in ~95% of cases. Indel size: 1 base in ~90% of events, 2–10 bases otherwise.
- **Check:** Indel count per generation matches the stated rate within 20% across ≥5 seeds; the fraction of frameshifts that break a gene is measured and reported.

**324. Duplication: a gene copied twice**
- **Rule:** A copying slip can duplicate a whole gene, giving the offspring two copies where the parent had one. The second copy is redundant at first, so it can mutate freely without harming the organism. A mutated duplicate can take on a new job. Duplication is the main route by which genuinely new genes appear.
- **Numbers:** Duplication rate ~1 × 10⁻⁶ per gene per generation at cell scale. A duplicated gene diverges from its twin at the point-mutation rate; a new function is recorded only when the diverged copy shows a measured effect different from the original.
- **Check:** Lineages with a duplication event are counted per run; at least one diverged duplicate with a measured new effect is recorded before duplication is claimed as a source of new function.

**325. Inversion: a stretch flipped around**
- **Rule:** A stretch of genome can be cut out and pasted back in reverse order. The genes inside still work, but their order relative to their regulatory switches changes. The flipped stretch no longer lines up with the same stretch in another organism, which matters when two genomes recombine (see 4.4). Inversions are rare, usually neutral, and occasionally break a gene at the cut point.
- **Numbers:** Inversion rate ~1 × 10⁻⁷ per genome per generation at cell scale. Length flipped: 10–1,000 bases. A cut inside a gene breaks it in ~50% of inversion events at that gene; a clean cut between genes is neutral.
- **Check:** Inversion count per run matches the stated rate within an order of magnitude across ≥5 seeds; each inversion's effect (neutral, gene broken, regulation changed) is classified and counted.

**326. Transposition: a jumping gene**
- **Rule:** Some sequences can copy themselves to a new address in the genome. They land inside a gene (breaking it), next to a gene (changing when it is read), or in empty space (doing nothing). The jumping sequence carries its own copying rule inside its own bases, so it spreads within a genome the way a gene spreads within a population.
- **Numbers:** Transposition rate ~1 × 10⁻⁶ per element per generation at cell scale. A genome carries 0–10 jumping elements at first. Landing inside a gene breaks it in ~90% of cases; landing in non-coding space is neutral in ~95% of cases.
- **Check:** The count of jumping elements per genome is logged per generation; a runaway (elements doubling every generation) is flagged as a system failure, and landing effects are classified and counted.

**327. Silent, missense, nonsense: three fates of a point mutation**
- **Rule:** A point mutation inside a gene has one of three fates. Silent: the amino acid stays the same, no effect. Missense: a different amino acid, effect from nothing to fatal. Nonsense: a stop signal appears early, the protein is cut short and usually useless. The fate is decided by the fixed genetic code, not by what would be convenient.
- **Numbers:** Roughly 25% silent, 70% missense, 5% nonsense for a random point mutation in a coding region. Missense effects: ~70% neutral or near-neutral, ~25% harmful, ~5% helpful (starting values, measured per run). Silent mutations accumulate at the raw mutation rate.
- **Check:** The silent/missense/nonsense split is measured from parent–offspring pairs and reported per run; genetic distance for the species criterion is computed from silent changes only.

**328. Most mutations are neutral or harmful; few help**
- **Rule:** A random change to a working system usually does nothing or makes it worse; improvement is rare. This is arithmetic, not pessimism: a genome that already works has far more ways to break than to improve. Most new mutations are carried silently or die with their carriers. The rare helpful one spreads only because its carriers survive and reproduce more (that spreading is Phase 5, not this phase).
- **Numbers:** Starting split for new mutations: ~70% neutral, ~25% harmful, ~5% helpful, measured as the change in the carrier's survival and reproduction over the next 10 generations. A mutation that cuts reproduction by >10% is classed harmful; one that raises it by >10% is classed helpful.
- **Check:** The neutral/harmful/helpful split is measured per run across ≥5 seeds and reported with the sample size; a run claiming >20% helpful mutations is flagged for a measurement error.

**329. Mutation is random in direction, not in rate**
- **Rule:** Which base changes, and where, is random. Mutation does not aim at what the organism needs. What is not random is the rate: some positions mutate more often (fragile sites, repeated sequences), some organisms mutate faster (see 4.9), and some environments damage more. Random direction with a structured rate is what makes evolution search without a plan and still find things.
- **Numbers:** Fragile sites mutate 10–100× the baseline rate; repeated sequences 5–10×. No position mutates toward a needed change more often than chance: the correlation between a mutation's usefulness and its occurrence is measured and must be ~0 (within ±0.05) across ≥5 seeds.
- **Check:** The occurrence–usefulness correlation is computed per run and reported; a positive correlation above 0.05 is a defect (the system is steering mutation) and the run is flagged.

**330. The mutation spectrum is logged, not assumed**
- **Rule:** Every mutation is logged with its type (point, indel, duplication, inversion, transposition), its address, its effect class (silent, missense, nonsense, regulatory), and its fate in the next 10 generations. The spectrum — the mix of types — is a measured property of the world. It changes as the copying chemistry and the environment change. No claim about mutation is made without the log behind it.
- **Numbers:** Log fields per event: type, address, parent genome id, offspring genome id, effect class, 10-generation fate. Log completeness target: 100% of mutations in runs up to 10,000 organisms; sampled at 1% above that, with the sampling rate recorded.
- **Check:** A random audit of ≥100 logged mutations re-derives each from the parent and offspring genomes; the audit passes only if ≥99% match exactly.

### 4.4 Recombination

**331. Crossover: two genomes swap stretches**
- **Rule:** When an organism has two genome copies (one from each parent), the copies can swap matching stretches before being passed on. An offspring then carries a mix: some stretches from one grandparent, some from the other. Crossover does not create new bases. It creates new combinations of existing ones, which is how a helpful mutation in one lineage can join a helpful mutation in another.
- **Numbers:** Crossover rate: 1–3 swaps per genome copy per reproduction at animal scale; 0 at cell scale (single copy, nothing to swap). Swap points are uniform along the genome except at hotspots (see 335). Each swap exchanges a stretch of 100–10,000 bases.
- **Check:** Offspring genomes show the expected mix: the fraction of bases from each grandparent is ~50/50 within 10% across ≥1,000 sexual births; a 100/0 split means crossover did not run.

**332. Recombination needs two parents**
- **Rule:** Recombination is the shuffling of two parents' genomes into one offspring, and it only exists where reproduction combines two genomes. Asexual lineages copy one genome and never recombine; their only variation is mutation. The world therefore has two inheritance modes — clonal and sexual — and which mode a lineage uses is part of its genome, not a setting the owner flips per species.
- **Numbers:** Asexual: 0 recombination events per birth, variation from mutation only. Sexual: 1–3 crossovers per birth plus independent assortment (see 333). Mode is recorded per lineage; a lineage switches mode only by a recorded mutation in its reproduction genes.
- **Check:** The mode of every lineage is logged; asexual lineages show zero recombinant offspring across ≥5 seeds, and sexual lineages show ≥1 crossover in >90% of births.

**333. Independent assortment: whole chromosomes shuffle**
- **Rule:** With several chromosomes, each chromosome in the offspring comes whole from one parent or the other, independently of the others. Even without crossover, an offspring is a new combination. A genome with more chromosomes shuffles more: the number of possible combinations doubles with each added chromosome. This is the coarsest shuffle, and it costs nothing extra beyond the two-parent reproduction itself.
- **Numbers:** Chromosome count: 1 at cell scale, up to 46 at human scale. Possible combinations from assortment alone: 2^n where n is the chromosome count (2 for n = 1, ~7 × 10¹³ for n = 46). Each chromosome's parent of origin is logged per birth.
- **Check:** Parent-of-origin counts per chromosome are ~50/50 within 10% across ≥1,000 births; a chromosome that always comes from one parent is a defect, logged and investigated.

**334. Gene conversion: one copy overwrites the other**
- **Rule:** During recombination, a short stretch of one genome copy can be overwritten by the matching stretch of the other copy, without swapping anything back. One variant is copied and the other is lost for that offspring: a quiet, one-way transfer. Gene conversion is rarer than crossover and shorter in reach, but it is a real route by which a variant spreads inside a lineage.
- **Numbers:** Conversion rate ~1 × 10⁻⁵ per base per reproduction at animal scale. Converted stretch: 10–500 bases. One conversion event per ~10 births at human scale. Each event is logged with its address and the variant copied.
- **Check:** Conversion events are counted per run and the rate matches the stated value within an order of magnitude; the variant copied is verified against the parent genomes in a random audit of ≥100 events.

**335. Recombination hotspots: some places swap more**
- **Rule:** Crossover is not uniform along the genome. Some stretches swap far more often than others, and the hotspot pattern is itself encoded in the genome and can evolve. Hotspots sit mostly between genes, which keeps genes intact while shuffling the combinations around them. A hotspot that moves inside a gene starts breaking that gene at the crossover point, and that cost is paid by the lineage.
- **Numbers:** Hotspot crossover rate 10–100× the genome average; hotspots cover ~5% of genome length and host ~50% of crossovers. A hotspot inside a gene raises that gene's breakage rate 10× at the hotspot address.
- **Check:** Crossover positions are logged per birth; the observed hotspot pattern matches the encoded pattern within 20%, and the fraction of crossovers inside genes is reported per run.

**336. Linkage: neighbours travel together**
- **Rule:** Genes that sit close together on the same chromosome are usually inherited together, because a crossover between them is unlikely. Linkage is the reason a helpful mutation can drag a harmful neighbour along with it, and vice versa. The unit selection sees is often a block of linked genes, not a single gene. Linkage decays with distance: the further apart two genes sit, the more often they are separated.
- **Numbers:** Two genes 1,000 bases apart are separated by crossover in ~1% of births; 100,000 bases apart, ~50% (effectively unlinked). Linkage is measured as the co-inheritance rate across ≥1,000 births and reported as a decay curve per chromosome.
- **Check:** The measured co-inheritance rate falls with distance as stated within 20%; a pair of genes that never separates despite being far apart is flagged as a possible structural defect.

**337. Horizontal transfer: genes move between lineages**
- **Rule:** At cell scale, a gene can move from one organism to another without reproduction. A fragment of genome is released when a cell dies, taken up by a living cell, and stitched into its genome. This is how a useful gene can jump between unrelated lineages, and it is the cell-scale analogue of sex. Transfer is a real chemical event — uptake, stitching, expression — not a copy-paste, and it can fail at each step.
- **Numbers:** Uptake rate ~1 × 10⁻⁶ per gene fragment per cell per generation in a rich dish. Success (uptake + stitching + expression) ~10% of uptakes. Transferred fragment: 100–5,000 bases. Transfer events are logged with donor lineage, recipient lineage, and gene.
- **Check:** Transferred genes are counted per run; a gene found in a lineage whose ancestors never carried it, with a logged transfer event, confirms the route; transfer without a logged event is an anomaly.

**338. Recombination breaks as well as builds**
- **Rule:** Shuffling is not free. A crossover inside a gene breaks it, a crossover between mismatched stretches (after an inversion, see 325) can delete or duplicate a whole block, and a bad combination of two individually fine variants can be worse than either parent. Recombination's cost is paid in broken offspring, and its benefit is paid in new combinations. Both are measured, and neither is assumed to win.
- **Numbers:** Crossover inside a gene breaks it in ~90% of cases. Mismatched crossover (inversion carriers) produces a deleted or duplicated block in ~50% of such births. Broken-offspring rate from recombination: target <2% of sexual births at animal scale.
- **Check:** The broken-offspring rate from recombination is reported per run; a rate above 5% triggers a review of the crossover placement rule, not a quiet tolerance.

**339. Recombination rate is a trait, not a constant**
- **Rule:** How often an organism recombines is set by its own genome: genes that control crossover frequency and hotspot placement. Lineages can therefore evolve toward more shuffling (more new combinations, more breakage) or less (safer copies, slower mixing). The rate is never set by the owner per species; it is a measured trait with a starting value, and it drifts and is selected like any other trait.
- **Numbers:** Starting crossover rate: 1 per genome copy per reproduction. Range observed in real life: 0–5 per copy. Rate changes by mutation in the recombination genes at the point-mutation rate. The rate is logged per lineage per generation.
- **Check:** The recombination rate per lineage is reported per run; at least two lineages differing in rate by ≥2× are recorded before any claim about rate evolution is made.

**340. Recombination does not invent variation, it rearranges it**
- **Rule:** Recombination creates no new base and no new gene. It only rearranges what mutation has already produced. A population with no mutations has nothing to recombine, and recombination in such a population is invisible. This is the clean division of labour in this phase: mutation invents, recombination rearranges, and the two together are what inheritance has to work with.
- **Numbers:** In a control run with mutation disabled, recombinant offspring are genetically identical to their parents at every base: measured difference 0 across ≥1,000 births. With mutation on, recombinant offspring differ from both parents at the mutation rate, rearranged.
- **Check:** The mutation-off control is run once per scale and the zero-difference result recorded; the mutation-on comparison is reported alongside it, with the numbers.

### 4.5 Expression

**341. Reading the genome: transcription**
- **Rule:** Expression starts with transcription: the reading chemistry copies a gene's bases into a working message (RNA), which is then read to build the gene's product. Transcription is the first control point. A gene that is never transcribed might as well not exist, and a gene transcribed constantly floods the cell with its product. The message is short-lived, so expression stops when transcription stops.
- **Numbers:** Transcription rate: 10–50 bases per tick at cell scale. Message lifetime: 10–100 ticks. One gene produces 1–100 messages per 1,000 ticks depending on its switch state. Transcription cost: 1 energy per 100 bases transcribed.
- **Check:** Message counts per gene are logged per 1,000 ticks; a gene with zero messages and a measured product of zero is classed unexpressed, and the switch state that explains it is recorded.

**342. Building the product: translation**
- **Rule:** The message is read three bases at a time. Each triplet names one building block, and the blocks are chained into the product (a protein). Translation is the second control point and the place where most errors become real: a misread triplet puts the wrong block in the chain, and a chain with the wrong shape usually does nothing. Translation stops at the stop triplet, and a message without one is an error, logged.
- **Numbers:** Translation rate: 1 building block per 2 ticks at cell scale. Error rate: 1 wrong block per 10,000 (independent of the genome mutation rate — a translation error dies with the product, it is not inherited). Product lifetime: 100–10,000 ticks.
- **Check:** The fraction of products that fold and work is measured per gene (target >90% for a normal gene); a gene whose products work <50% of the time is flagged as broken or misread.

**343. Switches: when a gene is on**
- **Rule:** Each gene has a switch: a short sequence nearby that the cell's chemistry reads to decide whether to transcribe it. A switch responds to signals: food present, temperature high, a neighbour's chemical, a developmental stage. The switch is part of the genome and mutates like any other sequence, so a lineage can evolve to turn a gene on earlier, later, or in new conditions.
- **Numbers:** Switch length 6–20 bases. A switch has 2–5 signal inputs at cell scale, up to 20 at human scale. Switch mutation changes the on/off threshold by a measured factor, logged per event. A broken switch gives 0 messages per 1,000 ticks.
- **Check:** For each gene, the switch state and the message count are logged together; the correlation between switch signal and transcription is measured, and a gene that transcribes with no signal is flagged.

**344. Expression level: how much, not just on or off**
- **Rule:** Expression is a dial, not a switch. A gene can be read a little or a lot, and the amount of product sets the strength of the trait. The level is set by the switch's strength, the number of messages, and how fast the product is broken down. Small level changes are the commonest way a mutation changes behaviour — a little more of an enzyme, a little less of a signal — without breaking anything.
- **Numbers:** Expression level measured as product molecules per cell: 0–10,000. A 2× level change is the smallest change classed as significant. Level is logged per gene per 1,000 ticks, with the switch strength recorded alongside.
- **Check:** A mutation that changes a trait is traced to either a product change or a level change, and the split is reported per run; a trait change with neither is a measurement defect.

**345. Regulation: genes control genes**
- **Rule:** Some gene products are regulators: they bind to other genes' switches and turn them on or off. This builds chains and loops — gene A turns on gene B, which turns off gene A — and those loops are what make development (see 4.6) and behaviour possible. A regulatory loop is a mechanism, not a plan: it runs the same chemistry as everything else, and a mutation in a regulator ripples through every gene it controls.
- **Numbers:** One regulator controls 1–50 target genes at cell scale, up to 1,000 at human scale. Loop depth: 2–5 genes in a chain at cell scale. A regulator mutation changes the expression of all its targets; the count of affected targets is logged per event.
- **Check:** The regulatory network (regulator → targets) is recorded per lineage; a mutation in a regulator is verified to change its targets' message counts in the predicted direction in ≥80% of cases.

**346. Expression costs energy**
- **Rule:** Every message transcribed and every product built costs energy and raw materials, so expressing a gene is a spending decision the organism makes continuously. A gene expressed at full level in conditions where its product is useless is a drain, and lineages that switch it off in those conditions save the cost. This is why switches evolve: they are how the organism stops paying for what it does not need.
- **Numbers:** 1 energy per 100 bases transcribed + 1 energy per 10 building blocks translated. A highly expressed gene (10,000 products) costs ~10% of a cell's energy budget per 1,000 ticks. Unused expression is logged as waste per lineage.
- **Check:** Energy accounts balance with expression costs included; lineages with a gene switched off in conditions where its product is unused show a measured energy saving of ≥5% versus lineages with it on.

**347. Timing: genes turn on in order**
- **Rule:** Expression is timed. Some genes read early in life, some late, some only at reproduction, some only in one cell type. Timing is set by switches that respond to the organism's age, its energy state, and developmental signals. A gene read at the wrong time is as useless as a gene never read: the product arrives when nothing needs it, or too late.
- **Numbers:** Timing recorded as the tick or generation at which a gene first reaches half its maximum level. Timing shifts of ≥100 ticks at cell scale are classed as significant. A gene's timing is logged per lineage per generation.
- **Check:** The timing curve of each gene is logged; a mutation that shifts a gene's timing by ≥100 ticks is classified as a timing mutation and its effect on the organism recorded.

**348. Expression noise: the same genome, different levels**
- **Rule:** Expression is noisy. Two cells with identical genomes in identical conditions express the same gene at slightly different levels, because transcription is a chemical process with random collisions. Noise is real variation, but it is not heritable: the offspring's level is drawn fresh from the same distribution. Noise is what makes genetically identical organisms differ, and it is measured as a spread, not treated as a defect.
- **Numbers:** Expression noise: coefficient of variation 0.1–0.5 per gene (level varies ±10–50% around its mean). Noise is larger for low-expression genes. The noise level per gene is a property of its switch and is logged.
- **Check:** Two cells with identical genomes show expression levels differing within the stated noise range; a difference beyond 3× the noise range is flagged as an environmental or genetic difference, not noise.

**349. Environment changes expression**
- **Rule:** The same genome expresses differently in different conditions. Heat turns on heat-response genes, hunger turns on foraging genes, a neighbour's signal turns on social genes. This is not the environment rewriting the genome: the switches were already there, waiting for the signal. Environmental induction is the mechanism behind plasticity (see 4.8), and it is measured as a level change per condition, not as a vague response.
- **Numbers:** Induction factor: expression level in the inducing condition divided by the level without it, typically 2–100×. Each gene's induction factor is measured per condition (temperature, food, light, neighbour signal) and logged. A gene with an induction factor >10 is classed as strongly induced.
- **Check:** For each gene and condition, the induction factor is measured across ≥5 seeds and reported; a gene claimed to respond to a condition must show a factor ≥2× in at least 4 of 5 seeds.

**350. Expression is the phenotype's first draft**
- **Rule:** The phenotype — what the organism is and does — begins as an expression pattern: which genes are on, at what level, in which cells, at what time. Everything downstream (development, behaviour, the mind) reads that pattern, not the genome directly. Two organisms with the same genome but different expression patterns are different phenotypes, and the difference is fully explained by the switches, signals, and noise recorded in this milestone.
- **Numbers:** The expression pattern is a vector: one level per gene per cell type per time window, logged per organism per 1,000 ticks. Pattern distance between two organisms is the mean absolute level difference across genes; a distance >2× the noise floor marks a different phenotype.
- **Check:** Organisms with the same genome and the same expression pattern show the same measured traits within noise; organisms with different patterns differ in at least one trait, verified across ≥5 seeds.

### 4.6 Development

**351. Development is the genome read in sequence**
- **Rule:** Development is what happens when the genome's timed switches fire in order. Genes turn on, products accumulate, cells divide, and the body takes shape step by step. There is no blueprint of the finished body anywhere: the body is the result of the sequence, the way a building is the result of following instructions in order. Change the order and the body changes; break a step and development stops or goes wrong at that step.
- **Numbers:** Development is a sequence of 5–50 timed steps at small-animal scale, up to ~1,000 at human scale. Each step is a gene or gene group reaching its threshold level. Step order and timing are logged per organism; a step that fires out of order is a developmental defect, logged.
- **Check:** The step sequence of a developing organism is logged and compared to its lineage's normal sequence; ≥95% of organisms follow the same order within timing noise, and deviations are classified by step.

**352. Cell division: one cell becomes two**
- **Rule:** Development proceeds by division: a cell copies its genome (see 4.2), grows, and splits into two cells that each carry the full genome. Division is the only way a body gains cells, and the division rate sets the pace of development. Fast division builds a body quickly and spends energy quickly. Which cells divide, and when, is decided by their switches responding to local signals, not by a central plan.
- **Numbers:** Division time: 100–1,000 ticks per division at cell scale. A body of 1,000 cells needs ≥10 rounds of division from one cell. Division cost: the copying cost (see 314) plus 10 energy for growth. Division rate per cell is logged per 1,000 ticks.
- **Check:** Cell counts per body match the division log within 1%; a body whose count exceeds its divisions is a logging defect, and a body that stops dividing without a recorded signal is flagged.

**353. Positional signals: cells know where they are**
- **Rule:** A developing body tells its cells where they are with chemical gradients. A signal released at one end is strong there and weak at the other, so each cell reads the local concentration and switches on the genes for its position. Head versus tail, front versus back, inside versus outside: all are read from gradients, not assigned by the owner. Move the signal and the body plan moves with it.
- **Numbers:** Gradient range: across the whole body, 10–1,000 cells long. A cell reads concentration with ±10% accuracy. Positional genes switch on at thresholds spaced ~10-fold apart along the gradient (e.g. 100, 10, 1 units). Signal sources: 2–6 per body at first.
- **Check:** Moving a signal source by a recorded amount shifts the positional boundary by the predicted distance within 20%; a body plan that does not move with its signal is a defect.

**354. Differentiation: same genome, different cell**
- **Rule:** A cell differentiates when its switches lock into a pattern — skin cell, gut cell, muscle cell — and stay there. The lock is a regulatory loop (see 345) that holds itself on: once a cell commits, its daughters inherit the switched-on state, so a body keeps its cell types across divisions. Differentiation is reversible only if the loop can be broken, and the conditions for breaking it are part of the genome.
- **Numbers:** Cell types: 2–5 at first multicellular scale, ~200 at human scale. Commitment takes 100–1,000 ticks of sustained signal. A differentiated cell keeps its type across ≥10 divisions unless the breaking condition is met. Type counts per body are logged.
- **Check:** Cell-type counts per body are stable within 10% across the body's life; a cell that changes type without the breaking condition is logged as a differentiation defect.

**355. Growth: bodies get bigger by rules**
- **Rule:** Growth is division plus enlargement, gated by food and energy. A body grows while it has surplus energy and stops when it does not. Size is not a target: it is the balance between division rate and death rate of cells, and the balance is set by the genome's switches responding to energy. A body that grows without limit is a body whose stop signal is broken, and it pays for it in energy.
- **Numbers:** Growth rate: 1–10% size increase per 1,000 ticks while energy is above the growth threshold (energy >50% of maximum). Adult size range per lineage is logged; a body exceeding its lineage's size range by >50% is flagged as runaway growth. Cell death balances division at adult size.
- **Check:** Body size over time is logged per organism; size plateaus within the lineage's range in ≥90% of adults, and runaway cases are counted and reported.

**356. Body plans from local rules**
- **Rule:** A body plan — the arrangement of parts — comes from local rules only. Cells divide, read gradients, differentiate, and stick to their neighbours. No cell knows the whole plan; the plan is what the local rules add up to. Two bodies with the same genome and the same starting conditions develop the same plan, and a mutation in a positional gene changes the plan in a way that can be traced back to that gene.
- **Numbers:** Body plans are described by the count and arrangement of cell types, logged per organism. Plan repeatability: ≥90% of organisms from one lineage share the same plan within measurement error. A plan change traces to a mutation in ≥80% of cases where a plan changes.
- **Check:** The plan of each body is recorded and compared to its lineage's plan; the repeatability figure is reported per run, and plan changes without a traced mutation are investigated.

**357. Developmental errors and how they are handled**
- **Rule:** Development can go wrong: a cell divides at the wrong time, a gradient is misread, a switch fires early. Most errors are small and the body absorbs them. Neighbouring cells compensate, the extra cell dies, the misread gradient is re-read at the next step. Errors that cannot be absorbed produce a malformed body, which usually dies or reproduces poorly. There is no repair crew with a plan — only the same local rules running again.
- **Numbers:** Error rate: ~1 developmental error per 1,000 cell divisions. Absorption rate: ~90% of errors leave no measurable trace in the adult. Malformation rate: <1% of bodies at cell-to-small-animal scale. Errors and their outcomes are logged per body.
- **Check:** The error, absorption, and malformation rates are reported per run across ≥5 seeds; a malformation rate above 5% triggers a review of the gradient or switch rules.

**358. Canalization: development resists noise**
- **Rule:** Development is canalized. Small disturbances — a hot day, a missed meal, expression noise — do not change the outcome, because the regulatory loops push development back onto its normal path. Canalization is a property of the loops, not a separate safety system: strong feedback means a disturbance is corrected, weak feedback means it is not. Lineages can evolve more or less canalization by changing loop strength.
- **Numbers:** Canalization measured as the change in adult trait per unit of disturbance: <0.1 (strong) to >1.0 (weak). Test disturbance: ±20% food for 1,000 ticks during development. Adult trait shift under that disturbance is logged per lineage.
- **Check:** Under the standard disturbance, ≥80% of lineages show an adult trait shift below 10%; lineages above that are classed as weakly canalized and the loop strength behind it is recorded.

**359. Development sets the adult, not the other way round**
- **Rule:** The adult body is the end of development, and the adult cannot go back and re-run it. A trait fixed during development stays fixed for life, and only the next generation can develop differently. This is why developmental mutations matter more than adult ones: a change in a developmental switch reshapes the whole body, while a change in an adult gene touches one function.
- **Numbers:** Developmental genes: ~5% of the genome at small-animal scale, ~10% at human scale. A mutation in a developmental gene changes ≥3 adult traits on average; a mutation in an adult-only gene changes 1. Trait counts per mutation class are logged.
- **Check:** The traits-changed-per-mutation figure is measured per class and reported; a developmental mutation that changes nothing is classed as silent and counted separately.

**360. Development is recorded, step by step**
- **Rule:** Every organism's development is logged as a sequence: which steps fired, in what order, at what time, and which cells divided and differentiated when. The log is the evidence that a body was built by rules and not placed. A placed body would have no developmental history, and a body whose log does not add up to its adult form is a defect. The log is kept for the life of the lineage.
- **Numbers:** Log fields per step: step id, tick, genes active, cells divided, cells differentiated. Log size: ~1 KB per organism at small-animal scale. Completeness target: 100% of steps for organisms up to 10,000 cells; sampled above that, with the sampling rate recorded.
- **Check:** A random audit of ≥100 bodies re-derives the adult cell-type counts from the developmental log; the audit passes only if ≥99% match within 1%.

### 4.7 Heritable variation

**361. What counts as heritable**
- **Rule:** Variation is heritable only if it is passed from parent to offspring through a recorded mechanism — genome copying, in the first instance. A difference counts as heritable variation when offspring resemble their parents more than they resemble random members of the population, for that difference. Differences caused by the environment alone, or by noise, are variation but not heritable variation.
- **Numbers:** Heritability measured as parent–offspring regression slope for a trait: 0 means not heritable, 1 means fully heritable. Measured per trait per run, with ≥100 parent–offspring pairs. A trait with slope <0.1 is classed as non-heritable.
- **Check:** The regression slope is computed and reported per trait per run; a trait claimed as heritable must show a slope ≥0.3 in at least 4 of 5 seeds.

**362. Genetic variance: the raw material**
- **Rule:** Genetic variance is the spread of genomes in the population: how different the organisms are from each other at the genome level. It is the raw material inheritance has to work with. A population with zero genetic variance cannot change by inheritance, whatever the environment does. Variance is created by mutation and recombination and is recorded as a number per generation, not as an impression.
- **Numbers:** Genetic variance measured as mean pairwise genetic distance (fraction of differing bases) across ≥100 sampled pairs per generation. Starting variance in a founded population: 0 (clones) rising by mutation; a healthy population holds 0.001–0.01 at cell scale. Variance is logged per generation.
- **Check:** The variance curve is logged per run; a population whose variance stays at 0 for >100 generations after founding is flagged as mutation-starved, and the mutation rate is checked.

**363. Standing variation vs new mutation**
- **Rule:** A population carries two kinds of heritable variation. Standing variation: differences already present, inherited from earlier generations. New mutation: variation that appears fresh each generation. Standing variation is what lets a population respond quickly to change, because the variant already exists. New mutation is slower but inexhaustible. The two are tracked separately.
- **Numbers:** Standing variation counted as the number of variant sites present in >1% of the population at generation 0 of a measurement window. New mutations counted per generation from parent–offspring pairs. In a typical run, standing variants outnumber new mutations 100:1 or more per generation.
- **Check:** Both counts are reported per run; when a trait changes, the variant behind it is traced to standing variation or to a new mutation, and the split is reported.

**364. Heritability is measured, not assumed**
- **Rule:** Heritability is a number measured from data: the parent–offspring slope (see 361) or the twin comparison at larger scales. It is specific to one trait, one population, and one environment. It is never a property of the trait in general: the same trait can be highly heritable in one environment and barely heritable in another, because the environment changes how much of the variation is genetic.
- **Numbers:** Heritability reported as h² (0–1) with the sample size, the trait, the population, and the environment stated. Minimum sample: 100 parent–offspring pairs. A heritability reported without its sample size and environment is an incomplete claim, flagged in review.
- **Check:** Heritability values are recomputed from the raw parent–offspring data in a random audit; the audit passes only if the recomputed value matches within 0.05.

**365. Epigenetic inheritance: marks that ride along**
- **Rule:** Some chemical marks on the genome — a methyl group here, a folded region there — change how a gene is read without changing its bases. Some of those marks survive copying and reach the offspring. This is real inheritance, but it is limited: marks are usually wiped clean within a few generations, they carry far less information than the genome, and they are not a second genome. Marks are logged as marks, never confused with mutations.
- **Numbers:** Mark inheritance: a mark survives to the offspring in ~50% of cases, to the grand-offspring in ~10%, and is gone by generation 3 in >95% of cases (starting values, measured per run). Marks affect expression level only, never the gene's code. Mark count per genome: 0–100 at cell scale.
- **Check:** Mark persistence is measured per run across ≥5 seeds and reported as a decay curve; a mark claimed to persist beyond 3 generations must show the measured persistence to back it.

**366. Maternal effects: the offspring's starting conditions**
- **Rule:** An offspring's starting conditions come from the parent's body, not from the offspring's genome. How much energy it is born with, which messages its mother loaded into it, the temperature of its birthplace: all are set by the parent's state. These maternal effects change how the offspring develops, and they can look like inheritance, but they are not. They last one generation.
- **Numbers:** Starting energy varies ±20% with the parent's energy at birth. Loaded messages: 0–10 per offspring at cell scale, decaying within 100 ticks. A maternal effect that changes a trait by >10% is logged as significant, with the parent's state recorded.
- **Check:** Offspring traits are regressed against both the parent's genome and the parent's state; the state term is reported separately, and a trait attributed to the genome must survive controlling for the parent's state.

**367. What is NOT heritable**
- **Rule:** The following are not inherited, and the system must not let them masquerade as inheritance. Learned behaviour: a memory dies with the mind that holds it, unless it is taught — and teaching is a Phase 7 mechanism, not inheritance. Injuries, acquired traits from use or disuse, and environmental damage to the body are likewise not inherited. An organism that learns to find food does not give birth to offspring that know where food is.
- **Numbers:** Learned behaviour transmission parent-to-offspring without teaching: 0, measured as the offspring's performance on the parent's learned task versus a naive control, difference target 0 ± 5%. Acquired-trait transmission: 0 by the same test. Both are tested once per scale.
- **Check:** The learned-task test is run per scale and the zero result recorded; any positive transmission without a teaching mechanism is a defect and the run is flagged.

**368. Variation persists or it vanishes**
- **Rule:** A new variant either spreads, stays rare, or disappears. Its fate is written in the lineage log, not in a summary. Most new mutations vanish within a few generations by chance alone, even helpful ones, when the population is small. A variant that persists for 100 generations has beaten the odds of chance loss, and that persistence is itself a measurement worth recording.
- **Numbers:** A neutral variant in a population of 100 has ~1% chance of persisting 100 generations by chance alone. Variant persistence is logged as the number of generations from first appearance to loss or to the present. Median persistence per run is reported with the population size.
- **Check:** The persistence distribution is reported per run; a run where every new variant persists is flagged as a logging or survival defect, because chance loss must occur.

**369. The lineage record is the variation record**
- **Rule:** All heritable variation is visible in the lineage record: every genome, every mutation, every recombination, every persistence and loss, linked parent to offspring back to generation 0. The record is the audit trail for every claim about inheritance in this phase. A variant that cannot be found in the record did not happen. The record is append-only: nothing is edited, and corrections are added as new entries.
- **Numbers:** Record completeness: 100% of births linked to a parent, 100% of mutations linked to a birth, for runs up to 10,000 organisms; sampled at 1% above that, rate recorded. Record size grows ~1 KB per organism at cell scale.
- **Check:** A random audit of ≥100 organisms traces each back to generation 0 through the record; the audit passes only if ≥99% of traces are complete with no missing links.

**370. Heritable variation is the phase's deliverable**
- **Rule:** This phase is done when the world can show, with numbers, that variation is created by mutation and recombination, carried by genome copying, expressed through switches and development, and recorded in lineages. Nothing else is smuggled in as inheritance. The deliverable is not a claim but a set of measured rates and a complete record: mutation rates, recombination rates, heritabilities, and the lineage tree that ties them together.
- **Numbers:** Deliverable checklist: per-base mutation rate measured (see 312); recombination rate measured (see 331); heritability measured for ≥3 traits (see 361); lineage record audit ≥99% complete (see 369); zero non-genome inheritance without a named mechanism (see 367). All five must pass across ≥5 seeds.
- **Check:** The checklist is run once per scale and the five numbers recorded together; the phase is not closed until all five pass in the same run set.

### 4.8 Plasticity

**371. Plasticity: one genome, many phenotypes**
- **Rule:** Plasticity is the genome's ability to produce different phenotypes in different conditions, through switches that respond to the environment (see 349). A plastic lineage is one whose measured trait changes with the environment along a recorded curve, the reaction norm. Plasticity is a property of the genome, so it is heritable and can evolve. The reaction norm is the trait that evolves, not the trait value at one condition.
- **Numbers:** Reaction norm measured as the trait value at ≥3 conditions (e.g. food low, medium, high). Plasticity score: the trait range across conditions divided by the trait mean, 0 (no plasticity) to >1 (strong). A score >0.2 is classed as plastic. Norms are logged per lineage per trait.
- **Check:** Reaction norms are measured for ≥3 traits per run across ≥5 seeds; a lineage claimed plastic must show a score >0.2 in at least 4 of 5 seeds.

**372. Acclimation: reversible change within a life**
- **Rule:** Acclimation is plasticity that reverses. An organism moved to a new condition changes its expression and its trait, and moved back, it changes back. Heat tolerance, foraging range, metabolic rate: all can shift within a life without any genome change. Acclimation is bounded: it works within the reaction norm's range and no further, and it costs energy to maintain the changed state.
- **Numbers:** Acclimation range: the trait can shift ±20–50% from its baseline within a life. Acclimation time: 100–1,000 ticks at cell scale. Maintenance cost: +5–10% energy while acclimated. Reversal time equals acclimation time within 20%.
- **Check:** Organisms moved between conditions and back show the trait returning to within 10% of baseline; a trait that does not return is classed as developmental (see 373), not acclimation.

**373. Developmental plasticity: the window that closes**
- **Rule:** Some plastic responses happen only during development and then lock in. The adult keeps the trait it developed, even if conditions change back. A body that grew large in a rich season stays large in a poor one. Developmental plasticity is the organism betting its adult form on its early conditions, and the bet is recorded as the condition during the sensitive window: a window with a start, an end, and a measured effect.
- **Numbers:** Sensitive window: a stated developmental step range (e.g. steps 3–8 of 20). Effect size: the adult trait differs by 10–100% depending on conditions inside the window, and by <5% depending on conditions outside it. Window boundaries are logged per trait.
- **Check:** Organisms exposed to a condition only inside the window show the adult effect; organisms exposed only outside it do not; both results are measured and reported per trait.

**374. Plasticity has a cost**
- **Rule:** Plasticity is not free. The switches, sensors, and regulatory loops that make it possible cost energy to build and maintain, and a plastic organism pays that cost even in conditions where it never uses the flexibility. A lineage in a stable environment can save the cost by losing plasticity. That loss is itself an evolutionary event, recorded when a reaction norm flattens.
- **Numbers:** Plasticity maintenance cost: +5–15% of the energy budget per plastic trait, depending on the number of switches involved. In a stable environment for ≥100 generations, lineages are expected to show a measurable flattening of at least one reaction norm; the flattening is logged when it occurs.
- **Check:** Energy budgets of plastic vs non-plastic sister lineages are compared; the plastic lineage shows the stated extra cost within 20%, and the flattening in stable conditions is reported when observed.

**375. Plasticity has limits**
- **Rule:** No reaction norm stretches forever. Beyond its range, the trait cannot change further, and the organism either copes with what it has or dies. The limit is set by the chemistry: a switch can only turn a gene up so far, a body can only grow so fast. Limits are measured by pushing the condition until the trait stops responding, and the breaking point is logged.
- **Numbers:** Limit measured as the condition value at which the trait response saturates (further change <5% per doubling of the condition). Tested across the full condition range the organism can survive: temperature 0–40 °C, food 0–100 units, light 0–1,000 lux at cell scale. The saturation point is logged per trait.
- **Check:** The saturation point is measured for ≥3 traits per run; a trait with no measured saturation point is flagged as untested, not as unlimited.

**376. Plasticity first, genes later**
- **Rule:** When a population meets a new condition, plasticity responds first. The organisms already carry the switches, so the trait shifts within a life. If the condition persists, genetic change can follow: mutations that make the shifted trait the default, even without the condition, spread because they save the cost of maintaining the switch. The plastic response is therefore a bridge to a genetic one, and the sequence — plastic shift, then genetic fixation — is a prediction to test, not a story to tell.
- **Numbers:** Timeline: plastic shift within 1 generation of the new condition; genetic fixation (the trait present without the condition) measured over 50–500 generations, if it occurs. Fixation is recorded only when ≥90% of the population shows the trait in the old condition. The sequence is tested once per new condition introduced.
- **Check:** For each lasting new condition, the plastic shift is measured in generation 1 and the population is checked for fixation at generation 100 and 500; the result (fixation, partial, none) is recorded with the numbers.

**377. The Baldwin effect, stated as a test**
- **Rule:** Learning and plasticity can guide evolution without Lamarckian inheritance. Organisms that learn or adjust survive in a new niche, and their descendants — who inherit the capacity to learn or adjust, not the learned content — are the ones that later evolve a genetic solution. This is a testable claim: it predicts that a lineage with the learning capacity reaches the genetic solution faster than a lineage without it, in the same new condition.
- **Numbers:** Test: two lineages, identical except for the learning/plasticity capacity, placed in a new condition; the genetic solution is defined in advance (a named trait value without the inducing condition). Time to solution measured in generations; the plastic lineage is predicted to reach it ≥2× faster. Run across ≥5 seeds.
- **Check:** The time-to-solution is reported for both lineages per seed; the Baldwin claim passes only if the plastic lineage is faster in at least 4 of 5 seeds, and the result is recorded either way.

**378. Plasticity buffers the genome**
- **Rule:** Plasticity hides genetic differences. When the environment is harsh, the plastic response moves every organism toward the working phenotype, so genomes that would otherwise fail survive. This buffering means selection sees less genetic variation than is really there. The variation is stored, not removed, and it shows itself when conditions change again. Buffering is measured as the difference between the genetic variance and the expressed phenotypic variance under stress.
- **Numbers:** Buffering measured as the ratio of phenotypic variance to genetic variance for a trait: <1 means buffered (phenotypes vary less than genomes), >1 means amplified. Under a standard stress (food at 20% of normal), the ratio is logged per trait per run; a ratio <0.5 is classed as strong buffering.
- **Check:** The variance ratio is reported per trait under normal and stressed conditions; a trait whose ratio does not fall under stress is classed as unbuffered, and the claim is recorded.

**379. Too much plasticity is a defect**
- **Rule:** A reaction norm that swings wildly — a trait that changes 10× with a small condition change — is not adaptability, it is instability. The organism cannot hold a working state. Over-plasticity is a failure mode of the switch system, usually a broken regulator or a loop with too much gain, and it is logged as a defect when it appears. The healthy range for a reaction norm is a measured band, not an open end.
- **Numbers:** Instability threshold: a trait range across conditions >3× the trait mean, or a trait that flips between two states with no middle, is classed as unstable. Instability is counted per lineage per run; a lineage with >3 unstable traits is flagged. The regulator or loop behind each unstable trait is identified where possible.
- **Check:** The unstable-trait count is reported per run; a run where >10% of lineages are unstable triggers a review of the switch and regulator rules.

**380. Plasticity is recorded as a norm, not a story**
- **Rule:** Every claim about plasticity is backed by a reaction norm: the trait measured at ≥3 conditions, with the sample size, the noise, and the cost recorded alongside. A lineage is plastic for a trait only if the norm shows it; a lineage is not plastic because it once changed. The norms are stored with the lineage record, so the plasticity of any ancestor can be looked up and compared to its descendants.
- **Numbers:** Norm completeness: ≥3 conditions, ≥20 organisms per condition, noise reported as the standard deviation per condition. Norms are stored per lineage per trait per generation window (every 100 generations). Missing norms are flagged as gaps, not filled in by interpolation.
- **Check:** A random audit of ≥50 plasticity claims re-derives each norm from the stored measurements; the audit passes only if ≥95% of claims match their norms within the stated noise.

### 4.9 Mutation rates

**381. The mutation rate ladder by scale**
- **Rule:** Mutation rate falls as genomes grow. A long genome at a high per-base rate would collect too many damaging changes per generation to survive. The ladder is a trade-off, not a decree: small genomes tolerate high rates, large genomes need low ones, and each scale's rate is a starting value to be challenged by measurement. The rate is a property of the organism's copying chemistry, encoded in its genome.
- **Numbers:** Per-base per-generation rate: protocell 2 × 10⁻² (validated); simple cell 1 × 10⁻⁶; complex cell 1 × 10⁻⁷; small animal 1 × 10⁻⁸; human 1 × 10⁻⁸. Mutations per genome per generation: protocell ~0.5, cell ~0.01, human ~60 (3.2 billion bases × 1 × 10⁻⁸ ≈ 32 per copy, ~64 per birth from two parents).
- **Check:** The measured per-genome mutation count per scale matches the ladder within a factor of 3 across ≥5 seeds; a scale off by more than that has its copying chemistry reviewed.

**382. The error threshold: too much mutation kills inheritance**
- **Rule:** There is a ceiling on the mutation rate. Above it, a genome cannot be copied faithfully enough for its information to survive. Each generation loses more than selection can restore, and the lineage melts into noise. The threshold is set by the genome length and the fraction of mutations that are harmful: roughly, the rate must stay below one harmful mutation per genome per generation.
- **Numbers:** Threshold ≈ 1 / (genome length × harmful fraction). For a 10,000-base genome with 25% harmful mutations, the threshold is ~4 × 10⁻⁴ per base per generation. A lineage run at 2× its threshold is predicted to lose its most complex trait within 50 generations; the prediction is tested, not assumed.
- **Check:** A lineage held above its computed threshold is measured for trait loss over 50 generations; if the trait holds, the threshold formula is revised with the numbers, not defended.

**383. Drake's rule: mutations per genome stay roughly constant**
- **Rule:** Across real life, the number of mutations per genome per generation stays within a narrow band: roughly 0.1 to 1 for microbes, tens for large animals. Genome sizes span six orders of magnitude, yet the per-genome count stays near constant because the per-base rate falls as genomes grow. Genesis adopts this as a starting rule and a check: a scale whose per-genome count is far outside the band has a copying chemistry worth questioning.
- **Numbers:** Target band: 0.01–1 mutations per genome per generation at cell scale; 10–100 at human scale. The band is a check, not a law: a scale outside it is flagged and investigated, and the investigation's result is recorded either way.
- **Check:** Per-genome mutation counts are reported per scale per run; any scale outside its band is listed with the investigation's finding, and the band itself is revised only with measured evidence.

**384. The rate itself can evolve**
- **Rule:** Mutation rate is a trait. Genes that code for proofreading, repair, and copying fidelity set it, and mutations in those genes change it. A lineage can evolve toward a higher rate (more variation, more damage) or a lower one (safer copies, slower change). The rate is therefore not a global constant: it is a measured value per lineage, logged per generation, and it drifts like any other trait.
- **Numbers:** Rate changes by mutation in fidelity genes at the point-mutation rate; a single breaking mutation in a proofreading gene raises the rate 10–100×. The rate per lineage is logged per generation; rate changes >2× are flagged as events with the gene identified.
- **Check:** The rate distribution across lineages is reported per run; at least two lineages differing in rate by ≥10× are recorded before any claim about rate evolution is made.

**385. Mutator strains: high rate as a strategy**
- **Rule:** A lineage with a broken proofreading gene — a mutator — produces far more variation than its neighbours. In a changing environment that variation can be worth the damage: one of its many mutants may fit the new conditions. Mutators are a gamble, not a design. Most mutator lineages die from their own error load, and the rare winner is recorded as a winner, not as proof that mutators are good.
- **Numbers:** Mutator rate: 10–100× the lineage baseline. Mutator frequency in a stable population: <1% of lineages. In a newly changed environment, mutator lineages are predicted to produce the first fitting mutant ≥2× faster; the prediction is tested once per new condition introduced.
- **Check:** Mutator frequency and the time-to-first-fitting-mutant are reported per run; a run where mutators dominate a stable population is flagged, because the error load should prevent it.

**386. Stress raises the mutation rate**
- **Rule:** Some organisms raise their mutation rate when stressed — starving, heated, damaged — by switching off repair or by activating error-prone copying. The logic is the same gamble as mutators: when the current genome is failing, more variation is worth more than fidelity. Stress-induced mutation is a gene-encoded response with a trigger, a magnitude, and a cost, and it switches off when the stress passes.
- **Numbers:** Stress induction: rate rises 10–100× while the stress signal is above threshold (energy <20% of maximum, or temperature >35 °C). The rise reverses within 100 ticks of the stress ending. Direction stays random: the occurrence–usefulness correlation under stress is measured and must stay within ±0.05 of zero.
- **Check:** Rates under stress vs calm are measured per lineage and reported; a lineage whose rate does not rise under stress is classed as non-inducible, and the correlation check from 329 is repeated under stress.

**387. The rate floor: too low stalls change**
- **Rule:** A mutation rate can also be too low. A lineage that copies almost perfectly barely changes, and when conditions shift it has nothing to work with: no standing variation, no new mutants, only plasticity to carry it. The floor is set by the need for change: a lineage must produce enough new variants per generation that a fitting one appears within the time the environment allows.
- **Numbers:** Floor estimate: ≥0.001 new mutations per genome per generation at cell scale (one new mutation per 1,000 births). A lineage below the floor for >500 generations in a changing environment is predicted to go extinct or stall; the prediction is tested when such a lineage is observed.
- **Check:** Lineages below the floor are counted per run; their extinction or stalling rate is compared to lineages above the floor, and the comparison is reported with the numbers.

**388. Measuring the rate: parent against offspring**
- **Rule:** The mutation rate is measured one way only: compare parent genomes to offspring genomes, count the differences, divide by the bases copied. No indirect estimate — no trait change, no diversity guess — substitutes for this count. The measurement needs enough births to be precise, so it is reported with its sample size and its confidence interval. A rate quoted without either is incomplete.
- **Numbers:** Minimum sample: 1,000 parent–offspring pairs per rate estimate at cell scale (100 at human scale, where genomes are long). Confidence interval reported at 95%. Sampling is random across the population, not taken from the most variable lineages.
- **Check:** Rate estimates are recomputed from the stored genome pairs in a random audit; the audit passes only if the recomputed rate matches within 10%.

**389. Rate differences between lineages are real data**
- **Rule:** Different lineages in the same run can have different mutation rates, and that difference is data. It shows the rate evolving, or a mutator appearing, or stress hitting one niche and not another. Rate is therefore reported per lineage, not as one global number for the run. A single global rate is a summary for the record, and it is always accompanied by the spread across lineages.
- **Numbers:** Per-lineage rate reported as the median and the range across lineages per run. A range spanning >10× is classed as wide and the lineages at each end are identified with their fidelity genes recorded. Global rate is the population-weighted mean.
- **Check:** The per-lineage rate spread is reported per run; a run reporting only a global rate is flagged as incomplete until the spread is added.

**390. Rate settings are proposed, reviewed, and recorded**
- **Rule:** Every mutation rate in this phase starts as a proposed value, is reviewed before it is used, and is recorded with the proposal, the review, and the measurement that follows. If measurement disagrees with the proposal, the measurement wins and the rate is changed in the record with a reason. No rate is ever silently tuned to make a result look better: a tuned rate is a changed experiment, and it is logged as one.
- **Numbers:** Proposal and review are recorded per rate per scale, with the date. Freebuff proposes starting rates and changes; Muse reviews them. A rate change after measurement is logged with the old value, the new value, the measured evidence, and the date.
- **Check:** The rate log is audited once per scale: every rate in use traces to a proposal, a review, and a measurement; any rate without that chain is flagged and its runs marked provisional.

### 4.10 The genome is honest

**391. No hidden information in the genome**
- **Rule:** The genome contains exactly what the lineage record says it contains. No hidden fields, no owner-written notes, no secret instructions that the organism's chemistry cannot read. If a base matters, it is in the sequence and visible to any audit; if it is not in the sequence, it does not affect the organism. This is the rule that keeps the genome honest: the world cannot cheat by hiding information where the inhabitants cannot, in principle, find it.
- **Numbers:** Genome audit: 100% of the genome's effect on the organism must be traceable to its sequence through the fixed genotype–phenotype map (see 307). Any effect without a sequence trace is a defect, logged with the seed and tick. Audit sample: ≥100 organisms per run.
- **Check:** The audit is run once per scale and the result recorded; a single untraceable effect fails the audit and blocks the phase sign-off until it is explained or fixed.

**392. The genome is fully readable by the owner and the inhabitant**
- **Rule:** The genome is readable in full: by the owner, for audit, and in principle by the inhabitants, should they ever develop the science to read it. There is no encrypted or compressed region, no part that only the simulation can see. Readability is what makes the Discovery Principle real at the genome level: an inhabitant that learns to sequence DNA finds the same genome the owner sees, with nothing extra and nothing withheld.
- **Numbers:** Read access: the full sequence is available through the lineage record and, when the Gateway contract extends to it, through the read-only feed. Read cost: zero to the world — reading never changes the genome. Format: the 4-symbol string with gene markers, as stored.
- **Check:** A genome fetched through the record matches the genome used by the simulation bit-for-bit in a random audit of ≥100 organisms; any mismatch is a defect.

**393. Genome provenance: every base has a history**
- **Rule:** Every base in every genome has a provenance: inherited unchanged from the parent, changed by a logged mutation, arrived by a logged recombination, or created by a logged duplication or insertion. There are no bases with no history. A base that appears without a provenance entry is a placed base, and placed bases are forbidden. Provenance is the genome-level version of the rule that nothing is placed in the world.
- **Numbers:** Provenance coverage target: 100% of bases in runs up to 10,000 organisms; sampled at 1% above that, rate recorded. Provenance fields per base block: source (inheritance, mutation, recombination, duplication, insertion), event id, generation. A base with no provenance is a 0-tolerance anomaly.
- **Check:** A random audit of ≥1,000 base blocks verifies provenance against the event log; the audit passes only if ≥99% of blocks have a matching event.

**394. The genome log is append-only**
- **Rule:** The genome record — every genome, every change, every event — is append-only. Nothing is edited, nothing is deleted, nothing is rewritten to make the past look tidier. If a recording error is found, the correction is a new entry that names the error and the corrected value, and both entries stay. History is the record of what happened, and the record is what makes the world's history trustworthy.
- **Numbers:** Log entries carry a sequence number, a tick, and a checksum chaining to the previous entry. A break in the chain is a 0-tolerance defect. Corrections are <1% of entries in a healthy run; a higher rate triggers a review of the logging code.
- **Check:** The checksum chain is verified once per run; a break is reported with the entry number, and the run is marked provisional until the break is explained.

**395. No placed genes, ever**
- **Rule:** No gene is written into a genome by the owner, by the experimenter, or by any process outside the recorded mechanisms of this phase: mutation, duplication, recombination, transfer. A gene that appears in a genome must have a parent, a mutation event, or a transfer event behind it. This is the genome-level statement of the Discovery Principle: genes are discovered by evolution, not installed.
- **Numbers:** Placed-gene count target: 0 in every run. The check is the provenance audit (see 393) plus a scan for any gene whose first appearance has no event. Any gene failing the scan is reported with its sequence, its first appearance, and the run is flagged.
- **Check:** The placed-gene scan is run once per run and the count (target 0) is recorded; a count above 0 is a failed run, reported as such, not worked around.

**396. The genome against the protocell criterion**
- **Rule:** The genome mechanism in this phase must satisfy the protocell life criterion where it applies: origin without placement, self-sustaining replication, compartmentalised individuality, metabolism, heritable variation, and selection. All six were measured 3/3 with clean controls, as validated on 2026-11-06. The criterion is the origin-of-life bar, and this phase's genome is what carries the organism past it: the strand that copies with a 2% per-base mutation rate, inside a vesicle that divides, is the genome at its smallest.
- **Numbers:** Protocell bar carried forward: first catalyst by ligation (validated at ticks 265/289/282), first copy at 353/330/285, generation 67/67/69, mutant persistence ≥1,000 ticks. The genome mechanism at cell scale and above must show the same six properties in its own terms, measured per scale.
- **Check:** The six properties are re-verified once per scale above protocell, with the numbers recorded; a scale that fails any of the six is not carried forward until the failure is understood.

**397. The genome is the same mechanism at every scale**
- **Rule:** The genome is one mechanism, not one per scale. The same rules — copy, mutate, recombine, express, develop — run from the protocell strand to the human chromosome set, with parameters changing by scale and the machinery growing more elaborate. A result proved at one scale must be re-proved at the next, because the parameters change, but the mechanism is never replaced by a different one. This is what makes the arc from cells to humans one story instead of a series of separate tricks.
- **Numbers:** Mechanism identity is checked per scale: the same copy, mutation, recombination, expression, and development rules are in force, with the scale's parameter values recorded. Parameter values per scale are listed in the scale record (see 305, 312, 381). A scale using a different rule is flagged as a fork, not a continuation.
- **Check:** The per-scale rule checklist is run once per scale and recorded; a scale that fails the checklist is not merged into the arc until it passes.

**398. The genome in the viewer: honest display**
- **Rule:** When the genome is shown — in the Command Center, the World View, or any future display — it is shown as it is: the real sequence, the real lineage, the real rates, with the scale and the magnification stated. A genome display never invents a gene, never smooths a mutation, and never shows a representative genome as if it were the organism's own. What the viewer sees is what the record holds, through the read-only Gateway feed.
- **Numbers:** Display labels state the organism id, the genome length, the generation, and the data source (live record or archive). Magnification or sampling is stated wherever the display cannot show the full sequence. No fabricated genome metric is displayed; every displayed number traces to the record.
- **Check:** A display audit compares ≥10 displayed genomes against the record; the audit passes only if all match exactly, including the labels.

**399. The genome record outlives the organism**
- **Rule:** When an organism dies, its genome stays in the record: in its offspring, in its lineage, and in the archive. Death is permanent for the organism, but the genome's history is not erased. The lineage tree keeps the dead, the extinct, and the failed, because they are the evidence of what evolution tried. A world that deletes the dead cannot learn from them, and neither can we.
- **Numbers:** Archive retention: 100% of genomes in runs up to 10,000 organisms; sampled at 1% above that, rate recorded. Dead lineages remain queryable by genome id and by generation. Archive size grows ~1 KB per organism at cell scale.
- **Check:** A query for a dead organism's genome returns it in ≥99% of sampled cases; a missing genome is a defect, logged with the organism id.

**400. Phase 4 closes on the record**
- **Rule:** Phase 4 is done when the genome mechanism is built, measured, and recorded at every scale it applies to: the genome defined, copying faithful and costed, mutation typed and rated, recombination shuffling, expression switching, development building bodies, variation heritable, plasticity normed, rates laddered. Every claim is backed by a number in the record. The phase closes with a sign-off on that record, not on a summary of it.
- **Numbers:** Close-out checklist: topics 301–400 each carry a measured Check; mutation and recombination rates measured per scale; heritability measured for ≥3 traits; lineage audit ≥99% complete; placed-gene count 0; protocell bar re-verified per scale. All items pass across ≥5 seeds before sign-off.
- **Check:** The checklist is run once and the results recorded with the date; the phase closes only when every item passes, and the closing decision is recorded with what the world is now ready for.

## Phase 5 — Evolution rulebook: selection and drift

### 5.1 Fitness

**401. What fitness is**
- **Rule:** Fitness is a measured difference in who leaves offspring, nothing more. It is the number of surviving, reproducing descendants an organism leaves, counted in its own place and time. It is not strength, speed, size, beauty, intelligence, or worth.
- **Numbers:** Count offspring that reach reproductive age per parent, over at least 3 generations and at least 5 seeds. Baseline: the population mean is fitness 1.0; report every lineage as a ratio to that mean, to 2 decimal places.
- **Check:** Two lineages in the same patch differ in descendant counts by at least 10% over 3 generations, with the difference reproduced in 4 of 5 seeds; otherwise no fitness claim is made.
**402. What fitness is not**
- **Rule:** Fitness is not a property of a body alone, and it is not a goal the organism pursues. The same trait can be fit in one patch and fatal in the next, fit in a wet season and useless in a dry one. Calling a fast or large organism "fitter" without counting its offspring is a story, not a measurement.
- **Numbers:** The same trait must be scored separately in at least 3 different patches or conditions, with at least 50 individuals per patch per condition.
- **Check:** A trait that wins in one patch and loses in another is recorded as locally fit, never as generally fit; any claim of general fitness without 3-patch data is rejected in review.
**403. Absolute fitness**
- **Rule:** Absolute fitness is the raw count: how many reproducing offspring one organism leaves. It answers whether a lineage is growing, holding, or shrinking in its own patch. It depends on the patch — food, space, hazards, neighbours — so the same genome can have high absolute fitness in a rich patch and zero in a poor one.
- **Numbers:** Report mean offspring per parent per generation, plus the fraction of parents leaving zero reproducing offspring. Track for at least 10 generations; a lineage with mean below 1.0 for 5 consecutive generations is recorded as declining.
- **Check:** The population census matches the summed offspring counts within 1%; a lineage declared growing shows mean above 1.0 in 4 of 5 seeds.
**404. Relative fitness**
- **Rule:** Relative fitness compares lineages sharing a patch: one lineage's offspring count divided by the population mean in that same patch, same generation. It strips out patch richness, so a lineage can be relatively fit even while the whole population shrinks.
- **Numbers:** Relative fitness is reported per lineage per generation, mean 1.0 by definition, range 0 to at least 3.0 in a diverse population. Compare lineages with at least 20 parents each; smaller samples are reported as unreliable.
- **Check:** The lineage ranked highest by relative fitness increases its share of the next generation's parents in 4 of 5 seeds; if it does not, the ranking is re-examined, not trusted.
**405. Lifetime reproductive success**
- **Rule:** Lifetime reproductive success counts every reproducing offspring an organism leaves over its whole life, not just one season. A short-lived organism that breeds early and often can beat a long-lived one that breeds late, and a late breeder that survives a bad year can beat both.
- **Numbers:** Record age at first reproduction in ticks, births per event, and total reproducing offspring per lifetime, for at least 100 individuals per lineage. Median lifespan and median lifetime offspring are reported side by side.
- **Check:** The lineage with the higher median lifetime offspring count holds or grows its population share over 5 generations in 4 of 5 seeds; a claim based on one season only is rejected.
**406. Fitness is measured after the fact**
- **Rule:** Fitness can only be counted once offspring have survived to breed; it cannot be predicted from a body, a gene, or a behaviour before the count is in. A trait that looks useful may produce no offspring, and a trait that looks useless may spread.
- **Numbers:** No fitness value is recorded before offspring reach reproductive age. Provisional scores are labelled provisional and expire after 1 generation; final scores use at least 3 generations of descendant data.
- **Check:** At least 1 in 5 provisional fitness rankings reverses or vanishes when the final 3-generation count arrives; if no ranking ever reverses, the measurement is suspected of being scripted and is audited.
**407. Fitness components**
- **Rule:** Fitness breaks into components — survival to breeding age, mating or reproduction success, number of offspring per event, and offspring survival — and each component can move on its own. A lineage can win by surviving longer, by breeding more often, by having more offspring per birth, or by having tougher offspring.
- **Numbers:** Report each component per lineage: survival to breeding age as a fraction (0–1), breeding events per lifetime, offspring per event, offspring survival to breeding age as a fraction.
- **Check:** The lineage with the highest total fitness shows an advantage in at least one named component, with the component and its size stated; a total with no component behind it is treated as an error.
**408. Fitness trade-offs inside one body**
- **Rule:** A body cannot spend the same energy twice. Energy spent growing cannot be spent breeding, and energy spent on defence cannot be spent on speed. A trait that raises one fitness component usually lowers another, so the net effect is what counts.
- **Numbers:** Energy budgets are recorded in the same units for growth, movement, defence, and reproduction.
- **Check:** The net descendant ratio decides: a trait is recorded as fit only if total reproducing offspring rise by at least 5% over 3 generations, in 4 of 5 seeds, after all component costs are counted.
**409. Fitness of a lineage, not a single organism**
- **Rule:** One lucky organism proves nothing; fitness belongs to lineages, counted over many individuals and several generations. A single organism can leave many offspring by chance — the right patch, the right moment — while its siblings leave none.
- **Numbers:** Lineage fitness uses at least 20 parents per lineage per generation, over at least 5 generations. Single-organism outliers are reported as anecdotes, never as lineage fitness.
- **Check:** A lineage's relative fitness stays above 1.0 for 3 consecutive generations in 4 of 5 seeds before it is called fit; a one-generation spike is recorded as noise.
**410. Fitness changes when the world changes**
- **Rule:** Fitness is a contract between a lineage and its current conditions, and conditions change. A drought, a new predator, a depleted patch, or a new neighbour can reverse every ranking overnight. Lineages do not become unfit because they changed; the world changed around them.
- **Numbers:** Fitness is re-measured after any change in food inflow of 20% or more, any new predator or competitor, or any temperature shift of 5°C or more. Old values are kept in the record with their conditions, never overwritten.
- **Check:** After a recorded environmental change, at least 1 in 10 lineage rankings changes by more than 10% within 3 generations; if rankings never change when the world does, the fitness measure is audited as insensitive.
### 5.2 Natural selection

**411. Selection is differential reproduction**
- **Rule:** Natural selection is the name for a measured difference in who leaves offspring, caused by the environment, not by any chooser. Organisms that survive and breed more in their patch leave more copies of their traits behind; organisms that survive and breed less leave fewer.
- **Numbers:** Selection is reported as a selection coefficient: the relative fitness gap between trait carriers and non-carriers, from 0 (no difference) to 1 (carriers leave no offspring). Measure over at least 3 generations, at least 5 seeds.
- **Check:** A trait's frequency rises by at least 5 percentage points over 3 generations where its coefficient exceeds 0.1, in 4 of 5 seeds; a claimed selection with no frequency change is rejected.
**412. Selection needs variation**
- **Rule:** Selection can only act on differences that already exist. If every organism in a patch carries the same trait, selection cannot favour one over another, and nothing changes no matter how harsh the conditions. Variation comes from mutation and recombination in earlier phases; selection sorts it, it does not create it.
- **Numbers:** Trait variance is reported per generation (standard deviation and range) for each trait under selection. Selection is only claimed where the starting variance is above zero and at least 20 individuals carry each variant.
- **Check:** In a control population with variance forced to zero, trait frequencies do not change over 5 generations; if they do, the change is drift or error, not selection, and is reclassified.
**413. Selection needs heritability**
- **Rule:** Selection changes a population only if the favoured trait is passed to offspring. If a trait is acquired during life — a scar, a learned habit, a full belly — and is not inherited, its bearers may thrive and die without the population changing at all.
- **Numbers:** Heritability is estimated as the parent-offspring regression slope for the trait, 0 to 1, from at least 100 parent-offspring pairs. A trait with slope below 0.1 is recorded as effectively non-heritable for selection purposes.
- **Check:** The observed change in trait mean per generation matches the predicted change (selection difference times heritability) within 25%, in 4 of 5 seeds; a larger gap triggers a re-measurement of heritability.
**414. Directional selection**
- **Rule:** Directional selection pushes a trait in one direction: bigger, smaller, faster, slower, earlier, later. It happens when one end of the trait range leaves more offspring than the other end, generation after generation.
- **Numbers:** Report the trait mean shift per generation in trait units, plus the selection differential (mean of breeders minus mean of the whole population). Starting values: a shift of at least 0.1 standard deviations per generation sustained over 5 generations counts as directional.
- **Check:** The trait mean moves at least 0.5 standard deviations over 5 generations in the predicted direction, in 4 of 5 seeds; movement in the opposite direction falsifies the claimed direction.
**415. Stabilising selection**
- **Rule:** Stabilising selection favours the middle and trims both extremes. It happens when the average trait value leaves the most offspring and both extremes pay a cost — too small and you are eaten, too large and you starve, too early and you freeze, too late and you miss the food.
- **Numbers:** Report trait variance before and after: a variance fall of at least 20% over 5 generations with a mean shift under 0.1 standard deviations counts as stabilising. Extreme carriers (beyond 2 standard deviations) must show relative fitness below 0.8.
- **Check:** Variance falls by at least 20% while the mean stays within 0.1 standard deviations, in 4 of 5 seeds; a falling variance with a moving mean is reclassified as directional.
**416. Disruptive selection**
- **Rule:** Disruptive selection favours both extremes and penalises the middle. It happens when the middle way works nowhere — two food sources with nothing between them, two hiding places with open ground in between — so organisms at either end leave more offspring than generalists in the middle.
- **Numbers:** Report the trait distribution shape per generation: a single peak splitting into two peaks separated by at least 1 standard deviation, with the middle (within 0.5 standard deviations of the old mean) showing relative fitness below 0.8.
- **Check:** The distribution is measurably bimodal (two peaks, valley at least 20% below the lower peak) in 4 of 5 seeds; a single peak with wide spread is recorded as variation, not disruption.
**417. Selection on a threshold**
- **Rule:** Some traits matter only past a threshold: big enough to crack a shell, fast enough to escape, tough enough to survive a cold night. Below the threshold the trait buys nothing; above it, survival jumps.
- **Numbers:** The threshold value is recorded in trait units with the survival rate below it (under 20% to breeding age) and above it (over 60%). The trait value at which survival first exceeds 50% is the measured threshold, to 2 significant figures.
- **Check:** Survival to breeding age jumps by at least 30 percentage points across the measured threshold, in 4 of 5 seeds; a smooth rise with no jump means no threshold exists and the claim is withdrawn.
**418. Selection through survival versus through reproduction**
- **Rule:** Selection can work by killing the unfit before they breed, or by letting them live but breed less. The two routes leave different fingerprints: survival selection shows up as a death-rate gap, reproduction selection as a birth-rate gap among survivors.
- **Numbers:** Report the death-rate gap and the birth-rate gap separately per trait, each as a ratio between carriers and non-carriers. A gap of 20% or more in either route counts as selection through that route.
- **Check:** The named route accounts for at least 70% of the trait's frequency change over 3 generations, by arithmetic from the two gaps; if neither gap explains the change, the change is not selection.
**419. Soft versus hard selection**
- **Rule:** Hard selection kills or sterilises outright: the trait either works or the organism leaves no offspring, whatever the neighbours do. Soft selection is relative: the trait matters only against the local competition, so the same trait can win in a crowded patch and be irrelevant in an empty one.
- **Numbers:** Hard selection is recorded where carrier survival to breeding age is below 10% regardless of local density, across densities from 10 to 100 individuals per patch.
- **Check:** The hard/soft label predicts the outcome of a density change: halving density removes a soft advantage but leaves a hard one, tested in 4 of 5 seeds; a label that predicts wrong is corrected in the record.
**420. Selection is slow unless the pressure is strong**
- **Rule:** A small fitness advantage moves a trait slowly. A 1% advantage takes many generations to show up in frequencies, and drift can swamp it entirely in a small population. A 50% advantage moves fast and visibly.
- **Numbers:** A selection coefficient of 0.01 is expected to need at least 50 generations for a 10-point frequency shift; a coefficient of 0.5 needs about 5. Report the coefficient, the generations observed, and the frequency shift together, always.
- **Check:** The observed frequency shift matches the shift predicted from the measured coefficient within 30% over the observed generations, in 4 of 5 seeds; a shift far larger than the coefficient predicts is investigated as drift or measurement error.
### 5.3 Sexual selection

**421. What sexual selection is**
- **Rule:** Sexual selection is selection through mating success: traits spread because their bearers mate more, not because they survive better. It is still natural selection in the broad sense — the currency is still offspring — but the filter is a mate, not the weather or a predator.
- **Numbers:** Report mating success (matings per individual per season) separately from survival to breeding age, for at least 50 individuals of each sex or mating type per lineage.
- **Check:** Carriers show higher mating success and lower or equal survival, yet higher total offspring, in 4 of 5 seeds; if carriers also survive better, the trait is recorded as naturally selected, not sexually selected.
**422. Mate choice**
- **Rule:** Mate choice is selection by preference: one sex (or mating type) prefers certain traits in a partner, and preferred partners leave more offspring. The preference itself is a trait that can evolve, and the chosen trait can grow extreme because each generation's choosers prefer the most extreme carriers of the last generation.
- **Numbers:** Choice is measured as the mating rate with preferred versus non-preferred partners: at least a 2-to-1 ratio in controlled encounters of 20 or more per type.
- **Check:** Removing the preferred trait (or blinding the sense that perceives it) cuts the carrier mating advantage by at least half, in 4 of 5 seeds; if the advantage survives, choice is not the mechanism.
**423. Competition for mates**
- **Rule:** Competition for mates is selection by contest: rivals fight, display, chase, or block each other, and winners mate more. The winning traits — size, strength, speed, persistence, timing — spread because winners breed, not because the trait helps against predators or hunger.
- **Numbers:** Record contests per season (at least 30 observed), win rate by trait value, and matings per winner versus per loser. Winners must mate at least twice as often as losers for competition to be the claimed mechanism.
- **Check:** The trait value of winners exceeds that of losers by at least 0.5 standard deviations, and winners' offspring counts exceed losers' by at least 50%, in 4 of 5 seeds.
**424. Costly signals**
- **Rule:** A costly signal is a trait that is expensive to carry — bright, loud, large, slow — and therefore honest: only an organism in good condition can afford it. Mates prefer it precisely because it cannot be faked cheaply.
- **Numbers:** Signal cost is measured as the survival or energy penalty for carriers: at least a 10% survival drop or 10% energy cost versus non-carriers, with a mating gain of at least 30%. The correlation between signal size and body condition must exceed 0.5.
- **Check:** Weakening the signal's cost (for example by rich food) weakens the chooser preference within 2 generations, in 4 of 5 seeds; a preference that survives a free signal is recorded as a habit, not a costly-signal choice.
**425. Runaway selection**
- **Rule:** Runaway selection is a feedback loop: choosers prefer a trait, the trait grows, choosers prefer the larger trait even more, and the trait grows again. It stops only when the survival cost of the trait finally outweighs the mating gain, or when choosers stop preferring the extreme.
- **Numbers:** Track trait mean and chooser preference strength per generation over at least 10 generations. Runaway is recorded where the trait mean rises at least 0.2 standard deviations per generation for 5 consecutive generations while survival of carriers falls.
- **Check:** The trait stops growing (mean shift under 0.05 standard deviations per generation for 3 generations) at the point where the mating gain first equals the survival cost, within measurement error, in 4 of 5 seeds.
**426. Sexual dimorphism**
- **Rule:** Sexual dimorphism is the measurable difference between mating types in size, shape, colour, or behaviour, produced when selection pressures differ between them. One type may be selected for contest, the other for choice, or one for survival and the other for display.
- **Numbers:** Dimorphism is reported as the difference in trait means between mating types, in standard deviations, per trait, with at least 30 individuals per type. A difference above 0.5 standard deviations counts as dimorphic for that trait.
- **Check:** The dimorphism index for a trait tracks the difference in selection coefficients between the mating types (correlation above 0.7 across traits); a dimorphic trait with equal selection on both types is investigated as a measurement artefact.
**427. Sexual conflict**
- **Rule:** Sexual conflict is selection pulling the two mating types in opposite directions over the same trait or behaviour. What helps one type mate can harm the other — a mating that costs the partner time, energy, or survival.
- **Numbers:** Measure the fitness effect of a mating on each partner separately: offspring gained by one type and offspring lost by the other, per mating, over at least 50 matings. Conflict is recorded where one partner gains at least 10% while the other loses at least 10%.
- **Check:** A defence trait in the harmed type spreads (frequency rise of at least 10 points over 5 generations) after the harmful trait spreads, in 4 of 5 seeds; no counter-move means no conflict is claimed.
**428. Alternative mating strategies**
- **Rule:** Alternative mating strategies are different ways of getting matings within one population: contest winners, sneaks, mimics, helpers, satellites. They persist when each strategy wins in some conditions and loses in others, so no single strategy takes over.
- **Numbers:** Record at least 2 strategies per population, each used by at least 10% of the mating type, with matings per strategy per season and the conditions where each wins. Frequencies are tracked per generation for at least 10 generations.
- **Check:** The payoff per strategy (matings per individual) differs by under 10% between strategies at equilibrium, in 4 of 5 seeds; a strategy paying 20% more for 3 generations is predicted to grow, and the prediction is tested.
**429. Sexual selection in hermaphrodites and asexuals**
- **Rule:** Sexual selection needs mating, but mating does not need two sexes. Hermaphrodites can choose partners and compete for the chance to be the sperm donor, the egg donor, or both, and the same logic applies: traits that win matings spread even at a survival cost.
- **Numbers:** In hermaphrodite populations, record matings per individual in each role (donor and recipient) separately, at least 30 individuals per role. Asexual lineages are checked for zero mating events over a full run before sexual selection is ruled out.
- **Check:** A trait that spreads in a hermaphrodite population is tied to the role in which it wins matings (donor or recipient), with the mating-rate gap stated; in asexual controls the same trait shows no mating-rate gap.
**430. Sexual selection versus survival: the net count**
- **Rule:** A sexually selected trait is judged by the net offspring count, never by mating success alone. A trait that doubles matings but halves survival to breeding age may leave the same number of offspring, or fewer. The mating gain and the survival cost are measured in the same currency — reproducing offspring — and the trait is fit only if the net is positive.
- **Numbers:** Report mating gain (percentage more matings) and survival cost (percentage fewer survivors) side by side, then the net reproducing-offspring ratio.
- **Check:** The net ratio predicts the trait's frequency change within 25% over 3 generations, in 4 of 5 seeds; a trait with high mating success and a falling frequency is recorded as a net loss, not a sexual-selection success.
### 5.4 Drift

**431. What genetic drift is**
- **Rule:** Genetic drift is change in trait frequencies by chance alone. In any finite population, some organisms leave more offspring by luck — the right patch, the right moment, a predator looking the other way — and their traits become more common for no reason at all. Drift needs no advantage, no disadvantage, and no environment; it needs only finite numbers and time.
- **Numbers:** Drift strength scales with 1 over twice the effective population size.
- **Check:** A neutral trait (measured selection coefficient under 0.02) changes frequency by at least 5 points over 10 generations in small populations (under 50) in 4 of 5 seeds; the change is labelled drift, never selection.
**432. Drift is strongest in small populations**
- **Rule:** The smaller the population, the louder chance speaks. In a population of ten, one lucky birth can shift a trait by a tenth of the population; in a population of ten thousand, the same birth is noise.
- **Numbers:** Report effective population size and the per-generation frequency change of neutral traits at sizes 10, 50, 200, and 1,000. The observed change must shrink as size grows, roughly in proportion to 1 over the square root of size.
- **Check:** Neutral-trait frequency change at size 10 exceeds the change at size 1,000 by at least 5 times, in 4 of 5 seeds; if small and large populations change equally, the change is not drift.
**433. Drift versus selection: the boundary**
- **Rule:** Selection beats drift only when the fitness advantage is large compared with chance. A trait with a 1% advantage in a population of 20 is mostly drift; the same trait in a population of 20,000 is mostly selection. The boundary is roughly where the selection coefficient exceeds 1 over twice the effective population size.
- **Numbers:** For every selection claim, report the coefficient and the effective population size together, and the ratio of the two.
- **Check:** Traits below the boundary show frequency changes indistinguishable from neutral-trait changes (within 20%) in 4 of 5 seeds; traits above the boundary move in the predicted direction, and the split is recorded.
**434. Founder effects**
- **Rule:** A founder effect is drift with a starting point: a small group founds a new patch, carrying only a sample of the parent population's traits. Whatever that sample happened to contain — common traits, rare traits, missing traits — becomes the new population's starting point, and its descendants inherit the accident.
- **Numbers:** Founding groups are 2 to 20 individuals; record the trait frequencies of founders versus the parent population, and the frequencies after 10 generations in the new patch.
- **Check:** The new patch's trait frequencies after 10 generations are closer to the founders' frequencies than to the parent population's, in 4 of 5 seeds; if they converge back to the parent's, gene flow or selection, not the founder effect, is at work.
**435. Bottlenecks**
- **Rule:** A bottleneck is a sharp, temporary crash in population size — a bad season, a disease, a patch drying out — after which the survivors rebuild. The survivors carry only a sample of the old variation, so rare traits can vanish in one crash and common traits can become universal, purely by who happened to live.
- **Numbers:** A bottleneck is a fall to under 10% of the previous population for at least 1 generation, then recovery to at least 50%.
- **Check:** At least 1 in 5 traits present before the crash (frequency above 5%) is absent after recovery, in 4 of 5 seeds; a crash with no trait loss is recorded as a census dip, not a genetic bottleneck.
**436. Fixation by drift**
- **Rule:** Fixation is a trait reaching 100% of a population — every organism carries it — and drift alone can do it. In a small population, chance can push a neutral or even slightly harmful trait to fixation while a useful trait is lost, because no force opposes the random walk.
- **Numbers:** Fixation is recorded when a trait reaches 100% (or 0%) and stays there for 5 generations.
- **Check:** At least 1 in 10 neutral traits fixates within 50 generations at size 10, in 4 of 5 seeds, while fewer than 1 in 50 fixates at size 1,000; a neutral trait fixating fast in a large population is investigated as hidden selection.
**437. Loss of variation by drift**
- **Rule:** Drift grinds variation down. Every generation, chance removes some variants and fixes others, and without new mutation the population slowly becomes uniform. The rate is set by population size: small populations lose variation fast, large ones slowly.
- **Numbers:** Heterozygosity (the fraction of individuals carrying two different variants) is reported per generation; it should fall by roughly 1 over twice the effective population size per generation. Report the fall over 20 generations at sizes 10 and 200.
- **Check:** Measured heterozygosity loss matches the predicted rate within 30% over 20 generations, in 4 of 5 seeds; a faster loss suggests a bottleneck, a slower loss suggests hidden gene flow or balancing selection.
**438. Drift load: harmful traits that spread by chance**
- **Rule:** Drift can spread harmful traits. A trait that lowers fitness by a few percent can still fixate in a small population if chance favours its carriers for a few generations in a row. The population then carries a cost it did not choose and cannot remove without new variation.
- **Numbers:** A harmful trait is one with a measured selection coefficient below −0.05.
- **Check:** The harmful trait's frequency rises by at least 10 points in small populations while falling in large ones, in 4 of 5 seeds; a harmful trait rising in a large population is investigated as a hidden benefit or a measurement error.
**439. Drift in the protocell pond**
- **Rule:** Drift already operates in the protocell pond, where the life criterion was validated. The neutral control there — efficiency 1 regardless of GC fraction — exists precisely so that GC changes in that arm can be read as mutation plus drift, not selection. The main arm's GC rise counts as selection only because it exceeds the neutral arm's drift by at least 0.10.
- **Numbers:** The validated gap is main-minus-neutral GC of +0.1511, +0.1435, +0.1812 across seeds 20261105–07, against a 0.10 bar, in 3 of 3 seeds.
- **Check:** A new pond run reproduces a neutral-arm GC drift band within 0.05 of the validated band; a main-arm claim is accepted only where its gap over its own neutral control exceeds 0.10 in at least 2 of 3 seeds.
**440. Drift as the null hypothesis**
- **Rule:** Every selection claim in this phase is tested against drift first. The null hypothesis is always that the observed frequency change is chance in a finite population. Selection is claimed only when the change is too large, too consistent, or too directional for drift to explain at the measured population size.
- **Numbers:** For each claimed selection, report the drift-only expected frequency change (from effective population size and generations) alongside the observed change.
- **Check:** A written drift null accompanies every selection claim in the emergence log, with its numbers; claims without a null are returned for re-measurement, and at least 1 in 10 claims is expected to fail against its null.
### 5.5 Gene flow

**441. What gene flow is**
- **Rule:** Gene flow is the movement of traits between populations by migrants who arrive and breed. A migrant carries its home patch's traits into a new patch, and if it breeds, those traits enter the new population.
- **Numbers:** Migration rate is migrants per generation as a fraction of the receiving population, 0 to 0.5. Record the count, the migrants' trait frequencies, and the receiving population's frequencies before and after, over at least 5 generations.
- **Check:** A trait present in migrants at over 50% frequency appears in the receiving population within 3 generations of the first migrant breeding, in 4 of 5 seeds; a migrant trait that never appears means migrants are not breeding.
**442. Gene flow versus drift**
- **Rule:** Gene flow and drift pull in opposite directions. Drift makes separated populations different by chance; gene flow makes them similar by mixing. One migrant per generation is often enough to stop drift from splitting two populations, because that single breeding migrant reintroduces the variants drift removed.
- **Numbers:** The balance point is roughly 1 breeding migrant per generation: below it, populations diverge; above it, they stay similar.
- **Check:** Population pairs with under 1 migrant per generation diverge by at least 10 points on a neutral trait over 10 generations, while pairs above 1 stay within 5 points, in 4 of 5 seeds; a pair that diverges despite high migration is investigated for selection against migrants.
**443. Gene flow versus selection**
- **Rule:** Gene flow can swamp local selection. If migrants keep arriving carrying traits that are wrong for the local patch, selection must remove them every generation just to hold the local trait in place. Local adaptation survives only where selection against the migrant trait is stronger than the inflow.
- **Numbers:** Report migration rate and the local selection coefficient against the migrant trait together.
- **Check:** The local trait's frequency follows the prediction (held where selection beats migration, lost where migration wins) in 4 of 5 seeds; a trait held despite heavy migration is investigated for a stronger hidden selection.
**444. Migrants must breed**
- **Rule:** Arrival is not gene flow. A migrant that arrives, lives, and dies without breeding changes nothing genetically; its traits die with it. Gene flow counts only breeding migrants, and a migrant that breeds once counts once.
- **Numbers:** Record arrivals per generation and breeding migrants per generation separately; the breeding fraction is the ratio, 0 to 1. At least 20 arrivals per patch pair are observed before a breeding fraction is reported.
- **Check:** The receiving population's trait shift matches the breeding-migrant count, not the arrival count, within 25% over 5 generations, in 4 of 5 seeds; a shift matching arrivals would mean non-breeding migrants are being counted as flow.
**445. Gene flow along a gradient**
- **Rule:** Where conditions change gradually across space — wet to dry, warm to cold, rich to poor — gene flow carries traits along the gradient and selection trims them at each step. The result is a cline: trait frequencies that change smoothly with the conditions, steep where selection is strong, shallow where gene flow is strong.
- **Numbers:** Sample trait frequencies at least 5 points along the gradient, 30 individuals per point.
- **Check:** Trait frequency correlates with the local condition (correlation above 0.7) across the 5 sample points, in 4 of 5 seeds; a flat frequency across a steep condition gradient means gene flow is swamping selection, and that is recorded.
**446. Hybrid zones**
- **Rule:** A hybrid zone is a narrow band where two diverged populations meet and interbreed. Hybrids carry mixed traits, and their fate decides what happens next: if hybrids thrive, the populations merge; if hybrids are weak or sterile, the zone stays narrow and the populations stay distinct.
- **Numbers:** Zone width is measured in metres where hybrid frequency exceeds 10%; hybrid fitness is their reproducing-offspring ratio against pure parents. Report both over at least 5 generations, with at least 20 hybrids measured.
- **Check:** A zone narrower than 10 m with hybrid fitness below 0.5 is recorded as a tension zone (selection against hybrids holds it); a zone widening by over 20% in 5 generations is recorded as merging, and the species criterion is re-applied.
**447. Gene flow carries more than genes**
- **Rule:** A breeding migrant carries its traits, but also its microbes, its parasites, its learned habits if it can teach, and its effect on the local food and space. Gene flow is therefore never only genetic: the migrant changes the receiving patch ecologically as well.
- **Numbers:** Record migrant parasite or microbe load where measurable, and the receiving patch's population density and food level for 3 generations after first breeding. Any density change over 20% is reported alongside the genetic shift.
- **Check:** The genetic shift and the ecological shift are reported as separate numbers in the same entry, in 4 of 5 seeds; an entry that reports only one is returned as incomplete.
**448. Barriers to gene flow**
- **Rule:** Gene flow stops at barriers, and barriers are anything that stops breeding: a river, a dry stretch, a temperature band, a difference in breeding season, a difference in mating signal. Barriers are measured by what they do to breeding, not by how they look. A wide river that organisms cross daily is no barrier; a narrow strip nobody crosses is a wall.
- **Numbers:** Barrier strength is 1 minus the breeding-migrant rate across it, 0 (open) to 1 (closed). A barrier counts as strong above 0.9, weak below 0.5.
- **Check:** Trait-frequency gaps across a strong barrier exceed 20 points within 10 generations, while gaps across a weak barrier stay under 5 points, in 4 of 5 seeds; a strong-looking barrier with no gap is recorded as permeable.
**449. Gene flow after a bottleneck**
- **Rule:** After a bottleneck, gene flow is the fastest way to rebuild lost variation. A few breeding migrants can restore traits the crash removed, in a handful of generations, where mutation alone would take hundreds. A bottlenecked population that stays isolated stays narrow; one that receives migrants recovers its variation and its ability to respond to change.
- **Numbers:** After a bottleneck that cut variance by at least 30%, record variance recovery with and without migrants over 10 generations.
- **Check:** Migrant-receiving populations recover at least 50% of lost variance in 10 generations while isolated ones recover under 10%, in 4 of 5 seeds; equal recovery means the migrants are not breeding or the variance measure is wrong.
**450. Gene flow is measured, not assumed**
- **Rule:** Gene flow is never assumed from distance, from a map, or from the fact that two populations look similar. It is measured by counting breeding migrants and their trait contribution, generation by generation.
- **Numbers:** Every gene-flow claim lists migrants per generation, breeding fraction, and the trait-frequency shift attributed to migrants, each with its sample size. Claims based on fewer than 10 observed migrants are labelled provisional.
- **Check:** An independent check — trait frequencies in the receiving population predicted from the migrant count alone — matches the observed shift within 30% over 5 generations, in 4 of 5 seeds; a mismatch triggers a search for selection or drift in the same window.
### 5.6 Coevolution

**451. What coevolution is**
- **Rule:** Coevolution is reciprocal selection: two lineages each change in response to the other's change, generation after generation. A plant grows a thicker shell and the eater grows a stronger bite; the bite grows stronger and the shell grows thicker again.
- **Numbers:** Track the paired traits (for example shell thickness and bite force) per generation over at least 10 generations, in at least 5 seeds.
- **Check:** Changing one lineage's trait (by a controlled seed or a transplant) changes the other's trait mean within 3 generations, in 4 of 5 seeds; no response means the traits are correlated by a shared environment, not coevolution.
**452. Coevolution needs interaction**
- **Rule:** Coevolution only happens where the two lineages actually meet and affect each other's offspring counts. A predator that never catches a prey, a plant that no eater touches, a parasite that never infects — none of these coevolve, however close they live.
- **Numbers:** Interaction strength is the fitness change when the partner is removed: at least a 20% change in offspring counts counts as a real interaction. Report encounters per individual per generation (at least 10 observed) alongside the fitness effect.
- **Check:** Removing the partner changes the focal lineage's trait trajectory (mean shift of at least 0.2 standard deviations within 5 generations) in 4 of 5 seeds; no change means the interaction was too weak to coevolve.
**453. Predator and prey**
- **Rule:** Predator and prey coevolve through capture and escape: faster prey selects for faster predators, faster predators select for faster prey, better camouflage selects for better senses, better senses select for better camouflage. The pair can escalate, settle into a balance, or end when one side cannot keep up and the prey goes extinct or the predator starves.
- **Numbers:** Capture rate is captures per encounter, 0 to 1, reported per generation with encounter counts (at least 30 per generation).
- **Check:** Capture rate stays within 0.1 of its starting value while both speeds rise by at least 0.5 standard deviations, in 4 of 5 seeds; a capture rate that falls to zero means the prey has escaped the interaction, and one that rises to 1 means the prey is finished.
**454. Host and parasite**
- **Rule:** Host and parasite coevolve through infection and defence: a parasite that infects more hosts selects for hosts that resist, resistant hosts select for parasites that overcome resistance.
- **Numbers:** Infection rate (fraction of hosts infected), parasite transmission per infected host, and host offspring loss per infection are reported per generation over at least 10 generations, with at least 50 hosts per patch.
- **Check:** Host resistance rises (infection rate falls by at least 10 points) and parasite infectivity then rises (infection rate recovers at least half the fall) within 5 generations each, in 4 of 5 seeds; a one-sided change is selection, not coevolution.
**455. Plant and eater**
- **Rule:** Plants and eaters coevolve through defence and counter-defence: thorns, tough leaves, bitter chemicals on one side; stronger jaws, detoxification, timing on the other. A plant that is never eaten does not invest in defence, and an eater that cannot eat the plant does not invest in counter-defence; each side pays only where the other bites.
- **Numbers:** Defence level (thorn density, toxin concentration, leaf toughness) and eater success (fraction of feeding attempts that gain food) are reported per generation over at least 10 generations.
- **Check:** A rise in defence of at least 20% is followed within 3 generations by a rise in eater counter-defence that restores at least half the lost feeding success, in 4 of 5 seeds; defence rising with no eater response means the eater has moved to another food.
**456. Mutualism coevolves too**
- **Rule:** Coevolution is not only conflict. In mutualism, two lineages each gain from the other — one provides food or shelter, the other provides transport, protection, or nutrients — and each selects for partners that give more. Cheats that take without giving are selected against by partners that stop rewarding them, so the pair can stabilise into a partnership that neither could manage alone.
- **Numbers:** Benefit per interaction is measured in offspring or energy for each partner, with at least 30 interactions observed per generation.
- **Check:** Partners that give more receive more (correlation above 0.5 between giving and receiving per individual), and cheats fall below 10% frequency within 5 generations of appearing, in 4 of 5 seeds; cheats persisting above 20% mean the partnership is not policed.
**457. Coevolution is local**
- **Rule:** Coevolution happens in a patch, between the organisms that actually meet there. The same two lineages can coevolve in one patch, ignore each other in another, and coevolve in opposite directions in a third, because the encounter rate, the food, and the costs differ.
- **Numbers:** The paired traits are reported separately for at least 3 patches, with encounter rates per patch. A pair counts as coevolving in a patch only where the encounter rate exceeds 1 per individual per generation and the trait correlation exceeds 0.7 there.
- **Check:** The trait correlation differs by at least 0.3 between the highest- and lowest-encounter patches, in 4 of 5 seeds; identical correlations everywhere suggest a shared environmental driver, not local coevolution.
**458. Coevolutionary mosaics**
- **Rule:** Because coevolution is local, the world becomes a mosaic: hot spots where the pair escalates fast, cold spots where nothing happens, and patches in between. Gene flow between patches mixes the results, so a hot spot's traits leak into cold spots and a cold spot's traits dilute a hot spot.
- **Numbers:** Hot spots are patches where both paired traits move at least 0.2 standard deviations per generation; cold spots move under 0.05.
- **Check:** Trait means differ by at least 1 standard deviation between the hottest and coldest patches after 10 generations, and the gap shrinks when migration between them doubles, in 4 of 5 seeds.
**459. Coevolution can end**
- **Rule:** Coevolution ends when the interaction ends: one side goes extinct, moves to another partner, or becomes so good that the other side stops mattering. A prey that becomes uncatchable, a host that becomes immune, a plant that becomes inedible — each ends the race by winning it outright, and then its own trait stops being selected and starts drifting.
- **Numbers:** An ending is recorded when the encounter rate falls below 0.1 per individual per generation for 5 consecutive generations, or one partner's local population reaches zero.
- **Check:** After the recorded ending, the escalating trait's mean shift falls below 0.05 standard deviations per generation for 5 generations, in 4 of 5 seeds; continued movement means the interaction has not actually ended.
**460. Coevolution is measured in pairs, not in species**
- **Rule:** A coevolution claim names two lineages, one patch, the two traits, and the lag between their changes. It does not name two species in the abstract, because the same species can be coevolving in one patch and indifferent in another.
- **Numbers:** Every coevolution entry lists both trait means per generation for at least 10 generations, the encounter rate, and the cross-correlation with its lag in generations. Entries without a lag estimate are labelled provisional.
- **Check:** An independent re-run from the same seed reproduces the cross-correlation within 0.2 and the lag within 1 generation, in 4 of 5 seeds; a claim that does not reproduce is withdrawn.
### 5.7 Arms races

**461. What an arms race is**
- **Rule:** An arms race is coevolution with escalation: each side's improvement selects for a bigger improvement on the other side, so both traits climb together. Speed against speed, armour against weapons, poison against resistance, senses against camouflage.
- **Numbers:** An arms race is recorded where both paired traits rise at least 0.2 standard deviations per generation for at least 5 consecutive generations, with the interaction outcome (capture rate, infection rate, feeding success) staying within 0.1 of its starting value. Report trait means and outcome per generation.
- **Check:** Both traits rise together (correlation above 0.7) while the outcome stays flat, in 4 of 5 seeds; traits rising while the outcome moves strongly in one side's favour is a one-sided win, not a race.
**462. Escalation has a cost**
- **Rule:** Every step in an arms race is paid for in energy, growth, or reproduction. Thicker armour is heavier, faster legs burn more, stronger poison costs more to make, sharper senses cost more brain. The race climbs only while the gain from the next step exceeds its cost; when the cost line crosses the gain line, the trait stops, even if the other side keeps going.
- **Numbers:** Cost per trait step is measured in energy per generation or in offspring lost: a step costing over 10% of lifetime offspring is a steep step.
- **Check:** The trait stops rising (mean shift under 0.05 standard deviations for 3 generations) within 2 steps of the measured cost first exceeding the measured gain, in 4 of 5 seeds; a trait that keeps rising past that point is investigated for an unmeasured gain.
**463. The Red Queen: running to stay still**
- **Rule:** In an arms race, a lineage can improve every generation and gain nothing, because the other side improves just as fast. This is the Red Queen: you must run as fast as you can to stay in the same place.
- **Numbers:** Red Queen is recorded where both traits rise at least 0.5 standard deviations over 10 generations while the interaction outcome stays within 0.05 of its start, and where a lineage that stops improving loses at least 20% of its outcome within 3 generations.
- **Check:** A control lineage frozen at its starting trait value (by a separate seed or a transplant) loses at least 20% on the outcome measure within 3 generations against the escalated partner, in 4 of 5 seeds; if the frozen lineage holds its ground, there is no race.
**464. Arms races end in extinction**
- **Rule:** An arms race can end with one side gone. If the prey cannot keep up, it is eaten out; if the predator cannot keep up, it starves; if the host cannot resist, it dies out; if the parasite cannot infect, it vanishes.
- **Numbers:** The trait gap at extinction is reported in standard deviations, with the last 5 generations of both trait means and the outcome rate. Extinction is recorded when a local population reaches zero and stays zero for 5 generations.
- **Check:** In at least 1 in 5 race runs, one side goes extinct locally within 20 generations, in 4 of 5 seeds; a race that never ends in extinction anywhere is checked for a hidden cap on escalation.
**465. Arms races end in stalemate**
- **Rule:** A race can also end in stalemate: both sides reach a point where the next step costs more than it gains for both, and the traits stop moving. The outcome settles at a stable rate — some prey caught, some hosts infected, some plants eaten — and stays there.
- **Numbers:** Stalemate is recorded where both trait means move under 0.05 standard deviations per generation for 5 consecutive generations while the interaction continues (encounter rate above 1 per individual per generation) and the outcome stays within 0.05.
- **Check:** The stalemate holds for at least 10 generations in 4 of 5 seeds, and a 20% increase in food inflow restarts movement in at least 1 in 3 of those runs; a stalemate that never restarts is checked for a hard cap.
**466. Asymmetric races**
- **Rule:** Arms races are rarely fair. One side may breed faster, mutate faster, pay less per step, or have more variation to draw on, so it climbs faster and the other side falls behind. The faster side's advantage is a number — generation time, mutation rate, cost per step — not a story about being better.
- **Numbers:** Report generation time, mutation rate, and cost per trait step for both sides.
- **Check:** The favoured side's trait rises at least twice as fast (in standard deviations per generation) as the other side's, in 4 of 5 seeds; equal rise despite a measured asymmetry is investigated as a hidden cost on the favoured side.
**467. Arms races spill over**
- **Rule:** A trait built for one race can spill into another interaction. Armour built against one predator also blocks another; poison built against one eater also deters another; speed built to escape one hunter also catches different prey.
- **Numbers:** For each escalated trait, report its effect on at least 2 other interactions in the same patch (capture rate, feeding success, infection rate), measured before and after the escalation, with at least 20 encounters per interaction.
- **Check:** At least 1 in 3 escalated traits changes a second interaction's outcome by over 10%, in 4 of 5 seeds; spillover is recorded as a measured side effect, never as a reason to call the trait generally good.
**468. De-escalation**
- **Rule:** Arms races can run backwards. If the partner disappears, the expensive trait becomes pure cost, and selection starts trimming it: thinner armour, slower legs, weaker poison, duller senses. De-escalation is selection too, and it is often faster than the climb, because the cost is paid every generation while the gain has vanished.
- **Numbers:** After the partner is removed (encounter rate below 0.1 for 5 generations), track the trait mean for 10 generations.
- **Check:** The trait falls by at least 0.5 standard deviations within 10 generations of the partner's removal, in 4 of 5 seeds, and the falling lineage gains at least 10% in offspring over the same window; a trait that does not fall is checked for a second use.
**469. Arms races and the Discovery Principle**
- **Rule:** Arms races are a discovery mechanism, not a placed story. Nobody decides that armour or poison or speed will appear; the rules of encounter, cost, and inheritance produce them, and the owner could not have predicted which defence or which counter would show up.
- **Numbers:** Each race entry lists the first appearance generation of each new trait level (defence or counter), with the trait value and the outcome rate at that generation.
- **Check:** The pre-run prediction list (written before the run) is compared with the observed trait levels after the run; levels not on the list are recorded as discovered, in 4 of 5 seeds, and the list itself is kept in the emergence log.
**470. Arms races are not progress**
- **Rule:** An arms race is not progress, improvement, or a ladder. Both sides can become faster, tougher, and more expensive while gaining nothing in outcome, and the world can end up spending far more energy for the same number of births and deaths.
- **Numbers:** Report total energy spent per generation by both sides before and after the race, alongside the outcome rate. A race where energy spend rises over 50% while the outcome stays within 0.05 is recorded as a costly stalemate.
- **Check:** The energy and outcome numbers appear together in every race entry, in 4 of 5 seeds; an entry that reports trait climbs without the energy cost is returned as incomplete.
### 5.8 Trade-offs

**471. What a trade-off is**
- **Rule:** A trade-off is a fixed budget split two ways: gain here, loss there, from the same body and the same energy. It is not a vague compromise; it is an arithmetic fact that a body spending more on one thing spends less on another.
- **Numbers:** A trade-off is recorded where a trait raises one fitness component by at least 10% and lowers another by at least 10%, measured in the same individuals over at least 3 generations, with at least 50 individuals per group.
- **Check:** The component gains and losses are reported side by side with the net offspring ratio, in 4 of 5 seeds; a gain reported without its loss is treated as an incomplete claim.
**472. Growth versus reproduction**
- **Rule:** Energy spent growing a bigger body cannot be spent making offspring. A lineage that grows large first breeds late and breeds fewer times; a lineage that breeds early stays small and breeds often. Which wins depends on the patch: where size protects against predators, late breeding pays; where food is brief, early breeding pays.
- **Numbers:** Report age at first reproduction, adult size, and lifetime offspring together, for at least 50 individuals per lineage.
- **Check:** The lineage with the higher lifetime offspring count in a patch is recorded as winning that patch, in 4 of 5 seeds, regardless of which side is bigger; a size claim without an offspring count is rejected.
**473. Survival versus reproduction**
- **Rule:** Energy spent staying alive — defence, repair, immune response, cautious behaviour — cannot be spent breeding. A lineage that invests heavily in survival lives long and breeds slowly; one that invests in breeding lives fast and dies young.
- **Numbers:** Report median lifespan and lifetime offspring together per lineage, at least 100 individuals. A survival investment that adds at least 20% to lifespan while cutting lifetime offspring by at least 10% is a survival-reproduction trade-off.
- **Check:** Lifetime offspring, not lifespan, predicts population share over 5 generations (correlation above 0.7), in 4 of 5 seeds; a long-lived lineage losing share is recorded as losing the trade-off.
**474. Speed versus endurance**
- **Rule:** A body built for a sprint is not built for a long chase, and a body built for endurance is not built for a burst. Muscle, energy stores, and heat all split one way or the other. Sprinters win short encounters and pay in recovery; endurance runners win long ones and pay in top speed.
- **Numbers:** Report top speed and time-to-exhaustion in the same units, plus encounters won per generation, for at least 30 individuals per lineage.
- **Check:** The lineage whose speed-endurance mix matches the common encounter length in its patch wins more encounters per energy spent, in 4 of 5 seeds; a faster lineage losing encounters is recorded as mismatched, not as unfit in general.
**475. Offspring number versus offspring size**
- **Rule:** A parent has a fixed reproductive budget to split among offspring: many small ones, or few large ones. Small offspring are cheap and numerous but fragile; large offspring are expensive and few but tough. Where the world is gentle, many small offspring win; where it is harsh, few large ones win.
- **Numbers:** Report offspring per birth, offspring size at birth, and offspring survival to breeding age, for at least 50 births per lineage.
- **Check:** The split that leaves more reproducing adults per parent wins the patch, in 4 of 5 seeds; a lineage making more babies that mostly die is recorded as losing, however many births it logs.
**476. Defence versus growth**
- **Rule:** Armour, spines, toxins, and thick skin cost material and energy that cannot go into growth. A defended organism grows slower and breeds later; an undefended one grows fast and breeds early, and pays when a predator arrives.
- **Numbers:** Report defence level, growth rate, and predator encounter rate together per patch, at least 30 individuals per lineage. Defence is worth it where encounter rates exceed 1 per individual per generation and defended survival exceeds undefended by at least 20%.
- **Check:** Defended lineages outbreed undefended ones only in high-predator patches, and lose in predator-free patches, in 4 of 5 seeds; defence winning everywhere suggests the cost is not being measured.
**477. Foraging versus vigilance**
- **Rule:** Time spent watching for danger cannot be spent eating, and time spent eating cannot be spent watching. An organism that feeds with its head down eats more and dies more; one that watches constantly eats less and lives longer.
- **Numbers:** Report time fractions (feeding versus vigilant) per individual, food gained per hour, and death rate per hour, over at least 100 observation hours per lineage. A 10% rise in vigilance that cuts food intake by at least 10% is a foraging-vigilance trade-off.
- **Check:** The vigilance level that maximises net offspring in a patch matches the patch's measured danger level (correlation above 0.6 across patches), in 4 of 5 seeds; a lineage watching more than the danger warrants is recorded as overpaying.
**478. Generalist versus specialist**
- **Rule:** A generalist eats many foods badly; a specialist eats one food well. The generalist survives when any one food fails, because it can switch; the specialist starves when its food fails, but outcompetes the generalist while its food is abundant.
- **Numbers:** Diet breadth is the number of food types eaten (at least 10 feeding observations per individual); efficiency is food gained per hour on the main food. Report both per lineage across at least 3 patches with different variability.
- **Check:** Specialists outbreed generalists in the most stable patch by at least 10%, and generalists outbreed specialists in the most variable patch by at least 10%, in 4 of 5 seeds; a lineage winning everywhere is checked for an unmeasured cost.
**479. Current reproduction versus future reproduction**
- **Rule:** Breeding now spends the body; breeding later saves it. An organism that breeds hard in its first season may have nothing left for a second, while one that holds back breeds in two seasons. Which pays depends on the chance of surviving to the second season: where survival is unlikely, breed now; where it is likely, hold back.
- **Numbers:** Report first-season births, second-season births, and survival between seasons, for at least 50 individuals per lineage.
- **Check:** Lifetime offspring, not first-season births, predicts population share over 5 generations, in 4 of 5 seeds; a lineage winning the first season and losing the lifetime count is recorded as losing the trade-off.
**480. Trade-offs are measured in one currency**
- **Rule:** Every trade-off in this milestone is converted into the same currency: reproducing offspring per parent per lifetime. Energy, time, size, speed, and defence are all costs; only offspring are the payoff.
- **Numbers:** Every trade-off entry ends with the net offspring ratio between the two strategies (to 2 decimal places) over at least 3 generations, with at least 50 parents per strategy. A ratio within 0.05 of 1.0 is recorded as a tie.
- **Check:** The net ratio predicts the frequency change of the two strategies within 25% over 3 generations, in 4 of 5 seeds; a strategy with a worse ratio that still spreads is investigated as drift, gene flow, or a hidden benefit.
### 5.9 Selection is local

**481. Selection acts where the organism lives**
- **Rule:** Selection acts in the patch where the organism eats, breeds, and dies — not in the world average, not in a distant patch, not in a textbook. A trait's value is decided by the food, predators, temperature, and neighbours in that one place, at that one time.
- **Numbers:** Every selection coefficient is reported per patch, with patch identity, food level, temperature, and density at the time of measurement. At least 3 patches are measured before any cross-patch comparison is made.
- **Check:** The same trait's coefficient differs by at least 0.1 between the most and least favourable patches, in 4 of 5 seeds; identical coefficients everywhere suggest the patch labels are not being used.
**482. Local adaptation**
- **Rule:** Local adaptation is a lineage doing better at home than away: higher offspring counts in its own patch than in a neighbouring patch, and higher than a foreign lineage transplanted into its patch. It is the signature that selection has tuned the lineage to its place.
- **Numbers:** Transplant experiments use at least 30 individuals per lineage per patch, in at least 2 patches. Local adaptation is recorded where the home lineage outbreeds the foreign lineage by at least 10% at home, and the reverse holds away.
- **Check:** The home-advantage pattern holds in both directions (each lineage wins at home) in 4 of 5 seeds; a lineage winning everywhere is recorded as generally fitter, not locally adapted.
**483. Maladaptation away from home**
- **Rule:** The other side of local adaptation is maladaptation away: a lineage tuned to one patch does badly in another, because the traits that help at home hurt away. A thick coat helps in the cold and kills in the heat; a fast sprint helps on open ground and fails in thick cover.
- **Numbers:** Report the offspring ratio of a lineage at home versus away: a ratio below 0.8 away from home counts as maladaptation.
- **Check:** The away ratio falls below 0.8 while the home ratio stays above 1.0 against foreigners, in 4 of 5 seeds; a lineage doing equally well everywhere is recorded as a generalist, not as locally adapted.
**484. Patch boundaries are real**
- **Rule:** Patches are not lines on a map; they are places where conditions change enough that selection changes direction. A patch boundary is where a trait's selection coefficient changes sign — favoured on one side, disfavoured on the other. The boundary is found by measuring the coefficient across space, not by drawing it first and measuring later.
- **Numbers:** Sample the selection coefficient at least 5 points across a suspected boundary, 30 individuals per point.
- **Check:** The sign change reproduces in 4 of 5 seeds at the same location (within 10% of the transect length); a boundary that moves from seed to seed is recorded as a gradient, not a boundary.
**485. Microclimates matter**
- **Rule:** Selection can differ across metres. A shaded hollow, a sunny rock, a wet ditch, and a dry ridge in the same small area can favour different traits, because temperature, moisture, and food differ at that scale.
- **Numbers:** Microclimate is measured at the scale organisms use: temperature and moisture at 1 m spacing, at least 20 points per locale. Trait frequencies are sampled at the same points, with at least 20 individuals per point.
- **Check:** Trait frequency correlates with the microclimate variable (correlation above 0.6) across the 20 points within one locale, in 4 of 5 seeds; no correlation means the microclimate is not the selecting factor.
**486. Selection changes with density**
- **Rule:** The same trait can be favoured when a patch is crowded and disfavoured when it is empty. At high density, competition for food and mates dominates, and traits that win contests spread; at low density, finding food and surviving the weather dominate, and contest traits are wasted cost.
- **Numbers:** Report density (individuals per square metre) with every coefficient, across densities from 0.1 to 10 per square metre.
- **Check:** The coefficient's sign or size changes by at least 0.1 between the lowest and highest density measured, in 4 of 5 seeds, for at least 1 in 3 traits tested; traits that never change with density are recorded as density-independent.
**487. Selection changes with season**
- **Rule:** A trait favoured in one season can be disfavoured in the next. Summer favours fast growth; winter favours fat stores and shelter. A lineage's fitness is the sum across the seasons it lives through, and a trait that wins the summer and loses the winter may still be net fit — or net unfit — depending on which season kills more.
- **Numbers:** Report the selection coefficient per season (at least 2 seasons, each at least 1 generation long where generation time allows), plus the net annual coefficient.
- **Check:** The net annual coefficient predicts the year-on-year frequency change within 25%, in 4 of 5 seeds; a prediction from one season alone that fails is recorded as a seasonal error, not as a selection failure.
**488. Selection changes over a lifetime**
- **Rule:** Selection is not the same at every age. A trait that helps a juvenile survive may hurt an adult's breeding, and a trait that helps an adult breed may kill a juvenile. The strength of selection also falls with age: traits that matter after most breeding is done are barely selected at all, because few offspring depend on them.
- **Numbers:** Report survival and breeding success per age class (juvenile, prime, old), at least 30 individuals per class, with the selection coefficient per class.
- **Check:** The age-weighted coefficient (weighted by offspring produced per age class) predicts the trait's frequency change within 25% over 3 generations, in 4 of 5 seeds; an unweighted coefficient that predicts wrong is corrected to the weighted one.
**489. No selection in the abstract**
- **Rule:** There is no such thing as selection in general — only selection in a patch, in a season, at a density, at an age. A claim that a trait is "selected for" without naming the patch, the season, the density, and the age is a slogan, not a measurement.
- **Numbers:** Each entry lists patch, season, density (individuals per square metre), and age class, with the coefficient and the sample size (at least 30 individuals). Entries with fewer than 30 individuals are labelled provisional.
- **Check:** A random audit of 10 selection entries finds all four labels present and the sample size stated in at least 9 of 10; entries failing the audit are re-measured before they are cited.
**490. Local selection, global record**
- **Rule:** Local selection is recorded locally and compared globally. The record keeps each patch's coefficient separate, so the pattern across patches — same direction everywhere, opposite directions, strong here and absent there — is visible instead of averaged away.
- **Numbers:** The record holds at least 3 patches per trait, each with its coefficient, sample size, and conditions. A species-level claim requires agreement (same sign) in at least 3 of 4 patches, or it is reported as locally variable.
- **Check:** The cross-patch pattern is recomputed from the stored local numbers and matches the species-level summary, in 4 of 5 seeds; a summary that cannot be rebuilt from its local entries is withdrawn.
### 5.10 Selection is measured

**491. Every selection claim carries a number**
- **Rule:** A selection claim without a number is not a claim. The number is the selection coefficient, the frequency change, the offspring ratio, or the survival gap — with its sample size, its patch, and its generations. Words like strong, weak, favouring, or selecting are banned from the record unless the number sits beside them.
- **Numbers:** Every claim lists the effect size (coefficient or ratio, to 2 decimal places), the sample size (at least 30 individuals), the generations observed (at least 3), and the seeds (at least 5).
- **Check:** A random audit of 10 claims finds all four numbers present in at least 9 of 10; a claim that fails the audit is struck from the record until re-measured.
**492. The null is drift, always**
- **Rule:** The first test of any selection claim is the drift null: could chance in a population this size produce a change this big? The null is computed from the effective population size and the generations observed, and the claim passes only if the observed change is far larger than the null expects. Selection is the explanation left standing after drift has been ruled out, not the first guess.
- **Numbers:** The drift null is the expected frequency change from chance alone, computed from effective population size; report it beside the observed change.
- **Check:** At least 1 in 10 selection claims fails against its drift null and is reclassified as drift, in the record as a whole; a phase with zero failed claims is audited for nulls that were never computed.
**493. Controls: the neutral trait**
- **Rule:** Every selection measurement runs beside a neutral control: a trait known to carry no fitness effect, measured in the same population, over the same generations, in the same patches. The neutral trait shows what drift and sampling noise look like in this exact run, so the selected trait's movement can be judged against it.
- **Numbers:** The neutral trait is measured with the same sample size (at least 30 individuals) and the same generations as the selected trait.
- **Check:** The neutral trait's change stays within its drift-only expectation in 4 of 5 seeds; a neutral trait moving far beyond its expectation means the run has an unmeasured force, and all claims from that run are held.
**494. Replication across seeds**
- **Rule:** A selection result that happens in one seed is a hint; one that happens in five is a result. Every claim is replicated across at least 5 seeds with different starting conditions, and the claim is the pattern across seeds, not the best seed.
- **Numbers:** Minimum 5 seeds per claim; the pass rate (seeds passing out of seeds run) is reported with the claim. A claim is accepted at 4 of 5 or better; 3 of 5 is provisional; below 3 is rejected.
- **Check:** The pass rate is stated in the same line as the claim in the emergence log, in 4 of 5 claims audited; a claim without a pass rate is returned for re-measurement.
**495. Falsifiers for selection claims**
- **Rule:** Every selection claim states what would prove it wrong before the run: the frequency change that would not happen, the direction that would falsify it, the control that would kill it. A claim with no falsifier cannot be tested and is not accepted.
- **Numbers:** Each claim's falsifier is a numeric threshold: for example, trait frequency rises less than 5 points over 3 generations, or the neutral control moves as far as the selected trait. The threshold is set before the run and is not moved after.
- **Check:** At least 1 in 10 claims is falsified and recorded as falsified, with the numbers, in the record as a whole; a phase with no falsified claims is audited for falsifiers written after the results.
**496. Selection is reported as a change, not a state**
- **Rule:** Selection is a change over time: frequencies moving, means shifting, shares growing or shrinking. A snapshot — a trait being common, a lineage being large — proves nothing about selection, because the trait could be common by history, by drift, or by an old selection that has long since stopped.
- **Numbers:** Every claim reports the starting frequency, the ending frequency, and the generations between them (at least 3), plus the rate of change per generation. A claim with only an ending frequency is labelled a snapshot and cannot close a milestone.
- **Check:** A random audit finds starting and ending frequencies with generation counts in at least 9 of 10 claims; snapshot-only claims are struck until a before-and-after is supplied.
**497. Confounds are named**
- **Rule:** A frequency change can be selection, drift, gene flow, a bottleneck, a changed patch, or a measurement error, and the record names which ones were checked. Each claim lists the confounds considered — drift (by the null), gene flow (by the migrant count), bottleneck (by the census), patch change (by the condition log) — and what each check found.
- **Numbers:** Each claim lists at least 3 confounds checked, with the check result (a number where possible: migrant count, census size, condition change).
- **Check:** In at least 1 in 5 claims, a confound check changes the conclusion (selection reclassified as drift, gene flow, or bottleneck), recorded in the log; a phase where no confound ever changes a conclusion is audited.
**498. The selection log**
- **Rule:** All selection measurements live in one log: trait, patch, season, density, age class, coefficient, frequency change, drift null, neutral control, seeds, pass rate, falsifier, confounds checked, and the verdict. The log is append-only; a falsified claim stays in it, struck through with its numbers, so the same mistake is not repeated.
- **Numbers:** The log holds one entry per claim, with all 13 fields filled. Completeness is audited per milestone: at least 9 of 10 entries complete before the milestone closes.
- **Check:** The log is re-readable from a checkpoint after a resume, with every entry intact (verified by count and by hash); a log that loses entries on resume fails validation and is rebuilt before work continues.
**499. Selection claims and the Gateway**
- **Rule:** Selection measurements are served through the Gateway like any other world state: population counts, trait frequencies, and lineage shares appear in the snapshot, and the viewer shows them as measured numbers, never as invented ones. The Gateway contract is closed and is not changed by this phase; selection data uses the existing snapshot fields and the repo logs, and no write path is added.
- **Numbers:** Snapshot fields used are population, births, turnovers, and lineage counts, as defined in the Gateway contract (contract version 1).
- **Check:** A selection claim's numbers match the Gateway snapshot and the repo log at the cited tick within 1% in 4 of 5 audited claims; a mismatch is investigated as a logging error before the claim is accepted.
**500. Phase 5 sign-off**
- **Rule:** Phase 5 closes when every milestone's claims are measured, replicated, and logged: fitness counted, natural selection demonstrated, sexual selection separated from survival, drift measured against its null, gene flow counted in breeding migrants, coevolution shown in pairs, arms races costed, trade-offs converted to offspring, selection shown to be local, and every claim carrying a number. Nothing is claimed done without a measured result.
- **Numbers:** Sign-off requires 10 of 10 milestones complete, each with its checks passing in at least 4 of 5 seeds, the selection log at least 90% complete, and at least 1 in 10 claims recorded as falsified or reclassified.
- **Check:** The sign-off entry in the emergence log lists the milestone counts, the seed pass rates, and the log completeness, and is reviewed by Muse before Phase 6 begins; a missing number blocks sign-off until it is supplied.

## Phase 6 — Evolution rulebook: speciation and deep time

### 6.1 What a species is

**501. The species criterion**
- **Rule:** A species is defined by reproductive isolation OR genetic distance beyond a measured threshold; both count. Two populations are different species when they can no longer produce fertile offspring together, or when their genomes have drifted apart past the threshold, even if no mating test has run.
- **Numbers:** Freebuff proposes the starting genetic-distance threshold, Muse reviews it; starting proposal is a genome-wide sequence divergence of 2–5%, to be challenged by measurement. The isolation test requires at least 20 attempted pairings with zero fertile offspring.
- **Check:** The criterion identifies a split in a test run where two lineages diverged, and does not split a control lineage that stayed connected; the decision and threshold are recorded in the research log.

**502. Reproductive isolation as the first test**
- **Rule:** Two organisms are reproductively isolated when mating between them produces no offspring, or offspring that cannot reproduce. Isolation can come from mismatched mating signals, incompatible timing, incompatible anatomy, or genomes that fail to pair during reproduction. The test is done by attempting pairings in the world, not by inspecting a label.
- **Numbers:** A pair of lineages is tested with at least 20 pairings across 3 runs; isolation is recorded when fertile offspring are 0 of 20. A single sterile hybrid does not count; the failure must repeat.
- **Check:** The isolation test returns "isolated" for a known-diverged pair and "not isolated" for a connected control pair, across ≥5 seeds; the counts are logged per run.

**503. Genetic distance as the second test**
- **Rule:** Genetic distance is the fraction of inherited sequence that differs between two organisms, measured over the whole genome. Distance grows by mutation and is reset toward zero only by mating between lineages. When distance passes the threshold, the lineages count as different species even if nobody has tested mating between them.
- **Numbers:** Distance is computed over the full genome each generation; the threshold is the value set under topic 501 (Freebuff proposes, Muse reviews). Lineages are compared at least once every 100 generations.
- **Check:** Two lineages that split and never exchange genes cross the threshold within a recorded number of generations, while a freely mating control population stays below it; both curves are logged.

**504. One mind, many species**
- **Rule:** Every species uses the same architecture family (neural core + forward model + episodic memory, sized to the organism), whatever its body. A species is a fact about reproduction and ancestry, not a different kind of mind. New species inherit the family; they do not get a new architecture placed on them.
- **Numbers:** Mind size follows the sizing rule from Phase 3 at every species; no species gets a hand-set mind size. The family is checked at 3 species per run.
- **Check:** Minds in two different species are built by the same construction code with different size parameters; the construction test passes at ≥3 sizes and the result is recorded.

**505. Species are populations, not types**
- **Rule:** A species is a population of interbreeding organisms, not a single ideal form. Individuals inside one species differ — in size, speed, efficiency, and traits — and the species is the spread of those differences plus the gene flow between them. No single organism defines its species.
- **Numbers:** Within-species trait spread is measured as the standard deviation of at least 3 traits across at least 50 living members; between-species spread must exceed within-species spread by at least 2× on the same traits.
- **Check:** The spread numbers are logged per generation; a run where two species overlap fully on all measured traits is flagged and the criterion re-examined, not papered over.

**506. Ring species and the fuzzy edge**
- **Rule:** Neighbouring populations can interbreed while distant ones cannot, forming a ring where "same species" depends on which pair is tested. The criterion handles this by testing pairs, not by forcing a single clean boundary: A breeds with B, B with C, but A cannot breed with C, and the record says exactly that instead of pretending the ring is one species or two.
- **Numbers:** Pairwise tests run for every adjacent pair plus the two end populations; at least 20 pairings per pair. The ring is recorded when adjacent pairs pass and the ends fail.
- **Check:** A simulated ring is detected and logged as a ring (not collapsed to one or two species) in a test run; the pairwise matrix is stored in the run log.

**507. Subspecies and varieties inside a species**
- **Rule:** Populations inside one species can differ in traits, habitat, or timing while still interbreeding. These are varieties, not species: they are recorded as trait clusters with gene flow between them, and they become species only when isolation or distance crosses the criterion. No variety is promoted by hand.
- **Numbers:** A variety is recorded when a trait cluster differs from the species mean by at least 2 standard deviations on at least 1 trait, while gene flow with the main population stays above 1 migrant per generation.
- **Check:** Varieties are listed per run with their trait offsets and gene-flow numbers; none is recorded as a species until the criterion in topic 501 is met, verified by the species-identification test.

**508. Naming species in the record**
- **Rule:** Every species the rule identifies gets a stable identifier in the historical record: first-appearance generation, parent species, and the evidence that triggered the split (isolation test or distance value). Names are labels for the record only; they change nothing in the world and no organism knows its species name.
- **Numbers:** Identifiers are sequential per run (SP-001, SP-002, …); each entry carries the generation, the parent identifier, and the trigger value. The record is written within 1 generation of identification.
- **Check:** A lineage query returns every species' ancestors back to the first cell with no gaps, and every identifier resolves to a recorded trigger; the query is tested on ≥5 runs.

**509. Species are not designed**
- **Rule:** Nobody decides what species exist. Species appear when lineages diverge under mutation, selection, and isolation; the owner's job is to measure the split, not to choose it. Any species that appears only because a value was placed by hand is recorded as placed, not evolved, and does not count toward the diversity numbers.
- **Numbers:** Zero hand-placed species per run is the target; any exception is logged with its cause and excluded from the species count. Diversity is reported with placed species removed.
- **Check:** A run audit finds no species whose first member was created outside reproduction; the audit result is recorded per run, and a failed audit blocks the phase sign-off.

**510. The species list is a living record**
- **Rule:** The species list changes every generation: species are born by splitting, die by extinction, and merge when gene flow resumes. The list is recomputed from the living population each generation, not frozen at first sight. An extinct species stays in the historical list with its end generation; a merged species stays with its merge generation.
- **Numbers:** The list is recomputed at least once per 100 generations; merges require gene flow above 1 migrant per generation sustained for 10 generations. The list is stored with the checkpoint.
- **Check:** The list at generation N matches an independent recount from the lineage log within 1 species; the recount is tested on ≥5 runs and the result recorded.

### 6.2 Isolation

**511. Geographic isolation — distance and barriers**
- **Rule:** A physical barrier — water, rock, distance beyond travel range — stops mating between two groups, so their genes stop mixing. Each group then evolves on its own. Barriers are terrain and distance, not walls placed for the purpose; the world makes them and the record notes where they are.
- **Numbers:** A barrier counts as isolating when crossings fall below 1 per 100 generations for at least 500 generations. Travel range is measured per body plan (speed × active hours per day).
- **Check:** Two groups separated by a barrier show zero gene flow for 500 generations while a connected control shows flow above 1 migrant per generation; both are logged.

**512. Ecological isolation — different ways to live**
- **Rule:** Two groups can live side by side yet never mate because they eat different food, live in different patches, or are active at different times. Their worlds overlap in space but not in habit, so gene flow stops without any wall. The separation is measured by what they do, not where a boundary is drawn.
- **Numbers:** Ecological isolation is recorded when shared food sources fall below 10% overlap and mating encounters fall below 1 per 100 generations, sustained for 500 generations.
- **Check:** Two lineages in the same region with under 10% food overlap and under 1 mating encounter per 100 generations are flagged as ecologically isolated; the food-overlap and encounter counts are logged.

**513. Temporal isolation — different clocks**
- **Rule:** Groups that breed in different seasons, at different times of day, or at different life stages never meet as mates even when they share the same ground. Their clocks separate them. The breeding window of each group is measured from behaviour, and overlap below the threshold means isolation.
- **Numbers:** Breeding windows are measured in hours per day or days per season; isolation is recorded when window overlap is under 5% for at least 10 breeding cycles.
- **Check:** Two groups with under 5% breeding-window overlap produce zero cross-group offspring over 10 cycles while a same-clock control produces offspring; the window measurements are logged.

**514. Behavioural isolation — signals that do not match**
- **Rule:** Mating depends on signals — movement patterns, chemical cues, timing of approach — and when two groups' signals drift apart, each stops recognising the other as a mate. No mating happens, not because bodies are incompatible but because the invitation is never answered. Signals are learned and inherited behaviours, measured by observation.
- **Numbers:** Signal match is scored 0–1 by comparing approach and display patterns; isolation is recorded when the match score falls below 0.3 and cross-group mating attempts fall below 1 per 100 generations.
- **Check:** Two groups with a match score under 0.3 show zero successful cross-group matings over 500 generations in a test run; the scores and attempt counts are logged.

**515. Mechanical isolation — bodies that do not fit**
- **Rule:** When body plans diverge enough, mating becomes physically impossible: sizes, shapes, or reproductive structures no longer fit together. Attempts may still happen but produce nothing. The failure is mechanical, measured by attempt outcomes, not assumed from size difference alone.
- **Numbers:** Mechanical isolation is recorded when at least 20 attempted pairings produce zero offspring and the size or shape difference exceeds 2× on the relevant measure (body length, reproductive structure scale).
- **Check:** A diverged pair with 0 offspring from 20 attempts is logged as mechanically isolated; a control pair with a smaller size difference still produces offspring, and both results are recorded.

**516. Gametic isolation — the meeting that fails**
- **Rule:** Even when mating happens, the reproductive cells may fail to combine: chemical mismatch, incompatible timing inside the body, or genomes that cannot pair. The pairing produces nothing, and the failure is inside the organism, invisible from outside. It is measured by offspring counts after confirmed matings, not by behaviour.
- **Numbers:** Gametic isolation is recorded when at least 20 confirmed matings produce zero offspring, while same-group matings in the same run produce offspring at a rate above 50%.
- **Check:** The confirmed-mating and offspring counts are logged per pair of lineages; a pair with 20 matings and 0 offspring is flagged, and the flag is tested against a fertile control pair.

**517. Hybrid sterility — offspring that cannot continue**
- **Rule:** Two groups may still produce offspring, but those offspring are sterile or too weak to reproduce. Gene flow is effectively zero because the hybrid line ends with its own generation. The test is not whether hybrids exist but whether they leave descendants.
- **Numbers:** Hybrid sterility is recorded when at least 10 hybrid offspring are tracked and zero of them reproduce within their normal breeding age, while same-group offspring reproduce at a rate above 50%.
- **Check:** Hybrid offspring are tracked to breeding age in a test run; the reproduction rate of hybrids versus same-group offspring is logged, and the sterility call follows the numbers.

**518. Isolation is not permanent until it is**
- **Rule:** Isolation can break: a barrier falls, a signal drifts back, a flood carries migrants across. Two groups that were isolated may meet again and merge, and the record must show the reunion, not pretend the split never happened. A species that merges back is recorded as merged, with the generation and the cause.
- **Numbers:** A reunion is recorded when gene flow rises above 1 migrant per generation sustained for 10 generations after at least 500 generations below that level. The merged lineage keeps both parent identifiers in its history.
- **Check:** A test run with a barrier that opens shows gene flow rising above the threshold and the species list updating to a merge; the before and after lists are logged.

**519. Measuring isolation without disturbing it**
- **Rule:** Isolation is measured by watching: counting crossings, encounters, matings, and offspring. The measurement never moves organisms, never forces a pairing, never opens a barrier. If a test needs a pairing that would not happen on its own, it is done in a separate diagnostic run, and the diagnostic result is labeled as such.
- **Numbers:** Observation-only metrics are logged every generation; diagnostic pairing tests run in a separate run with at least 20 pairings per pair and are labeled diagnostic in the record.
- **Check:** The main run's behaviour metrics are unchanged by the presence of logging (verified by a run with logging on versus off, same seed, same outcome); the diagnostic label appears in the log.

**520. The isolation ledger**
- **Rule:** Every isolation event is written down: which two groups, which mechanism, when it started, the measurements that support it, and whether it held or broke. The ledger is the evidence for every later speciation claim; a species without a ledger entry is an unproven claim.
- **Numbers:** One ledger entry per isolated pair per mechanism; entries are written within 100 generations of detection and kept with the checkpoint. The ledger is queryable by species identifier.
- **Check:** Every species in the record has at least one ledger entry supporting its split; an audit across ≥5 runs finds zero species without a supporting entry, and the audit result is recorded.

### 6.3 Speciation

**521. Allopatric speciation — split by separation**
- **Rule:** A population is divided by a barrier or by distance, and the two halves evolve apart until the species criterion is met. The split is recorded when isolation or distance crosses the threshold. This is the most common route to a new species.
- **Numbers:** Separation must last at least 500 generations with gene flow below 1 migrant per 100 generations; the split is recorded when the criterion in topic 501 is met. At least 5 separated pairs are tracked per run.
- **Check:** A run with a barrier produces at least one recorded split with a ledger entry, while a run with no barrier produces none from the same starting population; both outcomes are logged across ≥5 seeds.

**522. Sympatric speciation — split without separation**
- **Rule:** A new species can form inside one shared region when part of a population shifts to a new food, a new patch, or a new time of activity, and stops mating with the rest. No barrier is needed; the split is real only when gene flow actually stops.
- **Numbers:** A sympatric split is recorded when gene flow between the two habit groups falls below 1 migrant per 100 generations for 500 generations while they share the same region. The habit shift must precede the gene-flow drop by at least 50 generations.
- **Check:** A run shows a habit split followed by a gene-flow drop and a recorded split; the ordering is logged, and the result repeats across ≥3 seeds.

**523. Parapatric speciation — split across a gradient**
- **Rule:** A population spread across a gradient — wet to dry, warm to cold, rich to poor ground — adapts to different ends of the gradient. The middle still mixes, but the ends drift apart until the ends cannot interbreed, even though neighbours can. The species forms at the ends of the gradient, not at a line.
- **Numbers:** A parapatric split is recorded when the two end populations fail the species criterion test (isolation or distance) while adjacent populations still exchange genes above 1 migrant per generation. The gradient must span at least 3 distinct resource levels.
- **Check:** End populations are tested as different species while adjacent pairs test as the same species, in a run with a measured gradient; the pairwise test matrix is logged.

**524. Peripatric speciation — a small group breaks away**
- **Rule:** A small group at the edge of a population — a few founders carried to a new patch — evolves fast because its gene pool is small and every mutation matters more. It can become a new species while the large parent population barely changes. The founders' descendants are a species when the criterion is met, not merely because they are few.
- **Numbers:** A founder group is 2–20 individuals; the split is recorded when the criterion is met after at least 200 generations of separation with gene flow below 1 migrant per 100 generations.
- **Check:** A founder-group run shows faster divergence (distance growth per generation at least 2× the parent population's rate) and a recorded split; the divergence rates are logged across ≥5 seeds.

**525. Speciation by polyploidy and sudden change**
- **Rule:** A reproduction error can double or change the genome in one generation, making the offspring instantly unable to breed with its parents while able to breed with others like it. This is a single-step split, and it counts as a species when the offspring line persists and the criterion is met. It is rare and must be measured, not assumed.
- **Numbers:** A sudden-change split is recorded when a genome-scale change (duplication or rearrangement above 10% of the genome) appears in one generation, the carriers are isolated from the parent population in the same generation, and the line survives at least 50 generations.
- **Check:** A run containing such an event logs the generation, the genome change size, and the carrier line's survival; confirmed by genome comparison, not by appearance.

**526. Hybrid speciation — a new species from a mix**
- **Rule:** Two species can cross to produce offspring that breed among themselves but not with either parent, forming a third species from the mixture. The hybrid line must persist, breed true, and stay isolated from both parents. A single hybrid generation is not a species; a self-sustaining hybrid population is.
- **Numbers:** Hybrid speciation is recorded when a hybrid line survives at least 100 generations, breeds among itself at a rate above 50%, and shows zero fertile offspring with either parent across at least 20 attempted pairings each.
- **Check:** A hybrid line meeting all three numbers is logged as a new species with both parents recorded; the pairing tests and survival curve are stored in the run log.

**527. How fast can a species form**
- **Rule:** Speciation speed depends on population size, mutation rate, selection strength, and how complete the isolation is. Small isolated groups under strong selection split fastest; large connected populations split slowest or never. The speed is measured in generations from separation to criterion, and no target speed is set — the world reports what it does.
- **Numbers:** Time-to-split is logged for every recorded split in generations; the run reports the median and the range across splits. Starting expectation from real-world analogues is 200–20,000 generations, but the measured number is what counts.
- **Check:** The time-to-split distribution is logged per run across ≥5 seeds; a split recorded faster than 50 generations triggers a review of the measurement, not an automatic acceptance.

**528. Speciation is a process, not a moment**
- **Rule:** A split is not one tick where a species appears. Isolation builds, distance grows, and the criterion is crossed at a generation that can be named only after the fact. The record therefore stores the whole path — first isolation, distance curve, criterion crossing — and the species' birth generation is the crossing generation, honestly labeled as a measurement point, not a magic instant.
- **Numbers:** Each split stores the isolation start generation, the distance at 10-generation intervals, and the crossing generation. The crossing is confirmed by a second measurement 50 generations later.
- **Check:** Every recorded split has a complete path in the ledger (isolation start, distance curve, crossing, confirmation); an audit across ≥5 runs finds zero splits missing any part.

**529. Speciation needs a falsifier**
- **Rule:** The claim "a new species formed" must be falsifiable: if the two groups still interbreed freely, or their distance is below threshold, the claim fails. Every split is tested against that falsifier before it is recorded, and a failed test is logged as a failed test, not hidden. A species that cannot pass its own test does not exist in the record.
- **Numbers:** The falsifier test is at least 20 attempted pairings plus a distance measurement; the split is recorded only when the falsifier fails (isolation or distance holds). Failed tests are logged at the same rate as passed ones.
- **Check:** A control run with no isolation produces zero recorded splits, and a run with forced gene flow shows the split claim failing its test; both are logged.

**530. The speciation record and sign-off**
- **Rule:** Speciation work is done when splits are recorded with full paths, the falsifier has been applied, and the numbers are in the emergence log. The record lists every split, its mechanism, its timing, and its evidence, plus every failed test. Muse reviews the record before the phase moves on; nothing is claimed from an unreviewed list.
- **Numbers:** The record contains at least 1 split per run across ≥5 seeds (or a recorded explanation of why none formed), with 100% of splits carrying a complete path. The review is recorded with a date.
- **Check:** The species record passes an audit (every split has a path, every failed test is logged, the count matches the ledger) and the review is recorded; the audit result is stored in the emergence log.

### 6.4 Extinction

**531. Background extinction — the ordinary end**
- **Rule:** Most species end quietly: their food thins, a better competitor arrives, their numbers fall below the level that can sustain breeding, and the last member dies. No catastrophe is needed. The species' end is recorded with its cause — the measured decline, not a guess — and its lineage stays in the historical record.
- **Numbers:** A species is extinct when zero living members remain for 100 consecutive generations. Background extinction is the baseline rate: the run reports extinctions per 1,000 generations, with the starting expectation of 1–10 per 1,000 generations.
- **Check:** Every extinction is logged with species, last generation, and the population curve of its final 100 generations; the background rate is computed per run across ≥5 seeds.

**532. Mass extinction — many at once**
- **Rule:** A large shock — a climate shift, a chemical change in the water, a collapse of a food source — can kill many species in a short span. Which species survive depends on their traits and luck.
- **Numbers:** A mass extinction is recorded when more than 50% of living species disappear within 500 generations, against a background rate below 10% per 500 generations. The shock's size (temperature, chemistry, or resource change) is logged with its cause.
- **Check:** A shock run shows the species count falling by more than 50% within 500 generations while a no-shock control run stays within background rates; both curves are logged across ≥3 seeds.

**533. Why death is permanent for a lineage**
- **Rule:** When the last member of a species dies, the species is gone for good. Its genome, its behaviours, its adaptations — all of it ends, because there is no organism left to carry them. Nothing revives it: no reset, no re-seeding from the record, no recreation from a fossil. The lineage's information survives only as history, never as a living organism.
- **Numbers:** Zero revivals is the rule; any reappearance of an extinct species identifier in the living population is flagged as an error and investigated. The historical record keeps the extinct species indefinitely.
- **Check:** An audit across ≥5 runs finds zero living members carrying an extinct species identifier; the audit result is recorded, and any flagged reappearance blocks the phase sign-off until explained.

**534. Extinction debt — the slow fall**
- **Rule:** A species can be doomed long before its last member dies: its habitat shrinks, its numbers fall below a viable breeding size, and the remaining members are too few or too scattered to recover. The population keeps falling even if conditions stop worsening. The debt is measured by the population trend, and the species is flagged as committed before it is gone.
- **Numbers:** A species is flagged as committed when its population falls below 10 breeding members for 50 generations and the trend over those 50 generations is still downward. The flag is written to the ledger.
- **Check:** Flagged species go extinct within 500 generations in at least 80% of cases across ≥5 runs; the flag accuracy is logged and the misses are reviewed.

**535. Competitive exclusion — one way of life wins**
- **Rule:** Two species living the same way in the same place cannot both last: the one that uses the shared resource even slightly better takes more of it each generation, and the other starves out. The exclusion is measured by resource share and population trends, not assumed from similarity.
- **Numbers:** Exclusion is recorded when two species share over 80% of their food sources and one species' share of that food rises above 90% while the other's population falls for 100 generations. The food-overlap and share numbers are logged.
- **Check:** A run with two species sharing over 80% of food shows one species' share rising and the other's population falling, ending in extinction; the curves are logged across ≥3 seeds.

**536. Extinction cascades — one loss pulls others down**
- **Rule:** Species depend on each other: one eats another, one shelters another, one pollinates or carries another's offspring. When one species dies, the species that depended on it lose food or shelter and may follow. The cascade is measured by tracking who depended on whom before the first loss, and the record shows the chain.
- **Numbers:** A cascade is recorded when at least 2 further species go extinct within 200 generations of a first extinction, and dependency links (food or shelter share above 50%) existed between them. The dependency links are logged before the cascade.
- **Check:** A run with a recorded dependency network shows the cascade pattern after a first extinction; the network and the extinction order are logged, and a control run without the dependency shows no cascade.

**537. Refugia — where survivors hide**
- **Rule:** During a bad period, a few places stay liveable while the rest of the world turns hostile: a sheltered bay, a deep pool, a warm vent. Species that reach a refuge survive; species that do not, die. Which species find them depends on where they already lived and how far they can travel.
- **Numbers:** A refuge is a patch where conditions stay within the survival range while the surrounding region falls outside it for at least 100 generations. Survival through a shock is compared between species with and without refuge access.
- **Check:** During a shock run, species with refuge access survive at least 2× the rate of species without it; the refuge locations and survival rates are logged across ≥3 seeds.

**538. Recovery after loss — the world refills**
- **Rule:** After extinctions, empty niches are re-occupied by the survivors' descendants, which diverge into new species over time. Recovery is not a return to the old species; the old ones are gone. The new species are different, built from whoever survived, and the recovery is measured by species count and diversity returning toward their old levels over generations.
- **Numbers:** Recovery is measured as the generations needed for species count to return to 80% of its pre-extinction level; the starting expectation is 1,000–10,000 generations. Diversity (trait spread) is tracked alongside the count.
- **Check:** After a shock run, the species count and diversity curves are logged until they reach 80% of pre-shock levels or 10,000 generations pass; the recovery time is recorded per run across ≥3 seeds.

**539. The extinction ledger**
- **Rule:** Every extinction is written down: species, last generation, last population size, the measured cause (starvation, competition, shock, or unknown with the evidence), and the species it leaves behind in the record. The ledger is the permanent history of what lived and died; it is never edited to make the story neater.
- **Numbers:** One entry per extinct species, written within 100 generations of the last member's death, kept with the checkpoint. The cause field is one of the measured causes, or "unknown" with the supporting numbers attached.
- **Check:** The number of ledger entries matches the number of species that have ever existed minus the number currently living, within 0; the reconciliation is tested on ≥5 runs and recorded.

**540. Extinction is information, not failure**
- **Rule:** An extinction is a measurement, not a mistake to fix. It tells the project which ways of life work and which do not, under which conditions. The response to an extinction is to record it and learn from it, never to revive the species, restock its niche, or tune the world to save it.
- **Numbers:** The run reports extinctions per 1,000 generations and the fraction of species that ever go extinct; a run with zero extinctions over 5,000 generations is flagged for review of whether selection pressure exists.
- **Check:** The extinction rate and the zero-extinction flag are logged per run; a flagged run is reviewed and the review recorded before the phase is signed off.

### 6.5 Deep time

**541. The world runs long enough for deep time**
- **Rule:** Evolution needs time measured in thousands to millions of generations, and the world runs continuously, 24/7, with no planned end, so that time is available. Deep time is not a setting to switch on; it is the consequence of a world that never stops. The run's age is measured in generations and ticks, and the record keeps growing with it.
- **Numbers:** The world runs without a tick cap; the run reports total generations, total ticks, and wall-clock days elapsed. The first deep-time checkpoint is 10,000 generations; the record is kept in full to that point.
- **Check:** A run reports its generation count increasing without a cap across a 7-day continuous window, with checkpoints resuming correctly; the generation count and checkpoint integrity are logged.

**542. Generations as the clock**
- **Rule:** The clock that matters for evolution is the generation: one full cycle of birth to reproduction. Wall-clock time and tick counts are recorded too, but generation is the unit in which change is measured, because selection acts once per generation. Every measurement — diversity, distance, extinction — is indexed by generation.
- **Numbers:** Generation is counted per lineage (the deepest chain) and per population (the median chain); both are logged every 100 generations. A generation at cell scale is one division cycle; at larger scales it is one birth-to-breeding cycle.
- **Check:** The generation count increases monotonically in the log with no resets; a lineage query returns the generation of any organism, and the count is verified against the birth log on ≥5 runs.

**543. Rates of change — fast and slow**
- **Rule:** Evolution is not one speed. Some traits change in a few generations under strong selection; others barely move for thousands. The run measures the rate of change per trait (change per generation) so fast and slow evolution are both visible, and neither is treated as the normal speed. A trait that never changes is a finding, not a missing measurement.
- **Numbers:** Rate of change is reported per trait as change per 100 generations, with the population mean and spread. Fast is above 0.1 standard deviations per 100 generations; slow is below 0.01. Both are logged.
- **Check:** The rate table is produced per run across ≥5 seeds; at least one fast and one slow trait are identified in each run, or the absence of either is recorded with the numbers.

**544. Stasis — long periods of no change**
- **Rule:** A species can stay nearly the same for thousands of generations when its niche is stable and selection holds it in place. Stasis is not a failure of evolution; it is selection working to keep what works. The record shows stasis as a flat trait curve, and it is reported as stasis, not as a gap in the data.
- **Numbers:** Stasis is recorded when a species' trait means move less than 0.1 standard deviations over 1,000 generations while the species survives and reproduces. The flat curve is logged with the species' population numbers.
- **Check:** At least one species per run shows a stasis interval of 1,000 generations or the run records why none did; the trait curves are stored in the run log.

**545. Punctuated change — long calm, sudden shift**
- **Rule:** Change often comes in bursts: long stable periods broken by rapid shifts when conditions change or a new niche opens. The record must show both the calm and the burst, with the trigger — a shock, a new food, a barrier falling — logged alongside the shift.
- **Numbers:** A burst is a trait shift above 1 standard deviation within 100 generations, following at least 1,000 generations of stasis (movement under 0.1 standard deviations). The trigger event and its generation are logged with the burst.
- **Check:** Burst events are listed per run with their triggers; at least one burst per run is checked against its trigger (the trigger precedes the burst by under 100 generations), and the check is recorded.

**546. The molecular clock — distance as a timer**
- **Rule:** Genetic distance grows roughly steadily when mutations accumulate at a steady rate, so distance can be read as a rough timer for when two lineages split. The clock is calibrated from measured splits, not assumed: the mutation rate per generation is measured, and the distance-to-time conversion is reported with its uncertainty. It is a timer with error bars, never a precise date.
- **Numbers:** The mutation rate is measured as substitutions per genome per generation, logged per run; the clock is calibrated from at least 5 known splits, and the calibration error (in generations) is reported alongside every estimate.
- **Check:** The clock's estimate for a known split falls within its stated error bars in at least 4 of 5 calibration cases; the calibration table is stored in the run log.

**547. Deep time needs deep records**
- **Rule:** A world that runs for millions of generations produces more history than can be kept in full detail, so the record is kept in layers: every event for the recent past, summaries per 100 generations for the middle past, and per-1,000-generation summaries for the deep past. No layer is deleted, and the full lineage tree is kept at all depths.
- **Numbers:** Full event logs are kept for the last 10,000 generations; 100-generation summaries cover 10,000–100,000 generations; 1,000-generation summaries cover beyond 100,000. The lineage tree is kept complete regardless of depth.
- **Check:** A lineage query reaches generation 0 from any living organism, and a summary at any depth matches a recount from the fuller layer within 1%; both are tested on runs of at least 10,000 generations.

**548. Contingency — history could have gone otherwise**
- **Rule:** Evolution is contingent: a chance mutation, a lucky survivor, a barrier that happened to fall can change everything downstream, and the same starting conditions can lead to different worlds. The project measures this by running the same starting conditions with different random streams and comparing outcomes.
- **Numbers:** Contingency is measured across at least 5 seeds with identical starting conditions: the species count, the dominant traits, and the number of splits are compared, and the spread across seeds is reported as the contingency measure.
- **Check:** The cross-seed spread is logged per run set; if all 5 seeds produce identical species, that is flagged as a sign that the outcome is forced by the rules rather than evolved, and the flag is recorded.

**549. Deep time is honest about what is unknown**
- **Rule:** Over deep time, some things cannot be known: the exact first member of a species, the precise generation of a split, the cause of an extinction with no surviving evidence. The record marks these as unknown with the evidence that is missing, instead of filling the gap with a plausible story. An honest unknown is a valid entry.
- **Numbers:** Unknown fields are counted per run; the record reports the fraction of splits and extinctions with a fully known cause versus an unknown cause. No field is filled by guesswork.
- **Check:** An audit of the record finds zero entries where a cause was stated without supporting numbers; the audit result is recorded per run, and any invented cause found is corrected to unknown.

**550. The deep-time record and sign-off**
- **Rule:** Deep-time work is done when the world has run long enough to show stasis, bursts, and splits, the record layers are in place, the molecular clock is calibrated, and the contingency measure is reported. Muse reviews the record and the numbers before the phase moves on; a world that has only run a few hundred generations has not done deep time.
- **Numbers:** The sign-off run has at least 10,000 generations, at least 5 splits, at least 1 mass or background extinction event, and a calibrated clock with its error bars. The review is recorded with a date.
- **Check:** The sign-off checklist (generations, splits, extinctions, clock, contingency, record layers) is verified against the run log and the audit passes; the result is stored in the emergence log.

### 6.6 Major transitions

**551. From single cells to colonies**
- **Rule:** The first major transition is cells staying together after division instead of drifting apart, forming a colony where cells share food and protection. The colony is not yet a body — each cell still reproduces on its own — but staying together must pay: colonies survive better than loners in the same patch, or the transition never takes hold.
- **Numbers:** A colony is 2–100 cells staying within 1 body-length of each other for at least 50 generations; the transition is recorded when colonies show survival at least 20% higher than solitary cells in the same patch across ≥5 seeds.
- **Check:** Colony survival versus solitary survival is logged per run; the transition counts only when the 20% advantage holds, and the comparison is recorded.

**552. From colonies to bodies with a germ line**
- **Rule:** The next transition is division of labour between body cells and reproductive cells: most cells give up reproducing so that a few can, and the body becomes the unit that reproduces. This only holds when the body's survival gains outweigh the lost reproduction of its body cells, and cheating (a body cell reproducing anyway) is counted when it happens.
- **Numbers:** A germ line is recorded when fewer than 10% of a body's cells reproduce, the body reproduces as a unit, and body survival exceeds colony survival by at least 20%. Cheating events are counted per run.
- **Check:** The reproductive fraction, body survival, and cheating count are logged; the transition is recorded only when all three numbers meet their bars, and the result is stored in the run log.

**553. From bodies to sexes**
- **Rule:** Reproduction can split into two roles — one producing many small reproductive cells, the other producing few large ones — when mixing genes from two parents pays better than cloning. Sexes appear when the two-role system out-reproduces the single-role system in the same conditions, and the split is measured by reproductive success, not by appearance.
- **Numbers:** Two sexes are recorded when a population shows two distinct reproductive roles, cross-role mating produces offspring at a rate above 50%, and the two-role population's reproduction rate exceeds a single-role control by at least 10% across ≥5 seeds.
- **Check:** The role split, mating success, and reproduction comparison are logged; the transition counts only when the 10% advantage holds, and the numbers are recorded.

**554. From individuals to eusocial groups**
- **Rule:** A further transition is a group where most members never reproduce and instead raise the offspring of a few — a colony that acts like one organism. It holds only when relatedness is high enough that helping relatives passes on more shared genes than breeding alone would, and the group must out-survive solitary living in the same niche.
- **Numbers:** A eusocial group is recorded when fewer than 5% of members reproduce, average relatedness within the group exceeds 0.5, and group survival exceeds solitary survival by at least 20% across ≥5 seeds.
- **Check:** The reproductive fraction, relatedness, and survival comparison are logged; the transition is recorded only when all three bars are met, and the result is stored.

**555. From groups to multicellular complexity**
- **Rule:** Bodies can grow more complex — more cell types, more tissues, more specialised organs — when each new specialisation pays for itself in survival or reproduction. Complexity is measured by the count of distinct cell roles and the coordination between them; a new role that adds cost without benefit is selected against.
- **Numbers:** Complexity is the count of distinct cell roles per body, logged per generation; a complexity increase is recorded when the role count rises by at least 1 and the body's survival or reproduction does not fall over the next 100 generations.
- **Check:** The role count and survival curves are logged per run; a role increase followed by a survival fall is recorded as a failed step, and the failures are counted.

**556. Transitions are rare and hard**
- **Rule:** Major transitions do not happen often, and most attempts fail: colonies break up, germ lines are invaded by cheaters, eusocial groups collapse. The project records failed transitions alongside successful ones, because a transition that always succeeds is a sign the rules are too easy. Rarity is a measurement, not a disappointment.
- **Numbers:** Transition attempts are counted (a colony forming, a germ line appearing) and successes are counted separately; the success rate is reported per transition type. A success rate above 50% per attempt is flagged for review of whether the bar is too low.
- **Check:** The attempt and success counts are logged per run across ≥5 seeds; the success rates are reported in the emergence log, and any flagged rate is reviewed with the review recorded.

**557. Cheating and the policing of transitions**
- **Rule:** Every transition creates a chance to cheat — a cell that takes the group's food without contributing, a body cell that reproduces, a worker that breeds. Cheating is measured by counting it, and transitions survive only when cheating is rare or policed (by relatedness, by punishment, by the cheat's own cost). A transition with unmeasured cheating is an unproven claim.
- **Numbers:** Cheating is counted as events per 1,000 generations per transition type; a transition is stable when cheating stays below 1 event per 100 generations or when cheating lineages die out within 50 generations.
- **Check:** The cheating counts and the fate of cheating lineages are logged; a transition is recorded as stable only when the cheating numbers meet the bar, and the result is stored.

**558. Transitions change what selection acts on**
- **Rule:** Each transition moves selection to a new level: first cells are selected, then colonies, then bodies, then groups. The record must say which level selection is acting on at each stage, measured by where the survival and reproduction differences appear — between cells, between bodies, or between groups. If the level is wrong, the explanation of the transition is wrong.
- **Numbers:** The selection level is measured by comparing variance in survival between units at each level (cells within a body, bodies within a group, groups within a population); the level with the largest between-unit variance is the level selection acts on.
- **Check:** The variance comparison is computed per run and logged; the recorded selection level matches the measured one, and a mismatch triggers a review recorded in the log.

**559. Transitions open new niches**
- **Rule:** A new kind of body can live in places the old kind could not: a colony can hold ground a single cell cannot, a body with sexes can colonise a patch that needs gene mixing. Each transition is followed by a measurement of which new niches open, recorded as discovered, not assigned.
- **Numbers:** New niches are counted as food sources or patches usable by the new form but not by the old form, measured by survival above the breeding threshold in each. At least 1 new niche per successful transition is expected, and the count is logged.
- **Check:** The niche count before and after each transition is logged; a transition with zero new niches is recorded as such and reviewed.

**560. The transitions record and sign-off**
- **Rule:** Transitions work is done when each transition type has its attempts, successes, cheating counts, selection level, and new niches recorded, with at least one successful transition of each type that the world has reached, or a recorded explanation of why a type has not appeared. Muse reviews the record before the phase moves on.
- **Numbers:** The record covers at least 5 runs of ≥5,000 generations each, with attempt and success counts per transition type. The review is recorded with a date.
- **Check:** The record passes an audit (every claimed transition has its numbers, every failed attempt is counted, the selection levels match the measurements) and the review is recorded; the audit result is stored in the emergence log.

### 6.7 Convergence

**561. Convergence — different ancestors, same solution**
- **Rule:** Unrelated lineages facing the same problem can evolve the same solution: streamlined bodies for moving through water, light-sensing patches for finding brightness, gripping shapes for holding food. Convergence is measured by comparing traits against ancestry — the traits match while the lineages do not.
- **Numbers:** Convergence is recorded when two lineages with a genetic distance above the species threshold share a trait within 0.2 standard deviations on a measured scale (speed, sensing range, body shape), while their other traits differ by more than 1 standard deviation.
- **Check:** Convergent pairs are listed per run with their distances and trait values; at least 1 convergent pair per run is expected once 3 or more species exist, and the list is logged.

**562. The problem sets the shape**
- **Rule:** The same physical problem pushes different bodies toward the same shape because physics allows only a few good answers: water resistance punishes bulk, light rewards a focused sensor, gripping rewards a hook. The run measures the problem (drag, light level, grip force) alongside the shape, so the link between problem and solution is evidence, not a story.
- **Numbers:** The problem is measured in physical units (drag force, light intensity, grip force) per patch; the shape is measured in the same run. A convergence claim requires the problem to be within 20% the same across the two lineages.
- **Check:** The problem measurements and shape measurements are logged together per convergent pair; a pair claimed convergent without matching problem numbers is rejected, and the rejection is recorded.

**563. Convergence is not identity**
- **Rule:** Convergent solutions look alike in function but differ in build: two light sensors may both detect brightness yet be built from different cell types and wired differently. The record notes the functional match and the structural difference separately, because mistaking convergence for shared ancestry would corrupt the tree of life.
- **Numbers:** Functional match is scored 0–1 on performance (detection range, speed, grip strength); structural difference is scored by the count of different cell roles used to build the trait. A convergent pair shows functional match above 0.8 with structural difference above 0.
- **Check:** Both scores are logged per convergent pair; a pair with matching function and identical structure is flagged for a shared-ancestry check instead of being logged as convergence.

**564. Divergence — same ancestor, different solutions**
- **Rule:** The counterpart of convergence is divergence: one ancestor's descendants solve different problems in different ways — one lineage takes to the water, another to the shore — and their traits spread apart while their ancestry stays shared. Divergence is measured by trait spread growing while genetic distance stays below the species threshold at first, then crossing it as the species split.
- **Numbers:** Divergence is recorded when two descendant lineages differ by more than 2 standard deviations on at least 1 trait while their genetic distance is still below the species threshold, with the split following within 1,000 generations.
- **Check:** Divergent pairs are listed per run with their trait gaps and distances; the ordering (trait gap first, split second) is logged, and the result is repeated across ≥3 seeds.

**565. Parallel evolution — close cousins, same answer**
- **Rule:** Closely related lineages can independently evolve the same trait because they start from similar bodies and similar genes. This is parallel evolution, not convergence from afar and not shared inheritance: the trait appears separately in each line after they split. The record distinguishes it by showing the trait absent in the common ancestor and present in both descendants.
- **Numbers:** Parallel evolution is recorded when a trait appears in two descendant lineages within 500 generations of their split, is absent in the reconstructed ancestor, and the lineages' genetic distance is below 2× the species threshold.
- **Check:** The ancestor reconstruction and the appearance generations are logged per parallel pair; a trait present in the ancestor is reclassified as inherited, not parallel, and the correction is recorded.

**566. Constraints — why only a few answers exist**
- **Rule:** Physics and chemistry limit the answers: a body can only move so fast for its size, a sensor can only be so sensitive for its cost, a structure can only be so strong for its material. The run measures them as hard limits — the maximum speed, the minimum cost — so the limits are numbers, not intuitions.
- **Numbers:** Each constraint is stated as a measured limit (for example, maximum speed per energy cost, minimum sensor cost per tick) and logged per body plan. Convergence claims cite the constraint that forces the shared answer.
- **Check:** The constraint limits are measured per run and logged; a convergence claim without a cited constraint is returned for more evidence, and the return is recorded.

**567. Convergence as a test of the world**
- **Rule:** If the world's physics is consistent, the same problem in two separate places should produce similar answers; if it does not, either the problems differ or the rules are inconsistent. Convergence is therefore a test of the world itself: repeated convergence across independent lineages is evidence the rules are stable, and its absence where it is expected is a finding to investigate.
- **Numbers:** The test is the count of convergent pairs per run once 5 or more species exist; the starting expectation is at least 1 pair per run, and a run with 5 or more species and zero pairs is flagged for review.
- **Check:** The convergent-pair count and the flag are logged per run; flagged runs are reviewed and the review recorded before the phase is signed off.

**568. Exaptation — an old trait finds a new job**
- **Rule:** A trait built for one purpose can be reused for another: a structure that sensed light becomes a structure that signals to mates, a gripping shape becomes a digging tool. The reuse is measured by tracking the trait's function over time — the old function fades, the new one grows.
- **Numbers:** An exaptation is recorded when a trait's measured contribution to its old function falls below 20% of its total benefit while its contribution to a new function rises above 80%, sustained for at least 100 generations.
- **Check:** The function-contribution curves are logged per exaptation event; at least 1 event per run is expected once 5 or more species exist, and the curves are stored in the run log.

**569. Convergence in minds, not only bodies**
- **Rule:** Minds can converge too: unrelated lineages can evolve the same learning trick, the same memory use, or the same curiosity pattern, because the same survival problem rewards the same mental solution. Mental convergence is measured the same way as bodily convergence — same performance, different ancestry — using the mind's measured behaviour, not its appearance.
- **Numbers:** Mental convergence is recorded when two lineages above the species threshold show the same learning rate (within 20%) and the same memory use pattern (within 20%) on a shared foraging task, while their body plans differ by more than 1 standard deviation.
- **Check:** The learning-rate and memory-use measurements are logged per convergent pair; the foraging-task results are stored, and a pair failing the 20% bars is not logged as convergent.

**570. The convergence record and sign-off**
- **Rule:** Convergence work is done when convergent, divergent, parallel, and exaptation events are recorded with their measurements, the constraints behind them are stated, and the world-consistency test has been applied. Muse reviews the record before the phase moves on; a list of similar-looking traits without ancestry checks is not a convergence record.
- **Numbers:** The record covers at least 5 runs, with at least 1 convergent pair and 1 divergent pair per run once 3 or more species exist. The review is recorded with a date.
- **Check:** The record passes an audit (every convergent pair has an ancestry check, every claim cites a constraint, the world-consistency test result is present) and the review is recorded; the audit result is stored in the emergence log.

### 6.8 The tree of life

**571. The tree is built from ancestry, not appearance**
- **Rule:** The tree of life is drawn from who descended from whom — parent to offspring, lineage to lineage — not from which organisms look alike. Appearance can mislead, but ancestry does not lie when the birth records are complete. Every branch in the tree is a recorded birth chain, and every split is a recorded speciation event.
- **Numbers:** The tree is built from the birth log: each organism links to its parent, each species to its parent species. The tree is complete when every living organism traces to the first cell with no gaps, verified on ≥5 runs.
- **Check:** A lineage query from any living organism returns an unbroken chain to generation 0; tested on a sample of at least 100 organisms per run, and the result is recorded.

**572. Branches and nodes — splits in the record**
- **Rule:** A node in the tree is a speciation event: one lineage becoming two. A branch is a lineage between splits. Nodes are placed at the generation the species criterion was crossed, and branches carry the traits of the lineage between nodes. A tree with nodes placed by guesswork is a picture, not a measurement.
- **Numbers:** Each node stores the split generation, the mechanism, and the trigger value; each branch stores the trait means of its lineage. Nodes are placed within 50 generations of the measured crossing.
- **Check:** Every node in the tree resolves to a ledger entry with its trigger value; an audit across ≥5 runs finds zero nodes without a supporting entry, and the audit result is recorded.

**573. The tree is a measurement, not a design**
- **Rule:** Nobody draws the tree in advance or decides its shape. The tree is computed from the birth and speciation logs after the fact, and its shape — bushy or sparse, balanced or lopsided — is whatever the world produced. If the tree looks tidy, that is a finding about the world, not a sign the tree was arranged.
- **Numbers:** The tree is recomputed from the logs at least once per 1,000 generations; its shape is reported as branch counts per depth level and the balance (the ratio of the largest to smallest branch at each level). Zero hand-placed branches is the target.
- **Check:** A recomputation from the raw logs reproduces the stored tree exactly (same nodes, same branches); the recomputation is tested on ≥5 runs and the result recorded.

**574. Extinct branches stay on the tree**
- **Rule:** A branch that ends in extinction stays on the tree with its end generation marked. Pruning dead branches would lie about the past: it would hide how many lineages tried and failed, and make the survivors look inevitable. The tree shows the dead ends as dead ends, with their full length and their cause of death where known.
- **Numbers:** Extinct branches are kept indefinitely; each carries its end generation and cause. The tree reports the fraction of branches that are extinct (starting expectation: over 50% after 10,000 generations).
- **Check:** The count of extinct branches in the tree matches the extinction ledger within 0; the reconciliation is tested on ≥5 runs and recorded.

**575. The root — one origin for all**
- **Rule:** Every living thing in the world traces back to the same first replicators, so the tree has one root. The root is the first cell lineage from the origin of life, and every branch connects to it through an unbroken chain of births. If a lineage cannot be traced to the root, either the record is broken or something was placed, and either way it is investigated.
- **Numbers:** The root is generation 0; the trace from any living organism to the root is tested on a sample of at least 100 organisms per run, with zero failures allowed. Any failure is logged as a record error.
- **Check:** The root-trace test passes on ≥5 runs with zero failures; any failure is investigated and recorded before the phase is signed off.

**576. Reading the tree — what it tells us**
- **Rule:** The tree answers questions: which species are closest cousins, when two lineages split, how many times a trait appeared, whether a group is one lineage or several. Each answer is computed from the tree and reported with its uncertainty (the split generation plus or minus the measurement error). An answer without its uncertainty is an overclaim.
- **Numbers:** Cousin distance is measured in generations to the shared node; split times carry the error from the molecular clock calibration (topic 546). At least 3 questions per run are answered from the tree and logged with their uncertainties.
- **Check:** The answers are recomputed from the raw logs and match the tree's answers within the stated error; the recomputation is tested on ≥5 runs and recorded.

**577. The tree grows with the world**
- **Rule:** The tree is not built once; it grows every generation as births happen and splits are recorded. New branches appear, old branches end, and the tree's size is the size of the world's history. The tree's storage grows with the world, and the storage budget is measured so the tree never silently stops growing.
- **Numbers:** Tree size is reported as node count and branch count per 1,000 generations; storage cost is logged in megabytes per 10,000 generations. The budget is set so the tree can grow to at least 1,000,000 nodes.
- **Check:** The node count increases monotonically with generations and matches the birth log's species count within 0; the check is tested on runs of at least 10,000 generations and recorded.

**578. The tree is shared with the views**
- **Rule:** The tree is part of what the Command Center shows: the history of life, browsable from the present back to the root. The view reads the tree through the Gateway, the same read-only feed as everything else, and the view changes nothing. A tree the viewer cannot see is a record nobody can use.
- **Numbers:** The tree is served through the Gateway snapshot (species list, parent links, split generations) at least once per 100 generations; the view shows at least the top 3 levels (planet, species, lineage) with counts.
- **Check:** A Gateway snapshot contains the species list and parent links matching the run log within 0; the match is tested on a live feed and recorded. The viewer labels the tree as the measured record, not a design.

**579. The tree can be wrong — and corrected**
- **Rule:** A tree built from measurements can be wrong: a split misdated, a branch misplaced, a convergence mistaken for shared ancestry. When new evidence corrects the tree, the correction is recorded with the old value, the new value, and the evidence — the tree is versioned, and old versions are kept so the correction itself is part of the history.
- **Numbers:** Corrections are versioned (tree v1, v2, …) with the generation of the correction and the evidence cited. The correction rate is reported per run; a rate above 5% of nodes corrected triggers a review of the measurement method.
- **Check:** The version history is stored with the checkpoints; a corrected tree still traces every organism to the root with zero failures, and the correction log is audited on ≥5 runs.

**580. The tree record and sign-off**
- **Rule:** Tree work is done when the tree is complete to the root, extinct branches are kept, the tree is served to the views, and the correction process is in place. Muse reviews the tree and the numbers before the phase moves on; a tree that cannot be recomputed from the logs is not a record.
- **Numbers:** The sign-off tree covers at least 10,000 generations, at least 5 species, and at least 1 extinct branch, with the recomputation test passing. The review is recorded with a date.
- **Check:** The sign-off checklist (root trace, node ledger, extinct branches, recomputation, view feed, correction log) is verified against the run log and the audit passes; the result is stored in the emergence log.

### 6.9 Fossils and memory

**581. Fossils — the record left in the ground**
- **Rule:** When organisms die, some trace remains: a body in sediment, a shell, a track, a chemical mark in the ground. These traces are fossils, the world's own memory of what lived — formed by burial, mineralisation, and preservation, not placed as exhibits. A fossil records that something lived, where, and roughly when.
- **Numbers:** Fossil formation is a measured rate: the fraction of dead organisms that leave a trace, logged per run, with a starting expectation of 0.1–1%. Each fossil stores the species, the generation, and the location. The fossil count is reported per 1,000 generations.
- **Check:** The fossil record is compared against the birth and death logs: every fossil resolves to a species that existed at that generation, and the rate is logged per run across ≥5 seeds.

**582. What fossils preserve and what they lose**
- **Rule:** Fossils are incomplete: hard parts preserve better than soft ones, big bodies better than small ones, quiet water better than fast currents. The record must say what is missing, so nobody reads the fossil record as a complete census. The bias is measured by comparing the fossil species list against the true species list.
- **Numbers:** Preservation bias is reported as the fraction of true species represented in the fossil record and the fraction of traits preserved per fossil; the starting expectation is that fewer than 50% of species leave fossils. The bias is logged per run.
- **Check:** The fossil species list is compared with the true species list per run; the representation fraction is logged, and a run claiming a complete fossil list is flagged for review.

**583. Reading fossils without inventing stories**
- **Rule:** A fossil shows a shape, a size, a location, and a layer — nothing more. What the organism did, how it lived, why it died are inferences, and each inference must be labeled as such with the evidence behind it. A fossil that is read as a fact about behaviour without evidence is an overclaim, and the record corrects it.
- **Numbers:** Every fossil-based claim carries a confidence level (high, medium, low) and the evidence cited; claims with no evidence are not entered. The fraction of fossil claims at each confidence level is reported per run.
- **Check:** An audit of fossil claims finds zero claims without cited evidence across ≥5 runs; the audit result is recorded, and any unsupported claim is downgraded to low confidence or removed.

**584. Trace fossils — tracks, burrows, marks**
- **Rule:** Not all fossils are bodies: tracks, burrows, feeding marks, and nests are traces of behaviour left in the ground. They are measured by their shape, size, and depth. A track is evidence of movement; it is not evidence of the track-maker's species unless a body fossil links the two.
- **Numbers:** Trace fossils are logged with type, size, depth, and generation; the link between a trace and a species is recorded only when a body fossil of that species is found in the same layer within 10 generations. Unlinked traces are labeled as unlinked.
- **Check:** The trace log is compared against the behaviour log: traces appear only in generations where the corresponding behaviour (movement, digging, feeding) was recorded, and the match rate is logged per run.

**585. The fossil record is layered in time**
- **Rule:** Fossils sit in layers, older below and younger above, because sediment builds up over time. The layer order is the time order, and it is measured by depth and by the generations of the fossils in each layer. A fossil found out of order — a young species in an old layer — is a finding to investigate (disturbance, reworking), not an error to delete.
- **Numbers:** Layers are dated by the generation range of their fossils; at least 10 layers per run are expected after 10,000 generations, each spanning roughly 1,000 generations. Out-of-order fossils are counted and logged.
- **Check:** The layer order matches the generation order for at least 95% of fossils per run; the match rate and the out-of-order count are logged, and out-of-order cases are investigated.

**586. Living fossils — species that barely change**
- **Rule:** Some species survive for thousands of generations with almost no change, while the world around them changes. They are living fossils: a present-day organism that closely matches its ancient fossil relatives. The match is measured by trait comparison between the living species and its fossil ancestors, and the species is recorded as a living fossil only when the match holds.
- **Numbers:** A living fossil is recorded when a living species matches its fossil ancestor (from at least 5,000 generations earlier) within 0.2 standard deviations on at least 3 measured traits. The match is computed per run.
- **Check:** The trait comparison is logged per candidate species; a species claimed as a living fossil without the 3-trait match is rejected, and the rejection is recorded.

**587. Memory outlives the individual**
- **Rule:** Knowledge can outlive its discoverer: a behaviour, a route, a food source learned by one organism can be passed to others through teaching, imitation, or the traces left behind — a worn path, a cache, a marked place. The record tracks how long a piece of knowledge survives after its first discoverer dies.
- **Numbers:** Knowledge survival is measured in generations from the discoverer's death to the last observed use of the knowledge; the run reports the median survival time and the longest-lived piece of knowledge. The starting expectation is 1–50 generations for socially passed knowledge.
- **Check:** The knowledge-survival curve is logged per run; at least 1 piece of knowledge is tracked from discovery to loss per run, and the curve is stored in the run log.

**588. The historical record is the fossil record's partner**
- **Rule:** The project's own logs — births, deaths, splits, extinctions — are the complete record, while fossils are the world's partial one. The fossil record is checked against the logs to measure what it preserves and what it loses, and the logs are never edited to match the fossils. History stays as it happened; the fossils are the check on what the world itself remembers.
- **Numbers:** The comparison is run at least once per 1,000 generations: the fossil species list against the true species list, the fossil extinction count against the true count. The agreement rates are logged.
- **Check:** The agreement rates are reported per run; a fossil record agreeing with the logs on more than 95% of species is flagged as suspiciously complete and reviewed.

**589. History stays — nothing is erased**
- **Rule:** The historical record is never rewritten to make the story cleaner: no extinct species deleted, no failed lineage hidden, no embarrassing result removed. Corrections are added as new entries with the old value kept. A world whose history can be edited is a world whose evidence cannot be trusted.
- **Numbers:** The record is append-only; every entry carries a generation and a writer (the run, not a person). The record size is logged per 1,000 generations, and zero deletions is the target — any deletion is logged as an event with its cause.
- **Check:** An audit of the record finds zero deletions without a logged cause across ≥5 runs; the audit result is recorded, and any unexplained deletion blocks the phase sign-off until resolved.

**590. The fossils and memory record and sign-off**
- **Rule:** Fossils and memory work is done when fossils form at a measured rate, the preservation bias is reported, the layer order is checked, knowledge survival is tracked, and the append-only history is audited. Muse reviews the record before the phase moves on; a fossil list without a bias report is not a record.
- **Numbers:** The sign-off run has at least 10,000 generations, at least 100 fossils, a measured formation rate, and a bias report. The review is recorded with a date.
- **Check:** The sign-off checklist (formation rate, bias, layer order, knowledge survival, append-only audit) is verified against the run log and the audit passes; the result is stored in the emergence log.

### 6.10 Evolution has no goal

**591. No destination in the rules**
- **Rule:** Nothing in the rules points toward humans, toward intelligence, or toward any particular form. Selection rewards what survives and reproduces here and now, not what will be useful later. A trait that helps today spreads; a trait that would help in a thousand generations but costs today does not. The world has no finish line written into it.
- **Numbers:** The test is the absence of any rule that rewards progress toward a target form: an audit of the rules finds zero target-seeking terms, zero rewards for complexity, and zero rewards for human-like traits. The audit is recorded per run.
- **Check:** The rule audit passes with zero target-seeking terms found; the audit is repeated after every rule change and the result is stored in the emergence log.

**592. Complexity is not progress**
- **Rule:** More complex is not better: a simple cell that survives is more successful than a complex body that dies. Complexity rises when it pays and falls when it costs, and the record reports complexity as a measurement — the count of roles, the size of the mind — never as a score.
- **Numbers:** Complexity is reported as the median role count and median mind size per generation, with no target value and no reward attached. A complexity fall of more than 20% over 1,000 generations is reported as a fall.
- **Check:** The complexity curves are logged per run; the absence of any complexity reward in the rules is verified by the audit in topic 591, and the curves are stored.

**593. Intelligence is not the point**
- **Rule:** Intelligence is one way of surviving, not the purpose of surviving. Most species will never be intelligent, and that is not a shortcoming — they survive by other means. The project measures intelligence where it appears (learning rate, memory use, problem-solving) but never rewards it, never steers toward it, and never judges a run by whether intelligence appeared.
- **Numbers:** Intelligence is measured on the tasks where it shows (foraging success, novel-food discovery, memory use) with no target and no reward; the run reports the distribution of these measures across species without ranking the species.
- **Check:** The intelligence measures are logged per run with no target attached; an audit finds zero rules that reward intelligence, and the audit result is recorded.

**594. Humans are not the endpoint**
- **Rule:** Human-level minds are the project's destination in the sense that the project wants to see whether they can evolve — not because evolution is aimed at them. If the world produces brilliant swimmers and no humans, it has answered the question honestly. The human experiment happens when human-level minds exist, or as a seeded starting condition if evolution stalls.
- **Numbers:** The human-level criteria (full hybrid mind at human scale, hands able to use tools, social cognition and communication, human-scale survival bar — all four must pass) are the test for whether humans have arrived; they are never a target the rules steer toward.
- **Check:** The four human-level tests are applied only as measurements when a candidate appears, and the topic 591 audit confirms no rule steers toward them.

**595. Evolution can go backwards**
- **Rule:** Traits can be lost: a lineage can lose its eyes in the dark, lose its legs on an island, lose its complexity when food is scarce. Loss is evolution working, not failing — the simpler form survives better in its niche. The record shows the trait, the generation, and the niche that made the loss pay.
- **Numbers:** Trait loss is counted per run (a trait present in the ancestor, absent in the descendant, with the loss sustained for at least 100 generations). At least 1 loss per run is expected once 3 or more species exist.
- **Check:** The loss events are listed per run with their traits and generations; a run with zero losses after 10,000 generations is flagged for review of whether loss is possible in the rules.

**596. There is no ladder, only a bush**
- **Rule:** Evolution is not a ladder from low to high with humans at the top; it is a bush, branching in all directions, with most branches ending and no branch higher than another. The project describes the world as a bush, never as a ladder. Any ranking of species is a human story laid over the tree, and the record does not rank.
- **Numbers:** The bush shape is reported as the tree's branch counts per depth level (topic 573); no species is assigned a rank or a height. The tree is presented with the root at one end and all living species at the other, none above another.
- **Check:** The tree presentation is reviewed for ranking language (no "higher", "lower", "advanced", "primitive") on ≥5 runs; any ranking found is corrected.

**597. Chance matters as much as selection**
- **Rule:** Not everything that survives is the fittest: a lucky individual survives a shock its betters did not, a neutral mutation spreads by drift, a founder's quirks become a species' traits. Drift and luck are measured alongside selection using a neutral control: compare the real run against a run where the trait does nothing, and the difference is selection; the rest is chance.
- **Numbers:** Drift is measured by the neutral-control comparison: the trait's spread in the main run versus a control run where the trait carries no advantage. The fraction of trait change attributable to drift is reported per run, with a starting expectation of 10–50%.
- **Check:** The neutral-control comparison runs at least once per 1,000 generations for at least 1 trait; a run claiming 0% drift is flagged.

**598. The world does not care what evolves**
- **Rule:** The world has no preference: it does not protect a favoured species, rescue a failing lineage, or punish a successful one. The rules apply the same to every organism. Any intervention to save a species, boost a lineage, or steer an outcome is recorded as an intervention, not as evolution, and excluded from the emergence numbers.
- **Numbers:** Zero interventions per run is the target; any intervention (a placed organism, a changed rule mid-run, a rescued species) is logged and excluded from the species count, diversity, and emergence claims. The intervention log is kept with the checkpoint.
- **Check:** The intervention log is audited per run; a run with an unlogged intervention fails the audit, and the result is recorded before the phase is signed off.

**599. Measuring emergence honestly**
- **Rule:** The project's claim is emergence: that what appears in the world came from the rules, not from the owner. The test is the Discovery Principle test from Phase 5 — could the owner have predicted it? If yes, it was placed; if no, it was discovered — applied to every major outcome in this phase: every split, every transition, every convergence. 
- **Numbers:** The test is applied to at least 5 major outcomes per run (splits, transitions, convergences); each is judged predicted or discovered with the owner's pre-run prediction list as the evidence. The discovered fraction is reported per run.
- **Check:** The prediction list and the judgements are stored in the emergence log; an outcome judged discovered without a pre-run prediction list is re-judged as unproven.

**600. Phase 6 record and sign-off**
- **Rule:** Phase 6 is done when the species criterion is in force, isolation and speciation are measured, extinctions are recorded, deep time has run, transitions are counted, convergence is checked, the tree is complete, fossils are kept, and the audit has passed. The full phase record is written in the emergence log, Muse reviews it, and the closing decision is recorded with the date.
- **Numbers:** The sign-off run set is at least 5 seeds of at least 10,000 generations each, with at least 5 splits, at least 1 extinction, a calibrated clock, and a complete tree to the root. The review is recorded with a date.
- **Check:** The phase checklist (one item per milestone, 6.1–6.10) is verified against the run logs and the result is stored in the emergence log.

## Phase 7 — Life builds up: chemistry to cells to bodies

### 7.1 The origin (protocells)

**601. The soup starts with chemistry, not cells**
- **Rule:** The world begins with monomers, energy, and water only — no strands, no membranes, no cells at the start. Amphiphiles self-assemble into empty vesicles, and strands form inside them by ligation and break apart by hydrolysis, all from fixed chemical rules.
- **Numbers:** Start state: zero strands, zero vesicles. Validation runs: 8,000 ticks, seeds 20261105, 20261106, 20261107, sampled every 100 ticks.
- **Check:** At tick 0 the count of strands and vesicles is zero in every seed; any placed replicator disqualifies the run.

**602. The six-criterion origin bar**
- **Rule:** Life is claimed only when all six criteria pass together: origin without placement, self-sustaining replication, compartmentalised individuality, metabolism, heritable variation, and selection. Each criterion is pre-registered before validation runs, and none is changed after seeing the numbers.
- **Numbers:** Bar: 6 of 6 criteria, in 3 of 3 validation seeds, each with its clean control behaving as required.
- **Check:** A run failing any one criterion is reported as a negative result, with the failed criterion named and its numbers shown.

**603. Origin without placement**
- **Rule:** The first catalyst appears by ligation from monomers, and the first catalysed copy follows it; nothing is placed or steered after the start. A strand counts as a catalyst when it starts with GG and has at least four bases.
- **Numbers:** Measured first catalyst at ticks 265, 289, 282 across the three seeds; first catalysed replication at ticks 353, 330, 285.
- **Check:** First catalyst tick is recorded per seed and is greater than zero with no strands present at tick 0; a placed replicator fails this criterion outright.

**604. Self-sustaining replication**
- **Rule:** A catalyst copies itself inside its vesicle, and daughters inherit at least one catalyst, so the lineage continues without outside help. Copying carries a per-base mutation probability, so offspring are similar but not identical to their parent.
- **Numbers:** Bar: best lineage reaches generation 10, with at least 10 consecutive generations of inherited catalyst, more than zero catalysed births, persisting at least 5,000 ticks after its first catalyst; mutation 2% per base.
- **Check:** Measured generations 67, 67, 69; inherited streaks 67, 67, 69; catalysed births 137,511, 138,081, 140,663 — all three seeds pass.

**605. Compartments: vesicles that divide**
- **Rule:** Vesicles grow only from lipid their own catalyst makes from monomers, and divide at twice their assembly lipid content, splitting their strands between two daughters. A daughter with no catalyst can acquire one later by ligation, but that is not inheritance.
- **Numbers:** Division at 2× assembly lipid content; measured divisions 5,025, 5,043, 5,173 across the three seeds.
- **Check:** At least 10 divisions carry the inherited-catalyst streak through division in each seed; divisions without catalyst-made lipid fail the check.

**606. Metabolism: the lineage makes its own membrane**
- **Rule:** The catalyst synthesises membrane lipid from monomers, so growth is paid for by the lineage's own chemistry. Energy and mass come from the soup's inflow and are conserved within documented numerical error; nothing is created free.
- **Numbers:** Lipid production is counted per lineage; the no-catalysis control must show zero catalysed births and fail the replication criterion.
- **Check:** Main arm establishes in 3 of 3 seeds; no-catalysis control shows 0 births and 0 mutations in 3 of 3, despite 1,580, 1,531, and 1,676 divisions.

**607. Heritable variation**
- **Rule:** Copying errors change catalyst sequences, and some mutant sequences persist in the population, giving selection something to act on. The heritable trait is GC fraction: catalyst efficiency rises with GC content in the main arm.
- **Numbers:** Efficiency is 1 + 2 × GC in the main arm and 1 regardless of GC in the neutral control; a mutant must persist 1,000 ticks (10 consecutive samples).
- **Check:** At least one mutation occurs and at least one mutant persists 1,000 ticks; measured mutant persistence 7,700, 7,600, and 7,800 ticks.

**608. Selection, measured against a neutral control**
- **Rule:** Selection is claimed only when the main arm's final mean GC fraction beats the neutral control's by a set margin on the same seed and horizon. A rise inside one run alone is not enough, because the GG catalyst motif biases the mutation balance upward.
- **Numbers:** Bar: main minus neutral final mean GC of at least 0.10 in at least 2 of 3 seeds; measured final GC 0.864, 0.875, 0.883 against neutral 0.713, 0.732, 0.702.
- **Check:** Differences +0.1511, +0.1435, +0.1812 — criterion passes in 3 of 3 seeds, with the neutral control as the null.

**609. What the protocell result does and does not establish**
- **Rule:** Passing all six criteria establishes a self-sustaining, compartmentalised chemical system with heredity, variation, and measurable selection under fixed coarse-grained rules — the working definition of life, made operational. It does not establish wet-lab chemistry, minds, multicellularity, or civilisation.
- **Numbers:** Verdict: 6 of 6 criteria pass in 3 of 3 seeds, with all controls behaving as required; limits recorded with the result.
- **Check:** The report lists the model's limits alongside the pass: no spatial structure, no explicit molecular structure, no translation, and a designed genotype-to-phenotype map for the catalyst rule.

**610. The served baseline is the live protocell pond**
- **Rule:** The world now serves the live protocell pond as its baseline: life from chemistry, not seeded cells. The pond sits in a labelled early-Earth shelf scene, which is scenery, not simulated terrain yet, and the feed is read-only with no write path.
- **Numbers:** Pond served from the validated runs above; Gateway contract closed, feed at the loopback address with one snapshot per frame over the stream.
- **Check:** The served state matches the validated protocell numbers, and the scene is labelled as a pond baseline; any claim of a later stage must show its own measured numbers.

### 7.2 The first cells

**611. The primordial soup pilot**
- **Rule:** A bounded dish of soup tests whether cells survive, reproduce, and measurably gain complexity over generations. The pilot design — dish size, cell model, mutation rate, complexity measure, success criterion — is proposed by Freebuff and reviewed by Muse before it is built.
- **Numbers:** Pilot design states dish size, founder count, mutation rate, and generation target in writing; success needs survival plus reproduction plus a measured complexity rise.
- **Check:** The approved design and its review are recorded with dates; building starts only after the review is recorded.

**612. The dish: a bounded world for cells**
- **Rule:** The dish is a bounded shallow basin with stated size, shape, and edges; resource inflow enters at a recorded rate and waste leaves by a recorded route, so mass and energy can be audited. Nothing enters or leaves unrecorded.
- **Numbers:** Dish size, inflow rate, and outflow route are recorded with the seed; the live feed samples the real nutrient field on a 16×16 grid, values 0–100.
- **Check:** A boundary test asserts nothing leaves the dish and nothing enters unrecorded; the same seed reproduces the same dish.

**613. Chemistry rules for the soup**
- **Rule:** A written list of chemical species and reaction rules states which chemicals combine into what, under which conditions, and where energy comes from, how it flows, and how it is spent. Concentrations vary across the dish, forming gradients cells can sense.
- **Numbers:** Species list, reaction conditions, energy inflow rate, and starting concentrations are recorded with the seed; mass and energy conserved within documented numerical error.
- **Check:** Chemistry alone runs stably with no cell present, and a determinism check shows the same seed gives the same soup.

**614. The first replicators in the dish**
- **Rule:** A cell copies itself when it has the energy and stores to pay for a copy; copying costs energy, and a cell without enough energy does not copy. Offspring inherit the parent's traits with mutation, and offspring can themselves replicate.
- **Numbers:** Replication cost in energy per copy and the energy threshold for copying are recorded; mutation 2% per base in the protocell model.
- **Check:** A single cell in a rich dish reproduces, its offspring reproduce in turn, and the first replicator is logged with generation and time.

**615. Mutation: offspring differ from parents**
- **Rule:** Copying introduces small random changes to the offspring's traits — size, speed, efficiency, and tolerances — at a rate high enough to create variety but low enough that inheritance survives. Mutation is the only source of new variation; nothing is placed by hand.
- **Numbers:** Mutation rate stated in the pilot design with its reason; trait changes measured as the difference between parent and offspring trait values.
- **Check:** A mutation test shows offspring differ measurably from parents, and at least one mutant lineage persists; no cell is placed after the initial seeding.

**616. Nutrient-only competition first**
- **Rule:** The pilot runs on nutrient competition only: cells compete for food and light, and no cell eats another. Predation from day one would confound the complexity measures, so it is kept out until it gets its own pressure with its own falsifier.
- **Numbers:** Predation rate zero throughout the pilot; the pilot's complexity metrics are computed on nutrient-only runs across at least 5 seeds.
- **Check:** Run logs show zero predation events; any complexity rise is attributable to nutrient competition, not to eating other cells.

**617. Complexity: what "more complex" means**
- **Rule:** Complexity is one stated metric with an exact formula — such as trait count, genome length in use, or behavioural repertoire — computed the same way every generation, so a rise cannot be faked by a cell doing nothing new. The metric is chosen before the run.
- **Numbers:** Starting complexity at generation 0 and ending complexity at the final generation are recorded per seed, with the formula in the research log.
- **Check:** The metric is tested for gameability: a cell cannot inflate it without doing more; the complexity curve is logged per generation.

**618. The generation clock that counts turnovers**
- **Rule:** Progress is counted in population-normalised turnovers — births relative to population size — not in the deepest chain ever reached, because a single surviving lineage cannot beat a record set by a dead chain. The stall guard watches the turnover clock, so a live population turning over cannot look stalled.
- **Numbers:** Runs target 2,000 turnovers with a 1,000-turnover floor; an atomic row is written every 100 turnovers so a stopped run keeps partial results.
- **Check:** The turnover count rises while births continue; a run that stops on the stall guard shows a frozen turnover count, not a frozen generation record.

**619. Directional selection in the dish**
- **Rule:** In the pilot, selection pushed traits in the same direction in every dish: size shrank, efficiency rose, light and temperature affinity fell, and speed and toxin tolerance rose. Those shifts are read from the trait distributions, not asserted from a single lineage.
- **Numbers:** Trait means per generation are logged; a directional shift counts when the same trait moves the same way in at least 4 of 5 seeds.
- **Check:** Per-seed trait curves show the direction and size of each shift; a trait that moves in only one seed is reported as noise, not selection.

**620. The pilot decision gate**
- **Rule:** The pilot passes only if cells survive, reproduce, and measurably gain complexity over the stated generations; the judgement is recorded with the numbers for each part, and the next phase starts only after the gate is closed. If it fails, the record states the single change and its falsifier for the next attempt.
- **Numbers:** Gate judged across at least 5 seeds; pilot cost per generation and tick rate recorded with the judgement.
- **Check:** Pass or fail is written in the emergence log with survival, reproduction, and complexity numbers per seed; no phase after the pilot starts on an unjudged gate.

### 7.3 Cells survive and reproduce

**621. The cell kernel, scaled down from the human kernel**
- **Rule:** The cell kernel reuses the tested stdlib kernel as its foundation, keeping conservation, determinism, and checkpoint-resume checks, and removes human-scale systems such as houses and human thirst and sleep. A cell's state is position, energy, chemical stores, age, and generation.
- **Numbers:** Kernel test suite pass count recorded; tick rate measured at 100, 1,000, and 10,000 cells.
- **Check:** Conservation and determinism checks pass at cell scale, and the kernel runs with no observer online.

**622. Cell senses: gradients, not vision**
- **Rule:** A cell senses only its surroundings: chemical gradients, light level and direction, and local temperature. It has no access to world state beyond its sensors, so everything it knows arrives through those channels.
- **Numbers:** Sensing ranges for food gradient, light, and temperature are recorded; the sensor vector's dimension and cost per tick are recorded.
- **Check:** A cell in a gradient moves toward food faster than a random-walking cell; a test asserts the sensor vector is the cell's only input.

**623. Cell drives: energy, hunger, reproduction**
- **Rule:** Energy falls with activity and rises with eating; hunger rises with time and activity; a cell reproduces only when energy and stores pass a threshold. The drives are homeostatic: they push the cell back toward balance rather than toward endless growth.
- **Numbers:** Energy gain per unit eaten, energy cost per tick of activity, hunger rise per tick, and the reproduction threshold are recorded.
- **Check:** A starving cell seeks food, a cell with no food dies with energy at zero, and the death is logged with cause and generation.

**624. Cell movement and action space**
- **Rule:** A cell can move, eat, reproduce, or rest, and every action costs something — energy, time, or opportunity. Movement follows sensed gradients; resting saves energy by not moving; eating consumes food at the cell's position.
- **Numbers:** Speed, eating rate and gain, resting saving, and reproduction cost are recorded per action.
- **Check:** A cell reaches food faster than a random walker, and a test asserts no action executes without its cost being paid.

**625. The cell harness: learned against random**
- **Rule:** The cell harness runs three arms on identical seeds — learned cells, learned cells with the steering layer off, and random cells — so any advantage is attributable to learning, not to the world or the seed. The steering layer stays off in the population arm.
- **Numbers:** At least 5 seeds per arm; survival and reproduction recorded per seed per arm; tick rate recorded per arm.
- **Check:** The learned population beats the random control on survival and reproduction across at least 5 seeds, or the failure is recorded with the diagnosis.

**626. The cell bar: learned beats random**
- **Rule:** The bar is survival and reproduction together: learned cells must beat random cells on both, across at least 5 seeds. A win on one measure alone does not pass, and the first-reproduction time per arm is recorded as the cell-scale analogue of first-drink day.
- **Numbers:** Median survival and total births per arm across at least 5 seeds; first-reproduction generation per arm.
- **Check:** Pass or fail is judged with the numbers in the testing report; a fail names the next single change and its falsifier.

**627. Reproduction assigns a new agent per offspring**
- **Rule:** Every offspring gets its own agent — its own mind, its own memory, its own life. The parent's agent never controls the child, and the child's mind starts fresh with no copy of the parent's memory. Population grows through birth, not placement.
- **Numbers:** Agent count tracked over time and checked against the living cell count; births and deaths logged per generation.
- **Check:** A reproduction test shows the offspring has its own agent; agent count equals living cell count in every logged generation.

**628. Cell death is permanent**
- **Rule:** A cell dies when its energy reaches zero or it takes lethal damage, and it stays dead: no revival, no reset, no reuse of its agent. Its lineage remains in the historical record, so the dead are remembered even though they never return.
- **Numbers:** Deaths logged with cause, generation, and time; death causes counted per run; survival curve recorded per seed as fraction alive per generation.
- **Check:** A starved cell dies and stays dead across checkpoint and resume; a dead cell's agent is retired, never reassigned.

**629. Cells in a real day and night**
- **Rule:** Light follows real solar geometry — declination and hour angle from standard formulae — so the dish has day and night, and cells that sense light experience the cycle. The run clock starts at dawn, so the first light is morning light.
- **Numbers:** Latitude 35°, longitude 0° as stated viewer initial conditions; day length and light levels logged per tick; the clock advances 1:1 with real time.
- **Check:** Light level rises after dawn and falls toward night in the logged data; a light-sensing cell's behaviour differs between day and night runs.

**630. Cell instrumentation**
- **Rule:** Every birth, death, and reproduction is logged with generation, time, and cause, with the population, energy, and hunger distributions per generation, and a lineage query returns any cell's ancestors back to generation 0. Logs survive checkpoint and resume.
- **Numbers:** Event counts per generation recorded; log format recorded in the repo; first survival, first reproduction, and first extinction logged per run.
- **Check:** A completeness check finds no birth or death unlogged, and the lineage query returns a full ancestor chain for a sampled cell.

### 7.4 Cells get better

**631. Selection acts on what already varies**
- **Rule:** Selection is environmental — food, light, temperature, and crowding decide who survives and reproduces — never the owner's choice. A trait spreads only if its bearers survive and reproduce more, and the spread is measured in the population, not assumed.
- **Numbers:** Trait frequencies logged per generation; a beneficial trait counts as spreading when its frequency rises in at least 4 of 5 seeds.
- **Check:** A selection test shows a beneficial mutation spreading through the population; populations with mutation are compared against populations without it.

**632. Complexity rises measurably**
- **Rule:** The complexity metric from the pilot is computed every generation, and a rise counts only when the same formula shows a higher value at the end than at the start across the run. The most complex lineage is named with its generation, traits, and what it does differently.
- **Numbers:** Start and end complexity per seed, with the range across at least 5 seeds; complexity change reported as increase, decrease, or flat with numbers.
- **Check:** Complexity increased in the recorded number of seeds out of 5; a run where it falls is reported as a fall, not hidden.

**633. Niches: different ways to live**
- **Rule:** Different lineages occupy different niches — different food sources, habitats, or timings — because their traits suit different conditions, not because anyone assigned them. A niche is defined by how a lineage lives, and it can empty by extinction and be re-occupied by another lineage.
- **Numbers:** Niches observed and their counts per run recorded; niche occupancy logged per generation; lineage patch-share entropy measured per lineage.
- **Check:** Two lineages diverge into different niches in the logged data; the median lineage entropy at the final generation is compared with its generation-100 value.

**634. Efficiency improves under scarcity**
- **Rule:** When food is scarce, lineages that convert food to energy more cheaply leave more offspring, so mean efficiency rises over generations. Efficiency is measured as energy gained per unit of food eaten, minus the cost of the actions that got it.
- **Numbers:** Mean efficiency per generation logged; starting and ending means recorded per seed; scarcity set by inflow rate in the dish design.
- **Check:** Mean efficiency at the final generation exceeds the generation-0 mean in at least 4 of 5 seeds, with the numbers shown.

**635. Speed and sensing improve together**
- **Rule:** Faster cells reach food sooner, but speed costs energy, so the winning balance depends on how patchy the food is; sensing range sets how far ahead a cell can aim. Both traits evolve under the same nutrient-only competition, and their joint distribution is what selection sees.
- **Numbers:** Mean speed and mean sensing range per generation logged; food patchiness stated as patch count and radius in the dish design.
- **Check:** Mean speed and sensing range both move in the recorded direction across seeds, and the energy cost of speed is shown alongside the gain.

**636. Tolerance widens**
- **Rule:** Cells exposed to heat, cold, or toxins survive better when their tolerance widens, so lineages in harsh patches evolve broader tolerance ranges. Tolerance is measured as the range of temperature or toxin level in which a cell keeps positive net energy.
- **Numbers:** Tolerance range per lineage logged; harsh patches defined by temperature or toxin level in the dish design; pilot evidence showed toxin tolerance rising in every dish.
- **Check:** Mean tolerance range at the final generation exceeds the starting range, with the per-seed numbers recorded.

**637. The falsifier for "cells get better"**
- **Rule:** The claim that cells improve is falsified if learned cells do not beat random cells on survival and reproduction across at least 5 seeds, or if complexity does not rise in any seed. A falsified claim stops the phase's advance and names the single change to try next.
- **Numbers:** Bar: learned beats random on both measures across at least 5 seeds; complexity rise in at least 3 of 5 seeds.
- **Check:** The judgement is recorded as pass or fail with the numbers; a fail lists the diagnosis, the next change, and the falsifier for that change.

**638. Trade-offs are real**
- **Rule:** No trait improves for free: bigger size costs more energy, faster movement costs more energy, wider sensing costs more per tick. A lineage that gains in one trait pays in another, and the net balance is what selection measures.
- **Numbers:** Cost per trait per tick recorded; size, speed, and sensing costs shown as energy per tick alongside their benefits.
- **Check:** Trait correlations are logged per generation; a trait that rises without a cost anywhere is investigated as a possible measurement error.

**639. Lineages, not just cells, are the unit of improvement**
- **Rule:** Improvement is tracked per lineage — a chain of parent-to-offspring descent — because a single lucky cell proves nothing. A lineage improves when its later generations outperform its earlier ones on survival and reproduction in the same dish conditions.
- **Numbers:** Lineage survival and reproduction per generation logged; the best lineage's generation count and trait profile recorded.
- **Check:** The best lineage's later generations beat its earlier generations on both measures, with the numbers shown; one lineage per dish is the observed pattern, not an assumption.

**640. Cells-get-better record and sign-off**
- **Rule:** The record states what improved, by how much, in which seeds, and what did not improve, with the trait curves, complexity curves, and niche data archived so the run can be re-run. The phase advances only after Muse signs off on the record.
- **Numbers:** Archive location recorded; seed list, generation counts, and final trait means recorded per seed.
- **Check:** The archive is confirmed complete and re-runnable, and the sign-off is recorded with the date in the emergence log.

### 7.5 Colonies

**641. Adhesion: cells stick together**
- **Rule:** Cells can stick to each other as an action that costs energy, forming clusters that move and feed as a group. Adhesion is reversible: cells can detach, and a cluster can break apart. Each cell keeps its own agent while stuck.
- **Numbers:** Adhesion cost in energy per tick, cluster sizes observed per run, and detachment rate recorded.
- **Check:** Cells in a rich patch form a cluster in the logged data; a test asserts adhesion does not merge agents and that detachment works.

**642. Clusters survive better than loners, sometimes**
- **Rule:** A cluster shares protection and pooled sensing, but shares food too, so clustering helps in some conditions and hurts in others. The comparison is measured per condition, not assumed in general: clustered cells are compared against solitary cells on the same dish.
- **Numbers:** Survival and reproduction of clustered versus solitary cells across at least 5 seeds, per food density.
- **Check:** The comparison shows in which food densities clustering wins and in which it loses, with the numbers per density.

**643. Clusters sense more than a single cell**
- **Rule:** A cluster's sensing comes from combining its members' own sensors — wider coverage, more gradients sampled — not from a cluster-level sense that no cell has. The cluster has no single mind; each cell keeps its own agent and its own decisions.
- **Numbers:** Sensing range of clusters versus single cells recorded; food-finding time for clusters versus loners recorded.
- **Check:** A cluster finds food a single cell misses in the logged runs, and a test asserts no cluster-level sensor exists in the code.

**644. Clusters share food and energy**
- **Rule:** Cells in a cluster can pass energy or food to neighbours, so a cell that found food can keep a hungry neighbour alive. Sharing is a cell action with a cost, and it benefits the cluster only when the shared energy is used by a cell that then survives and reproduces.
- **Numbers:** Sharing rate, amount shared per event, and cost per sharing event recorded; cluster survival with and without sharing compared.
- **Check:** Clusters with sharing outperform clusters without it on survival across at least 5 seeds, with the numbers shown.

**645. Clusters have a size that works**
- **Rule:** Very small clusters gain little, and very large clusters starve their inner cells, so there is a working size range set by food inflow, diffusion, and the cost of staying stuck. Cluster size is an outcome of those rules, not a target set by hand.
- **Numbers:** Cluster size distribution per generation logged; food inflow rate and diffusion rate stated in the dish design.
- **Check:** The size distribution peaks inside a recorded range, and clusters outside it shrink or break up in the logged data.

**646. Clusters break up**
- **Rule:** A cluster breaks up when food runs out, when inner cells starve, or when detachment pays better than staying. Breakup is a real event with a cause, logged like a death, and the freed cells go back to living alone.
- **Numbers:** Breakup events logged with cause and generation; breakup rate per generation recorded.
- **Check:** Breakups are logged with causes, and the cause counts match the food and starvation data for the same generations.

**647. Colonies on surfaces**
- **Rule:** Cells that stick to a surface form a colony that stays put and grows outward, feeding from the flow past it. Surface colonies trade movement for stability: they cannot chase food, but they are not swept away either.
- **Numbers:** Surface colony growth rate, colony area, and food flow rate past the surface recorded.
- **Check:** A surface colony grows outward in the logged data and its area curve matches the food flow; a colony with no flow stalls.

**648. Colonies resist being washed away**
- **Rule:** Adhesion to a surface and to each other gives a colony grip against currents, so it holds its place while solitary cells drift. Grip is paid for in adhesion energy, and a colony that cannot pay it is swept away like any loner.
- **Numbers:** Current speed, adhesion energy per tick, and the fraction of colonies holding position recorded.
- **Check:** Colonies hold position in currents that sweep solitary cells away, and the holding fraction falls when adhesion energy runs out.

**649. Colonies and the first division of labour**
- **Rule:** In a colony, cells in different positions face different conditions — outer cells meet food first, inner cells are sheltered — so they begin doing different work. The roles come from position and signals, not from a script, and they reverse when the colony breaks up.
- **Numbers:** Roles observed and their counts per colony recorded; work split per role logged.
- **Check:** A colony shows at least two roles in the logged data, and the roles disappear when the colony breaks up.

**650. Colony record and sign-off**
- **Rule:** The record states cluster sizes, colony areas, sharing rates, and breakup causes per seed, with the comparisons against solitary cells, and archives the runs. The phase advances only after the record is signed off.
- **Numbers:** Archive location, seed list, and final cluster-size distribution recorded per seed.
- **Check:** The archive is confirmed complete and re-runnable, and the sign-off is recorded with the date.

### 7.6 Multicellularity

**651. Differentiation: cells take roles**
- **Rule:** Cells in a cluster take different roles — outer versus inner, feeding versus moving — set by position and chemical signals, not by a script. A differentiated cell keeps its own agent, and its role can change if its position changes.
- **Numbers:** Roles observed and counts per cluster recorded; signal thresholds that trigger each role stated.
- **Check:** A cluster develops at least two roles in the logged data, and a role change follows a position change in a recorded case.

**652. Division of labour**
- **Rule:** Different roles do different work: one role gathers food, another moves the cluster, another holds the structure. The division emerges from the roles, and each role's work must benefit the cluster in shared energy or protection, or the role fades.
- **Numbers:** Work split per role recorded; cluster performance with roles versus without roles compared across at least 5 seeds.
- **Check:** A cluster with roles outperforms a cluster without roles on survival and reproduction, with the numbers shown.

**653. Body plans: stable arrangements**
- **Rule:** A body plan is a stable arrangement of differentiated cells that forms repeatably from the same starting cluster. It is inherited: offspring clusters form the same plan with mutation, and the plan is never designed by the owner.
- **Numbers:** Body plans observed and their frequencies per run recorded; plan fidelity from parent to offspring measured.
- **Check:** The same starting cluster forms the same body plan across seeds, and offspring plans match parents within the measured mutation range.

**654. Collective sensing at body scale**
- **Rule:** A body senses more than any one of its cells because its cells sample different places at once, and the combined signal guides the body's movement. The body still has no single mind at this stage; the sensing is the sum of its cells' sensors.
- **Numbers:** Body sensing range versus single-cell range recorded; food-finding time for bodies versus loners recorded.
- **Check:** A body finds food a single cell misses, and the sensing range grows with body size in the logged data.

**655. Bodies move as one**
- **Rule:** The cells of a body coordinate movement so the body travels in one direction instead of pulling apart. Coordination comes from shared signals between neighbouring cells, and a body that cannot coordinate splits or stalls.
- **Numbers:** Body speed, coordination cost per tick, and the fraction of bodies moving coherently recorded.
- **Check:** Bodies move coherently in the logged data, and bodies that lose coordination split or stall at the recorded rate.

**656. Reproduction of bodies**
- **Rule:** A body produces an offspring body, not just a cell: the offspring starts as a small cluster with the parent's plan, and each of its cells gets its own fresh agent. The offspring's plan matches the parent's within mutation.
- **Numbers:** Body reproduction rate and cost recorded; offspring survival rate recorded per seed.
- **Check:** A body reproduces and the offspring body survives in the logged runs; the offspring plan matches the parent's within the measured range.

**657. Bodies grow**
- **Rule:** A body grows by its cells reproducing inside it, adding cells in the places the plan allows, until it reaches the size its food supply supports. Growth costs energy, and a body that cannot pay for growth stops growing instead of growing free.
- **Numbers:** Growth rate in cells per generation, final body size, and energy cost per added cell recorded.
- **Check:** Body size over generations follows the logged growth curve and plateaus at the food-supported size; growth stalls when energy runs out.

**658. Bodies repair**
- **Rule:** A body replaces dead or damaged cells from its own stores, so small injuries do not kill it. Repair costs energy and materials, and a body that spends everything on repair has nothing left to grow or reproduce.
- **Numbers:** Repair rate in cells per tick, repair cost per cell, and the injury sizes repaired versus fatal recorded.
- **Check:** A body with a small injury recovers in the logged data, and repair spending is shown in the energy accounts for the same ticks.

**659. Death of bodies is permanent**
- **Rule:** A body dies when its cells die or its energy fails, and it stays dead; its agents are retired, never reused, and its lineage remains in the historical record. Body deaths are logged with cause, generation, and time.
- **Numbers:** Body death causes and counts per run recorded; body survival curve per seed recorded.
- **Check:** A starved body dies and stays dead across checkpoint and resume, and the death log is complete for the run.

**660. Multicellularity record and sign-off**
- **Rule:** The record states the first body, the first body plan, the first body reproduction, and the first body extinction per run, with body counts, survival, and reproduction per seed, and archives the runs. The phase advances only after sign-off.
- **Numbers:** Archive location, seed list, and final body counts recorded per seed.
- **Check:** The archive is confirmed complete and re-runnable, and the sign-off is recorded with the date.

### 7.7 Bodies

**661. Body size is set by food and physics**
- **Rule:** A body's size is limited by how much food reaches its cells and how much energy movement and repair cost at that size. Bigger bodies sense further and survive more, but pay more every tick, so size settles where the gain covers the cost.
- **Numbers:** Body size distribution per generation logged; energy cost per tick versus body size recorded.
- **Check:** Mean body size plateaus at the size where cost meets inflow in the logged data, and bodies above that size shrink or die.

**662. Body shape follows what the body does**
- **Rule:** Shape emerges from the body's way of living: a body that chases food grows streamlined, one that sits and filters grows broad. Shape is never drawn by hand; it is the outcome of growth rules, adhesion, and selection on the same dish.
- **Numbers:** Shapes observed and their frequencies per run recorded; shape measured as length-to-width ratio and surface-to-volume ratio.
- **Check:** Shape frequencies shift with food distribution in the logged runs, and the same starting cluster reaches the same shape across seeds.

**663. Bodies eat**
- **Rule:** A body takes in food through its surface or a mouth-like opening, and the food it takes in is limited by its surface area and the food density where it feeds. Eating costs energy to move food in and digest it, and the net gain is what fuels growth and reproduction.
- **Numbers:** Eating rate per unit surface, digestion gain per unit eaten, and net energy per feeding event recorded.
- **Check:** Net energy per feeding event is positive in the logged data for feeding bodies, and a body with no food in reach loses energy.

**664. Bodies excrete waste**
- **Rule:** Eating produces waste, and waste leaves the body into the water, where it diffuses and can feed other cells or poison the local patch if it builds up. Waste is mass that entered as food, so the accounts balance.
- **Numbers:** Waste output per unit eaten, local waste concentration, and the concentration at which feeding slows recorded.
- **Check:** Mass in equals mass out plus mass stored within documented error, and feeding slows in the logged data where waste builds up.

**665. Bodies age**
- **Rule:** Bodies age: cells accumulate damage with time and use, repair gets slower, and the body's performance falls. Aging is a property of the body's own cells and chemistry, not a clock imposed from outside.
- **Numbers:** Damage accumulation rate per tick, repair rate by age, and performance by age recorded; lifespan distribution per seed logged.
- **Check:** Older bodies show lower performance and slower repair in the logged data, and lifespan varies across bodies in the same run.

**666. Bodies reproduce as bodies**
- **Rule:** A mature body with enough stored energy produces an offspring body with its plan, and the offspring's cells each get fresh agents. Reproduction is the population mechanism at this scale: bodies are born, never placed.
- **Numbers:** Age and energy thresholds for reproduction, offspring count per body, and offspring survival rate recorded per seed.
- **Check:** Offspring bodies appear only through reproduction in the logs, and the offspring count matches the birth log for the run.

**667. Species: what counts as a new species**
- **Rule:** A speciation event is recorded when a population is reproductively isolated from its parent population, or when its genetic distance from the parent exceeds a measured threshold. The threshold is set by measurement, with Freebuff proposing the starting value and Muse reviewing it.
- **Numbers:** Genetic distance threshold stated with its measurement method; reproductive isolation tested by whether crosses produce viable offspring.
- **Check:** Two diverged lineages are identified as different species by the rule in a recorded case, and no species is declared by the owner.

**668. Diversity is measured, not asserted**
- **Rule:** Diversity is species count, lineage count, and trait spread, each with a stated formula computed the same way every generation. A diverse population holds many lineages in many niches; a narrow one holds few.
- **Numbers:** Species count, lineage count, and trait spread per generation logged; starting and final diversity recorded per seed.
- **Check:** Diversity curves are logged per generation across at least 5 seeds, and the range across seeds is reported with the numbers.

**669. Extinction is permanent**
- **Rule:** A species with no living members is extinct, and it never returns; its lineage stays in the historical record. Extinction is environmental — no food, no niche, no mates — never the owner's choice.
- **Numbers:** Extinctions logged with species, cause, generation, and time; extinction causes counted per run; species count over time recorded per seed.
- **Check:** An extinct species shows zero living members in every later generation, and a test shows a species with no food going extinct.

**670. Bodies record and sign-off**
- **Rule:** The record states body sizes, shapes, lifespans, reproduction, species counts, diversity, and extinctions per seed, with the lineage tree complete back to the first cell, and archives the runs. The phase advances only after sign-off.
- **Numbers:** Archive location, seed list, species count, and extinction count recorded per seed.
- **Check:** The lineage tree has no gaps — every species has a parent — and the archive is confirmed complete and re-runnable.

### 7.8 Senses

**671. Chemical sensing at body scale**
- **Rule:** A body senses chemical gradients across its surface, so it can tell which direction food lies in and how strong the signal is. The signal is read from the water at the body's surface, never from world state directly.
- **Numbers:** Chemical sensing range and gradient sensitivity recorded; sensor cost per tick recorded.
- **Check:** A body in a gradient turns toward the stronger concentration in the logged data, and a body with its chemical sense removed performs worse.

**672. Light sensing at body scale**
- **Rule:** A body senses light level and direction through light-sensitive cells, so it can move toward light where food grows or away from light where it is exposed. Light follows the real day-night cycle, so the signal changes through the day.
- **Numbers:** Light sensing range and sensitivity recorded; day and night light levels logged.
- **Check:** Bodies move toward or away from light consistently in the logged data, and their behaviour differs between day and night runs.

**673. Temperature sensing**
- **Rule:** A body senses local temperature and moves away from water too hot or too cold to feed in. Temperature is read from the water at the body's position, and the body pays a cost when it stays in water outside its tolerance.
- **Numbers:** Temperature sensing range and tolerance limits recorded; cost per tick outside tolerance recorded.
- **Check:** Bodies leave water outside their tolerance in the logged data, and bodies that cannot leave lose energy at the recorded rate.

**674. Touch and pressure**
- **Rule:** A body senses contact and pressure where its surface meets another surface — a rock, another body, or the dish edge — so it can stop, turn, or hold on instead of pushing through. Touch is local: only the part of the body in contact feels it.
- **Numbers:** Touch range is contact only; response time to contact and the force that triggers a turn recorded.
- **Check:** A body turns or stops on contact in the logged data, and a body with touch removed collides more often in a comparison run.

**675. Vibration and water movement**
- **Rule:** A body senses vibrations and currents in the water, so it can tell when something nearby moves or when the flow changes. The signal is read from the water around the body, and it fades with distance.
- **Numbers:** Vibration sensing range and sensitivity recorded; current speed and direction logged per tick.
- **Check:** Bodies react to a nearby moving body in the logged data, and the reaction rate falls with distance as recorded.

**676. Sensing costs energy**
- **Rule:** Every sense costs energy per tick to run, so a body cannot sense everything at full range for free. Wider range and finer sensitivity cost more, and a body that overspends on sensing has less left to move and eat.
- **Numbers:** Cost per sense per tick recorded; total sensing cost versus movement and eating costs shown per body.
- **Check:** Sensing costs appear in the energy accounts, and bodies with wider sensing show higher sensing costs in the logged data.

**677. Senses combine into a picture of the surroundings**
- **Rule:** A body acts on its senses together — chemical direction plus light plus touch — not on any one channel alone. The combination is done by the body's own cells passing signals to each other, so the picture is built from sensed data, never from hidden world state.
- **Numbers:** Sensor counts per body and the weight each channel carries in movement decisions recorded.
- **Check:** A body with one sense removed still navigates but worse than with all senses, and the performance drop per removed sense is recorded.

**678. Sensing has a range, and the world beyond it is unknown**
- **Rule:** A body knows nothing beyond its sensing range: food, danger, and other bodies past that distance do not exist for it until they come closer. This is what makes searching real — the body must move to learn what is out there.
- **Numbers:** Sensing ranges per channel recorded; the fraction of the dish inside a body's range at any time recorded.
- **Check:** Bodies pass within a recorded distance of food without reacting when it lies beyond range, and react once it enters range.

**679. Senses improve by selection**
- **Rule:** Bodies with better sensing find food sooner and avoid harm better, so sensing range and sensitivity rise over generations under the same selection that improves speed and efficiency. The improvement is measured per channel, not assumed for all senses at once.
- **Numbers:** Mean sensing range and sensitivity per channel per generation logged; starting and ending means recorded per seed.
- **Check:** At least one channel's mean range rises across generations in at least 4 of 5 seeds, with the numbers shown.

**680. Senses record and sign-off**
- **Rule:** The record states each sense's range, cost, and measured contribution to finding food and avoiding harm, per seed, with the comparison runs for removed senses, and archives the runs. The phase advances only after sign-off.
- **Numbers:** Archive location, seed list, and sensing ranges per channel recorded per seed.
- **Check:** The archive is confirmed complete and re-runnable, and the sign-off is recorded with the date.

### 7.9 Movement

**681. Movement costs energy every step**
- **Rule:** A body moves by spending energy: pushing against water, bending its shape, or beating a tail-like part. Faster movement costs more, and a body that moves without food to gain from it burns its stores for nothing.
- **Numbers:** Energy cost per metre at three speeds recorded; body speeds and their costs logged per body plan.
- **Check:** Energy accounts show movement costs rising with speed, and bodies that move without feeding lose energy in the logged data.

**682. Directed movement toward food**
- **Rule:** A body steers toward sensed food gradients, turning when the signal strengthens on one side and weakening when it fades. Steering is done by the body's own cells, using only what the body senses, with no waypoints or placed paths.
- **Numbers:** Turning rate, speed toward food, and time to reach food recorded; comparison against drifting bodies recorded.
- **Check:** A body reaches food faster than a drifting body across at least 5 seeds, and no placed path exists in the run logs.

**683. Movement away from harm**
- **Rule:** A body moves away from sensed harm — water too hot, toxins, or a larger body approaching — turning and speeding up until the signal fades. Fleeing costs energy, so a body flees only when the harm signal is strong enough to pay for it.
- **Numbers:** Harm thresholds that trigger flight, flight speed, and energy cost of flight recorded.
- **Check:** Bodies flee from a harm source in the logged data, and the flight rate falls when the harm signal is below threshold.

**684. Bodies rest to save energy**
- **Rule:** A body saves energy by not moving: it settles, slows its sensing, and spends only the cost of staying alive. Rest is a real choice with a cost — a resting body cannot feed or flee — so it rests when the saving outweighs the lost opportunity.
- **Numbers:** Resting energy cost per tick versus active cost recorded; resting time per body per generation logged.
- **Check:** Resting bodies spend measurably less energy per tick than moving bodies, and resting time rises when food is scarce in the logged data.

**685. Bodies move through water, not through walls**
- **Rule:** Water resists movement, surfaces block it, and the dish edge stops it: a body cannot pass through rock or leave the bounded world. Collisions cost energy and change direction, and the physics of water, mass, and friction apply the same way to every body.
- **Numbers:** Water resistance, collision energy cost, and dish boundary behaviour recorded; mass and size per body plan logged.
- **Check:** Bodies stop or turn at surfaces and the dish edge in the logged data, and mass and energy are conserved within documented error.

**686. Movement in currents**
- **Rule:** Currents carry bodies that do not resist them, and a body that swims against a current pays extra. A body senses the flow around it and can hold position, drift with it, or fight it, each at a different cost.
- **Numbers:** Current speeds, holding cost per tick, and drift distance per tick recorded.
- **Check:** Bodies drift downstream when they stop swimming in a current, and holding position costs the recorded energy per tick.

**687. Bodies that chase and bodies that are chased**
- **Rule:** When one body moves toward another and the other moves away, a chase happens with no script: the chaser follows sensed signals, the fleeing body follows its harm signal, and the outcome depends on speed, sensing, and energy. Predation is a later pressure with its own falsifier, not part of the pilot.
- **Numbers:** Chase speed, flee speed, chase duration, and energy cost per chase recorded; predation rate zero in pilot runs.
- **Check:** Chases are logged with durations and outcomes, and the pilot logs show zero predation events.

**688. Movement improves by selection**
- **Rule:** Bodies that move better reach food sooner and escape harm more often, so speed, turning, and energy efficiency of movement improve over generations. The improvement is measured as time to food and survival after a harm event.
- **Numbers:** Mean speed, turning rate, and time-to-food per generation logged; starting and ending means recorded per seed.
- **Check:** Mean time to food falls across generations in at least 4 of 5 seeds, with the numbers shown.

**689. Movement and the body plan together**
- **Rule:** How a body moves depends on its plan: a streamlined body swims fast, a broad body moves slowly but steadily, a body with a tail-like part beats it to push water. The plan and the movement evolve together, because a plan that cannot move cannot feed.
- **Numbers:** Speed and cost per body plan recorded; plan frequencies and their speeds logged per generation.
- **Check:** Speed differs by plan in the logged data, and plans whose movement cannot reach food decline in frequency.

**690. Movement record and sign-off**
- **Rule:** The record states speeds, costs, time to food, flight behaviour, and resting time per seed, with the comparisons against drifting bodies, and archives the runs. The phase advances only after sign-off.
- **Numbers:** Archive location, seed list, and final mean speeds recorded per seed.
- **Check:** The archive is confirmed complete and re-runnable, and the sign-off is recorded with the date.

### 7.10 Bodies in a real world

**691. Hunger and thirst at body scale**
- **Rule:** A body needs food and water: hunger rises with time and activity, thirst rises as water is lost, and both push the body to seek what it lacks. A body that finds neither loses energy and then dies; the drives are homeostatic, pushing back toward balance.
- **Numbers:** Hunger rise per tick, thirst rise per tick, energy gain per unit eaten, and water gain per drink recorded; death by starvation or dehydration logged with cause.
- **Check:** A body with no food or water dies with the cause logged, and fed bodies show hunger and thirst falling in the logged data.

**692. Sleep is physiological**
- **Rule:** Bodies sleep: they stop moving and sensing, save energy, and wake when hunger or thirst crosses a threshold, with daytime sleep capped so sleep does not eat the whole day. Sleep is a body state with a cost and a benefit, not a switch that pauses the world.
- **Numbers:** Sleep energy saving per tick, wake thresholds for hunger and thirst, and the daytime sleep cap recorded; sleep share of ticks logged.
- **Check:** Bodies wake on crossing the recorded hunger or thirst threshold in the logged data, and daytime sleep stays under the cap.

**693. Aging and death are permanent**
- **Rule:** Bodies age, weaken, and die, and death is permanent: no revival, no reset, no reuse of the body's agents. The body's lineage and history stay in the record, so what it learned and did outlives it only through its offspring and the record.
- **Numbers:** Lifespan distribution per seed logged; deaths logged with cause, generation, and time; death causes counted per run.
- **Check:** A dead body stays dead across checkpoint and resume, and the death log is complete for the run.

**694. Bodies live in a world that looks real**
- **Rule:** The world is drawn with ray-traced lighting, textured materials, and real water, rock, and living surfaces — no low-poly shapes standing in for the world. An eye-level view must let a watcher tell water from food, food from shelter, and one body from another.
- **Numbers:** Photoreal bar: ray-traced lighting, textured materials, no low-poly; eye-level screenshot review recorded per scene change.
- **Check:** A screenshot review distinguishes water, food, shelter, and bodies, and the review result is recorded; a scene that fails the bar is not called done.

**695. The world runs continuously**
- **Rule:** The world runs 24 hours a day, 7 days a week, with no time limit: bodies live, eat, reproduce, and die on the world's own clock, whether or not anyone is watching. Time limits apply only to bounded tests such as the pilot, never to the world itself.
- **Numbers:** World uptime and tick count logged; test caps stated separately as test caps, never as world caps.
- **Check:** The tick count rises while no observer is connected, and the run log shows births and deaths during unwatched periods.

**696. The world is watched, not steered**
- **Rule:** Watching changes nothing: the feed is read-only, one-way, and the world never senses the watcher. The Gateway contract is closed, serving one snapshot per frame over the stream, with a snapshot endpoint and a health endpoint, and no write path anywhere.
- **Numbers:** Contract version 1; snapshot fields include tick, population, births, and cell positions; a client marks a frame stale after 3 seconds without a new one.
- **Check:** The feed serves live state from the running world, and a test asserts no write path exists and no observation feedback reaches the simulation.

**697. The Discovery Principle holds at body scale**
- **Rule:** Bodies discover things through their own sensing, movement, and memory — new food, new places, new ways to live — and nothing is placed for them to find. The test is whether the owner could have predicted it: if yes, it was placed; if no, it was discovered.
- **Numbers:** Predicted list written before each run; discovered list written after; discoveries counted per run with generation and body.
- **Check:** At least one discovery per run is recorded as unpredicted by the owner, with the prediction list shown alongside it.

**698. The psychoactive plant rule is preserved for later**
- **Rule:** A mushroom-like psychoactive plant exists as a rule for a later stage, not as placed content now: it grows by the world's plant rules, must be found by inhabitants themselves, and its effect is simulated chemistry — a temporary loosening of the predictive model, with more noise, weaker priors, and higher plasticity — dose-dependent, time-limited, and costly.
- **Numbers:** Dose parameters are set by experiment, with Freebuff proposing the values and Muse reviewing them; no dose is fixed in this phase.
- **Check:** No plant is placed or labelled in this phase, and the preserved rule is recorded with the dose decision named as Freebuff proposes, Muse reviews.

**699. What bodies are ready for, and what they are not**
- **Rule:** Bodies with senses, movement, hunger, thirst, sleep, aging, and death are ready for the next phase — minds that grow with bodies — and are not yet animals with nervous systems, nor human-level minds, nor inhabitants of a town. The human-level bar stays as decided: all four tests must pass, and three out of four is not human-level.
- **Numbers:** Exit criteria: bodies survive, reproduce, sense, move, and die permanently across at least 5 seeds; human-level criteria listed as the destination bar, not claimed here.
- **Check:** The exit judgement is recorded with the numbers per seed, and no nervous-system, brain, or human-experiment claim appears in the record for this phase.

**700. Phase 7 record and sign-off**
- **Rule:** The record states the arc from chemistry to bodies — protocell numbers, pilot results, cell calibration, colonies, multicellularity, bodies, senses, and movement — with every claim backed by a measured result, every run archived, and the preserved decisions listed: species criterion, peer range 15 m and house-gap rule for the later town, physiological sleep, the plant rule, and the closed Gateway contract.
- **Numbers:** Archive locations, seed lists, and final numbers per milestone recorded; topic count 100, numbered 601–700 with no gaps.
- **Check:** The archive is confirmed complete and re-runnable, the sign-off is recorded with the date, and Phase 7 closes only after Muse signs off.

## Phase 8 — Life builds up: animals, brains, and behaviour

### 8.1 Animals

**701. What counts as an animal**
- **Rule:** An animal is a multicellular body whose cells are differentiated into tissues, that moves under its own power for at least part of its life, eats other organisms or their products, and reproduces as a body. Movement, eating, and a body plan held together across a lifetime separate animals from colonies that merely stick together.
- **Numbers:** Movement means sustained displacement above 0.1 body lengths per second for at least 60 seconds; eating means at least 50% of lifetime energy intake comes from consuming other organisms. Body plans are recorded as tissue counts and symmetry class.
- **Check:** A lineage is recorded as animal only when all three conditions are measured in the same run; the first animal's generation, body plan, and speed are logged, and the identification rule passes its test across ≥5 seeds.

**702. Animal movement — muscles and the cost of moving**
- **Rule:** Movement comes from contractile tissue that shortens against a body, converting chemical energy into motion; faster movement costs more energy per metre, and a body that moves all the time starves faster than one that rests between trips. Speed, endurance, and cost trade against each other, so different lineages settle on different gaits and budgets.
- **Numbers:** Movement cost starts at 0.05 energy units per body length travelled, doubling at twice the cruising speed; cruising speed starts at 0.5–2 body lengths per second. Freebuff proposes the starting cost curve, Muse reviews it.
- **Check:** An animal that moves reaches food measurably faster than a drifting body of the same size, and its energy ledger shows movement as a separate, positive cost in every logged run.

**703. Animal senses — vision, hearing, touch, smell**
- **Rule:** Animals sense the world through camera-like vision, sound direction and distance, contact, and chemical gradients, each sense reporting only what reaches the animal's own sensors. No sense reads the world state directly; a sense that cannot reach a thing cannot report it, so an animal can be fooled, can miss food, and can fail to notice a predator.
- **Numbers:** Vision starts at 30 m range with a 120° field; hearing at 50 m; touch at contact only; smell at 10 m downwind. Sensor dimensions and costs are recorded per species; Freebuff proposes the starting ranges, Muse reviews them.
- **Check:** An animal finds food by sight faster than a blind control of the same species across ≥5 seeds, and a sensor-block test shows behaviour changes when a sense is cut.

**704. Eating — foraging, grazing, hunting**
- **Rule:** Animals gain energy by finding and consuming food: grazing on sessile growth, foraging for scattered items, or hunting moving prey. Each mode costs time and energy to perform, and the gain must exceed the cost or the lineage starves; which mode a lineage uses is set by its body, senses, and what its ancestors learned, never by assignment.
- **Numbers:** A meal restores 20–60 energy units depending on food type; foraging costs 0.1 energy per second of searching; a hunt costs 0.5 energy per second of pursuit. Starting values are proposed by Freebuff and reviewed by Muse.
- **Check:** Foraging animals eat measurably more per day than random-moving animals of the same species, and the energy ledger per species shows intake minus foraging cost as a positive number.

**705. Predation — who eats whom, and the cost of the chase**
- **Rule:** Predation is a behaviour, not a label: one animal pursues, catches, and eats another, gaining its stored energy minus the cost of the chase. A predator that chases everything starves; a predator that never chases starves too, so the chase must be selective, and prey that escape teach the predator nothing except the cost of failing.
- **Numbers:** A successful catch transfers 40–70% of the prey's stored energy to the predator; a failed chase costs 5–15 energy units. Predation is nutrient-only-confined no longer: it arrives here as a Phase 4 pressure with its own falsifier, recorded per run.
- **Check:** A predator gains energy from a kill in the ledger, and across ≥5 seeds the food web persists — predators do not eat all prey in any seed.

**706. Defence — fleeing, hiding, armour, poison**
- **Rule:** Prey survive by fleeing, hiding, armouring, or being poisonous, each defence costing something: fleeing costs energy, hiding costs foraging time, armour costs growth, poison costs synthesis. No defence is free, so lineages balance defence against feeding, and a defence that costs more than the predation it prevents is selected against.
- **Numbers:** Fleeing costs 0.3 energy per second; hiding cuts foraging intake by 50% while hidden; armour adds 20% to growth cost; poison synthesis costs 2 energy per dose. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Prey with a defence survive measurably longer under predation than defenceless controls of the same species across ≥5 seeds, and the defence's cost appears in the energy ledger.

**707. Food webs — the ecology of eating**
- **Rule:** The food web is the recorded graph of who ate whom, built up from observed kills and meals, not from a designed chart. It changes as species appear, vanish, and change diet; a web that collapses to one species is a failed ecology, and a web where every species eats every other is a measurement error, not a result.
- **Numbers:** The web is logged per run as a species-by-species matrix with kill counts; stability means at least 3 species persist for at least 100 generations in ≥4 of 5 seeds. Freebuff proposes the stability thresholds, Muse reviews them.
- **Check:** The food-web matrix is published per run, and the species count at the end of each run is recorded; a web with fewer than 3 species is logged as collapsed, with its cause.

**708. Animal bodies — size, shape, and the cost of being big**
- **Rule:** Bigger bodies hold more energy, move faster in absolute terms, and can eat a wider range of food, but they cost more to grow, more to maintain, and more to reproduce. Body size is therefore a bargain struck with the ecology: big where food is rich and predators are few, small where food is scarce or hiding matters.
- **Numbers:** Maintenance cost scales with body mass to the power 0.75; growth cost is 10 energy units per gram of new tissue; reproduction costs 30% of the parent's stored energy. Starting exponents proposed by Freebuff, reviewed by Muse.
- **Check:** Body-mass distribution per species is logged per generation, and maintenance cost appears as a separate line in the energy ledger, rising with mass as predicted.

**709. Animal reproduction — new agent per offspring**
- **Rule:** An animal reproduces by producing offspring, each of which gets its own agent — its own mind, its own memory, its own life. The parent's agent never controls the child, and the child's mind starts fresh, with no copy of the parent's memories. Population grows through birth, never through placement.
- **Numbers:** Reproduction requires energy above 60% of maximum and age above the species' maturity threshold, which starts at 10% of expected lifespan. Litter or clutch size starts at 1–6, set by the species' evolved life history.
- **Check:** Agent count matches living animal count in every checkpoint, and a reproduction test shows an offspring with its own fresh agent; no agent is placed by hand after the initial seeding.

**710. Animal death — permanent, recorded, and ecologically real**
- **Rule:** Animals die from starvation, predation, injury, disease, or age, and death is permanent: no revival, no reset, the agent is retired and never reused. Dead animals remain in the historical record with their lineage, so a death is a fact about the world, not a deleted row.
- **Numbers:** Starvation kills at energy zero; age kills at a lifespan drawn from the species' evolved range, starting at 100–1,000 days; injury kills when damage exceeds 80% of body integrity. Causes are tallied per run.
- **Check:** Every death is logged with cause, age, and time; a starved animal stays dead in a test; the death-cause counts per seed are published, and the survival curve per species is recorded.

### 8.2 Nervous systems

**711. Nerve nets — the first nervous systems**
- **Rule:** A nerve net is a spread of connected neurons with no centre: a signal entering anywhere spreads to nearby neurons, and the body responds as a whole — contracting, turning, or withdrawing. It is the simplest nervous system, and it works because the body's sensors and muscles share the same net, with no brain in between.
- **Numbers:** A nerve net starts at 20–100 neurons, each connected to its 4–8 nearest neighbours; signal speed starts at 0.5 m per second through the net. Freebuff proposes the starting sizes, Muse reviews them.
- **Check:** An animal with a nerve net withdraws from a touch measurably faster than an animal with no neurons, and the withdrawal time is logged per trial across ≥5 seeds.

**712. Reflexes — fast answers with no thinking**
- **Rule:** A reflex is a fixed, short path from sensor to muscle: touch triggers withdrawal, bright light triggers turning away, a sudden sound triggers freezing. Reflexes cost almost nothing and need no memory, but they cannot learn, cannot choose, and can be fooled by a stimulus that looks like danger and is not.
- **Numbers:** A reflex fires within 50–200 ms of the stimulus; a reflex path is 2–4 neurons long; the false-alarm rate is recorded per species. Starting latencies proposed by Freebuff, reviewed by Muse.
- **Check:** Reflex latency is measured per trial, and a reflex test shows the same stimulus producing the same response in the same animal on repeated trials.

**713. Ganglia — local centres that decide**
- **Rule:** A ganglion is a cluster of neurons that gathers signals from one part of the body and decides what that part does, without asking the rest of the body. Ganglia let a limb react to what it touches while the head is busy elsewhere, and they are the first step from a spread-out net toward a centralised system.
- **Numbers:** A ganglion starts at 50–500 neurons; local decisions take 100–500 ms; a body starts with 2–6 ganglia, one per major body region. Freebuff proposes the starting counts, Muse reviews them.
- **Check:** A limb with its own ganglion reacts to a local stimulus while the rest of the body is occupied, and the reaction time is logged per trial.

**714. Centralisation — from net to cord to brain**
- **Rule:** Centralisation is the evolutionary drift of neurons toward one end of the body, where the main senses sit, until a cord and then a brain form. It is not designed: lineages whose neurons cluster near their eyes and mouths respond faster to what they see and eat, so clustering spreads by selection, and the brain is the end of that drift, not its starting point.
- **Numbers:** Centralisation is measured as the fraction of neurons within the front third of the body, starting below 0.4 in nerve nets and rising above 0.7 in brained animals. The fraction is logged per species per generation.
- **Check:** The centralisation fraction rises across generations in at least one lineage per run, and the rise correlates with faster response times in the same lineage.

**715. Sensory processing — turning signals into a picture of the world**
- **Rule:** Sensory processing is what neurons do between a sensor firing and a muscle moving: combining signals, filtering noise, detecting edges, movement, and change. A nervous system that only passes signals through is a reflex; one that combines them can tell a predator's shadow from a cloud's, and that difference is worth the neurons it costs.
- **Numbers:** Processing depth starts at 1–3 layers of neurons between sensor and muscle; a processing layer costs 0.01 energy per tick per neuron. Freebuff proposes the starting depths, Muse reviews them.
- **Check:** An animal with two processing layers distinguishes a moving threat from a moving shadow measurably better than a one-layer control, with the confusion rate logged per trial.

**716. Motor control — from twitch to coordinated movement**
- **Rule:** Motor control is the nervous system's command of muscles: first a twitch, then a contraction, then coordinated sequences that walk, swim, or fly. Coordination means the right muscles fire in the right order at the right time, and it is learned and refined by the animal's own experience of what its body does when it tries.
- **Numbers:** Coordination is measured as the fraction of muscle activations that move the animal toward its sensed goal, starting below 0.3 in early movers and above 0.7 in coordinated ones. Movement efficiency is logged per species.
- **Check:** Coordinated animals reach a food source in fewer steps and less energy than uncoordinated animals of the same body plan, with the step and energy counts logged per trial.

**717. Pain and damage sensing — the cost signal**
- **Rule:** Pain is a signal that reports tissue damage to the nervous system, weighted by how bad the damage is, so the animal learns to avoid what hurt it. It is not a punishment from outside; it is the body's own report, and an animal that cannot feel damage keeps injuring itself until it dies.
- **Numbers:** Damage above 5% of body integrity produces a pain signal; the signal strength scales linearly with damage up to 100% at 50% integrity loss; pain raises the learning rate for the associated action by 2×. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Animals with damage sensing avoid a harmful stimulus after one exposure measurably more often than animals without it, and the avoidance rate is logged per trial.

**718. Internal sensing — hunger, thirst, fatigue, temperature**
- **Rule:** Internal sensing reports the body's own state — energy stores, water, fatigue, temperature — to the nervous system, so drives can be felt rather than computed from outside. An animal that cannot feel hunger does not seek food until it is too late; an animal that cannot feel cold does not seek shelter until it freezes.
- **Numbers:** Hunger is reported when energy falls below 70% of maximum; thirst below 60% of water stores; fatigue after 8 hours of continuous activity; cold below the species' comfort band, starting at 10–30 °C. Thresholds proposed by Freebuff, reviewed by Muse.
- **Check:** An animal seeks food measurably sooner after the hunger signal appears than a control with the signal cut, and the delay between signal and feeding is logged.

**719. Nervous system cost — brains are expensive**
- **Rule:** Every neuron costs energy to build and to run, so a bigger nervous system must pay for itself in better decisions. A lineage that grows neurons without gaining survival loses to one that spends the same energy on muscle or fat; the size of a nervous system is therefore set by what it earns, not by what is possible.
- **Numbers:** Each neuron costs 0.001 energy per tick to run and 0.1 energy to build; a nervous system above 1% of body mass must show a survival gain or it is recorded as overbuilt. Starting costs proposed by Freebuff, reviewed by Muse.
- **Check:** The energy ledger shows nervous-system cost as a separate line per species, and species with larger nervous systems show higher survival per unit of cost, or the excess is logged as overbuilt.

**720. Nervous system evolution — measured, never placed**
- **Rule:** Nervous systems change only through reproduction with mutation and selection: offspring inherit a nervous system like their parent's, with small changes, and the changes that help survival spread. No nervous system is designed, installed, or upgraded by hand; the ladder from net to ganglion to brain is climbed by lineages, and a lineage can stall or slide back.
- **Numbers:** Neuron count mutates by ±5% per generation; connection changes occur at 1 per 100 connections per generation; the ladder is judged over ≥5 seeds. Mutation rates proposed by Freebuff, reviewed by Muse.
- **Check:** Neuron counts and centralisation fractions are logged per lineage per generation, and no lineage's nervous system changes except through a recorded birth event.

### 8.3 Brains (hybrid mind at animal scale)

**721. The hybrid mind at animal scale — one family, sized to the body**
- **Rule:** Every animal runs the same hybrid mind family — a neural core, a forward model, and episodic memory — sized to its body and its niche, exactly as the cell minds were sized to cells. A small animal gets a small mind, a large animal a larger one, but the parts are the same parts, the rules are the same rules, and no animal gets a different kind of mind.
- **Numbers:** Mind size scales with body mass to the power 0.5, starting at 50 neurons for the smallest animals and rising to 100,000 for the largest in this phase; the sizing formula is recorded and the fruit-fly brain sits near the midpoint of the ladder.
- **Check:** The same code constructs minds at three sizes in a test, and the mind-size-to-body-mass curve is published per species; no animal runs a different architecture family.

**722. The neural core at animal scale — the fruit-fly-inspired centre**
- **Rule:** The neural core is a recurrent network of spiking-style neurons that takes the animal's senses in and produces its actions out, learning by a plasticity rule that strengthens connections that predict well and weakens those that do not. It is inspired by the fruit fly's brain — small, complete, and sufficient for a real life — and it is the centre of the mind, not an accessory.
- **Numbers:** The core starts at 100–10,000 neurons depending on body size; the plasticity rate starts at 0.01 per update; the core's decision rate is 10 decisions per second. Starting sizes proposed by Freebuff, reviewed by Muse.
- **Check:** The core's behaviour changes with experience in a test — the same animal acts differently after learning than before — and the change is logged with the numbers.

**723. The forward model at animal scale — predicting what happens next**
- **Rule:** The forward model predicts the animal's next sensory input from its current senses and its chosen action, and the gap between the prediction and what actually happens is the surprise that drives learning. A model that predicts well lets the animal act before the world answers; a model that predicts badly is retrained by its own errors, not by an outside teacher.
- **Numbers:** Prediction error is measured as mean squared error over the sensor vector; it must fall by at least 50% over the first 1,000 decisions in a run; the model is sensor-only, never conditioned on the network's own drifting output. E-002's rejected action-conditioned form stays rejected.
- **Check:** The prediction-error curve is logged per animal, and a test shows error falling with experience; a model whose error never falls is recorded as unlearned, not as working.

**724. Episodic memory at animal scale — remembering what happened**
- **Rule:** Episodic memory stores what happened to this animal — where it found food, where it was hurt, who it met — as episodes it can recall when a similar situation returns. Memory belongs to one agent only: no animal reads another's episodes, and an offspring starts with an empty memory, however much its parent knew.
- **Numbers:** Memory capacity scales with mind size, starting at 100 episodes for the smallest minds and 10,000 for the largest; an episode costs 0.01 energy to store and 0.001 to recall. Starting capacities proposed by Freebuff, reviewed by Muse.
- **Check:** An animal with memory returns to a known food source measurably faster than one without, and a test shows the offspring's memory is empty at birth.

**725. The planner stays cut — no steering layer at any scale**
- **Rule:** There is no planner steering layer in any animal mind: no hand-designed rule that steers the animal toward a goal, no drive-gated steering, no multi-ray voting. The v4 evidence — 4,493 interventions with no separation — closed that question, and the cut holds at animal scale exactly as it holds at cell and human scale.
- **Numbers:** Planner flag is False in every population arm at every scale; the planner code stays behind a flag for the research track only, and any research-track return needs a new steering idea and a falsifier, reviewed by Muse before it runs.
- **Check:** A test asserts no planner code executes in any population run, and the three-arm harness at animal scale runs with the population and no-planner arms identical.

**726. Drives at animal scale — hunger, thirst, fear, curiosity, social**
- **Rule:** Drives are homeostatic signals that push the animal back toward balance: hunger rises as energy falls, thirst as water falls, fear as danger nears, curiosity as novelty appears, and the social drive as isolation grows. No drive is a command; each is a weight on the mind's choices, and hunger still wins over curiosity when the animal is starving.
- **Numbers:** Hunger and thirst rise 1 unit per hour at rest and 2 per hour active; fear spikes to 10 on a predator sighting and decays over 60 seconds; the social drive rises 0.5 per hour alone and is relieved only by a perceived peer within 15 m.
- **Check:** Drive levels are logged per animal per hour, and a test shows a starving animal choosing food over novelty, with the choice logged.

**727. Sleep and consolidation at animal scale — the mind keeps what it learned**
- **Rule:** Sleep is physiological: the animal wakes when thirst or hunger crosses a threshold, and daytime sleep is capped, so sleep does not eat the animal's life. While asleep the mind replays episodes and refits the forward model — consolidation — which is the only decision work done in sleep, and the rest of the decision path is skipped.
- **Numbers:** Wake thresholds are thirst below 40% and hunger below 40%; daytime sleep is capped at 2 hours; consolidation replays 10 episodes per sleep hour. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Animals that sleep retain measurably more of a learned route than animals kept awake, and the sleep-skipped decision share is logged per run.

**728. Perception without omniscience — the mind sees only what its senses bring**
- **Rule:** The animal mind receives only its sensor vector — what its eyes, ears, skin, and chemical sensors report — and nothing else. It cannot read the world state, another animal's mind, or the future; it must infer, guess, and sometimes be wrong, and being wrong is how the forward model learns.
- **Numbers:** The sensor vector dimension is recorded per species, starting at 12 for the simplest animals and rising to 40 for the most sensing-rich; the vector is the mind's only input, and any other channel is a bug. Freebuff proposes the starting dimensions, Muse reviews them.
- **Check:** A test cuts a sense and shows behaviour changing accordingly, and a code check asserts the mind's input is the sensor vector alone.

**729. Mind cost at animal scale — the brain must earn its keep**
- **Rule:** A bigger mind costs more energy every tick, so a species earns a bigger brain only when the brain pays for itself in survival: better foraging, better escape, better memory of where food is. A mind that costs more than it returns is selected against, and the mind-size ladder is climbed by earnings, not by ambition.
- **Numbers:** Mind cost is 0.001 energy per neuron per tick plus 0.01 per stored episode per day; a mind above 5% of the animal's daily energy budget must show a survival gain in the same run or it is logged as overbuilt.
- **Check:** Mind cost appears as a separate line in the energy ledger per species, and survival per unit of mind cost is published per seed.

**730. The animal mind is one mind — no tiers, no brain-dead animals**
- **Rule:** Every animal, whatever its species or size, runs the same hybrid mind family — neural core, forward model, episodic memory — with no brain-dead tier and no separate simple controller for the small ones. The smallest animal's mind is a small version of the same mind, not a different kind of thing, and the population is the max the hardware can carry, measured not guessed.
- **Numbers:** Mind size is set only by the sizing formula from topic 721; no species is assigned a reduced architecture; the population cap is measured per run as the count the hardware sustains at the target tick rate.
- **Check:** A test constructs the mind for the smallest and largest species from the same code path, and the population count per run is logged against the tick rate.

### 8.4 Learning

**731. Habituation — learning to ignore what does not matter**
- **Rule:** Habituation is the mind's way of spending less attention on a stimulus that keeps appearing without consequence: the first rustle startles, the tenth is ignored. It saves energy and attention for what is new, and it reverses when the stimulus starts to matter — a rustle followed by teeth is startling again.
- **Numbers:** The response to a harmless repeated stimulus falls by at least 50% within 10 exposures; the habituation rate starts at 0.1 per exposure; reversal takes 1–2 exposures after a harmful pairing. Starting rates proposed by Freebuff, reviewed by Muse.
- **Check:** Response strength per exposure is logged, and a test shows the response falling across exposures and recovering after a harmful pairing.

**732. Associative learning — this predicts that**
- **Rule:** Associative learning links a neutral signal to a consequence: a smell that precedes food becomes a signal for food, a shadow that precedes a predator becomes a signal for danger. The link is formed by the plasticity rule when the two events co-occur, and it fades when they stop co-occurring, so the animal's associations track the world as it changes.
- **Numbers:** An association forms after 3–10 pairings; it fades to half strength after 20 unpaired presentations; the learning rate for associations starts at 0.05 per pairing. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** An animal approaches a smell it learned predicts food measurably more often than a control smell, and the approach rate is logged per trial across ≥5 seeds.

**733. Trial and error — learning by doing, and paying for mistakes**
- **Rule:** Trial and error is learning from the outcome of the animal's own actions: an action that led to food is repeated, one that led to pain is avoided. The cost is real — the animal pays in energy, time, and sometimes injury for the trials that fail — and that cost is what makes the learning honest rather than free.
- **Numbers:** A successful action's weight rises 0.1 per success; a failed action's weight falls 0.1 per failure; at least 20 trials are needed before a new action is judged learned or not. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** The success rate of a learned action rises across trials in the log, and a test shows the same animal choosing the successful action more often after 20 trials than before.

**734. Curiosity — the drive to explore what is new**
- **Rule:** Curiosity is an intrinsic drive that rewards the mind for surprise: a novel place, a new smell, an unfamiliar object draws the animal in, because the forward model's error is highest where the world is unknown. Curiosity never overrides survival drives — a hungry animal eats first — but it is what finds the food source nobody knew about.
- **Numbers:** Curiosity weight starts at 0.2 of the decision weight; novelty is measured as forward-model prediction error above 0.5; exploration time is capped at 20% of the waking day. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Curious animals discover a new food source in a test measurably more often than non-curious controls, and the discovery count per seed is logged.

**735. Learning from pain — one trial can be enough**
- **Rule:** A single painful event can teach what ten safe trials cannot: the animal that is bitten once avoids the biter's territory, the animal that eats a poisonous berry once avoids that colour. Pain raises the learning rate for the action that caused it, so the lesson sticks after one exposure, and the cost of the lesson is the injury itself.
- **Numbers:** Pain multiplies the learning rate by 2× for the associated action; a one-trial avoidance forms when damage exceeds 10% of body integrity; the avoidance lasts at least 7 days without reinforcement. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Avoidance after a single painful trial is measured per animal, and the avoidance rate is logged across ≥5 seeds.

**736. Learning from success — repeating what worked**
- **Rule:** Success teaches by reward: an action that ends in food, safety, or a mate is more likely next time, and the more it succeeds, the stronger the pull. The mind keeps a running record of what worked in which situation, and that record — not a script — is what the animal follows when the same situation returns.
- **Numbers:** Each success raises the action's weight by 0.1, capped at 1.0; weights decay 0.01 per day without use; a behaviour is judged learned when its success rate exceeds 70% over 20 trials. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** The success rate of a repeated action is logged per animal, and a test shows the rate rising from below 50% to above 70% over the learning period.

**737. Generalisation — what was learned here applies there**
- **Rule:** Generalisation is the mind applying a learned lesson to a new but similar situation: the animal that learned one red berry is poisonous avoids other red berries, and the animal that learned one river is drinkable tries another river. It saves relearning everything from scratch, and it can misfire — a safe red berry avoided is a meal lost — which is the price of the shortcut.
- **Numbers:** Generalisation strength starts at 0.5 for stimuli sharing at least 70% of their features with the learned one; the misfire rate is logged per species. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** An animal avoids a novel stimulus similar to a learned danger measurably more often than a dissimilar control, and the generalisation rate is logged per trial.

**738. Learning speed — fast learners, slow learners, and the trade**
- **Rule:** Learning speed is set by the plasticity rate: a fast learner adapts in a few trials but forgets fast and can learn the wrong thing from one coincidence, while a slow learner takes longer but holds its lessons. Different lineages settle at different speeds because the trade is real, and the speed itself is inherited with mutation.
- **Numbers:** Plasticity rate starts at 0.01–0.1 per update across species; fast learners are defined as reaching 70% success within 10 trials, slow learners within 50. Starting rates proposed by Freebuff, reviewed by Muse.
- **Check:** Learning speed per species is logged, and a comparison across ≥5 seeds shows fast and slow learners surviving differently in stable versus changing environments.

**739. Learning without a teacher — the world is the only instructor**
- **Rule:** No animal is taught by the owner, by a script, or by a placed lesson: every lesson comes from the world itself — from food found, pain felt, a peer watched, or a place explored. A mind that learns only from the world can be wrong about the world, and that wrongness is measurable, which is what makes the learning real.
- **Numbers:** Zero owner-placed lessons in any run; every learning event is logged with its cause — food, pain, observation, or exploration — and the cause counts are published per run.
- **Check:** A code and log audit shows no learning event with an owner-placed cause, and the learning-event cause counts are published per seed.

**740. The learning bar — learned animals beat random animals**
- **Rule:** Learning is judged the same way at every scale: the learned population beats the random control on survival and on reproduction across at least 5 seeds, judged by the three-arm harness. If the learned animals do not beat random, the learning is not working, and the failure is recorded with the next single change and its falsifier — not tuned away.
- **Numbers:** The bar is survival and reproduction, both higher for the learned arm than the random arm, across ≥5 seeds; the harness runs population, no-planner, and random arms identically, with planner=False throughout.
- **Check:** The harness numbers are published per seed per arm, and the bar judgement is recorded as pass or fail with the numbers, submitted to Muse for review.

### 8.5 Memory

**741. Short-term memory — holding the present long enough to act**
- **Rule:** Short-term memory holds the last few seconds of sensation and action so the animal can finish what it started: following a scent trail, tracking a moving prey, remembering where the hole was a moment ago. It fades within seconds, and what is not used or stored is gone, which is why the animal must act while the trace is fresh.
- **Numbers:** Short-term capacity starts at 5–10 items; the trace decays to half strength in 10 seconds; a trace that is rehearsed or rewarded moves to episodic memory. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** An animal follows a scent trail measurably better with its short-term trace intact than with it cut, and the trail-following success rate is logged per trial.

**742. Episodic memory — the animal's own history**
- **Rule:** Episodic memory is the record of what happened to this animal, in order, with place and outcome attached: where food was, where danger was, who was there. It is the animal's history, and it is what lets the animal return to a good place, avoid a bad one, and recognise a peer it has met before.
- **Numbers:** Capacity scales with mind size, from 100 episodes in the smallest minds to 10,000 in the largest; episodes older than the capacity are forgotten oldest-first; recall takes 10–50 ms. Starting capacities proposed by Freebuff, reviewed by Muse.
- **Check:** An animal returns to a remembered food source measurably faster than an animal with its memory cut, and the return time is logged per trial across ≥5 seeds.

**743. Spatial memory — maps made of experience**
- **Rule:** Spatial memory is the map the animal builds from its own movement: which way the water is, where the den is, how far the food patch lies. It is not a given map of the world; it is assembled from episodes, it has errors, and it is corrected every time the animal travels and finds the world different from its map.
- **Numbers:** A map is judged accurate when the animal reaches a remembered place within 10% of the direct distance; map error is logged per trip; maps hold 5–50 places depending on mind size. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Travel distance to a remembered place is logged per trip, and a test shows the distance falling as the map is corrected over repeated trips.

**744. Memory consolidation — sleep turns experience into knowledge**
- **Rule:** Consolidation is the replay of the day's episodes during sleep, refitting the forward model and strengthening the associations that mattered, so that what was learned while awake survives the night. It is the only decision work done in sleep; everything else is skipped, and a mind that never sleeps keeps its raw episodes but never turns them into usable knowledge.
- **Numbers:** Consolidation replays 10 episodes per sleep hour, chosen by surprise and by reward; a consolidated episode's recall strength rises 0.1 per replay; sleep is capped in the day and woken by thirst or hunger thresholds, per topic 727.
- **Check:** Animals that sleep retain a learned route measurably better the next day than animals kept awake, and the retention difference is logged per run.

**745. Forgetting — losing what no longer matters**
- **Rule:** Forgetting is the mind letting go of episodes that are old, unused, or contradicted, so that memory stays small enough to search and fresh enough to trust. An animal that remembered everything would drown in its own past; forgetting is not a defect but the price of a working memory, and what is forgotten can be relearned.
- **Numbers:** An unused episode decays 0.01 strength per day; an episode contradicted by a new experience loses half its strength at once; capacity is enforced oldest-first once full. Starting rates proposed by Freebuff, reviewed by Muse.
- **Check:** Memory size per animal is logged over time and stays within capacity, and a test shows an outdated association fading after the world changes.

**746. Recognition — knowing a peer, a place, a predator**
- **Rule:** Recognition is matching a present sensation to a stored episode closely enough to act on it: this smell is the predator from last week, this face is the peer that shared food, this place is the den. It is a judgement, not a certainty, and it can be wrong — a harmless animal mistaken for a predator costs a meal, a predator mistaken for harmless costs a life.
- **Numbers:** Recognition triggers when similarity exceeds 0.7 on the episode's feature vector; the false-recognition rate is logged per species; recognition takes 20–100 ms. Starting threshold proposed by Freebuff, reviewed by Muse.
- **Check:** Recognition accuracy is measured per trial — correct recognitions against false ones — and the rates are logged per species across ≥5 seeds.

**747. Memory is per-agent — no shared minds**
- **Rule:** Memory belongs to one agent and one agent only: no animal reads another's episodes, no animal inherits its parent's memories, and no central store holds what the group knows. What the group knows lives in the members' separate memories and in what they show each other, never in a shared file.
- **Numbers:** Zero cross-agent memory reads in any run; an offspring's memory is empty at birth; a test asserts that one animal's recall does not change another's stored episodes. These are checked by code audit and by test.
- **Check:** A test shows two animals with different experiences holding different memories after the same events, and the audit log shows no cross-agent reads.

**748. Memory and the forward model — the past predicts the future**
- **Rule:** Memory feeds the forward model: when a situation matches a stored episode, the model predicts what happened last time, and the animal acts on that prediction before the world answers. This is why an animal that has been somewhere before moves with confidence and an animal in a new place moves cautiously — the past is the only guide to the future either of them has.
- **Numbers:** A prediction backed by a matching episode starts with 0.3 lower error than a prediction with no match; the error gap is logged per decision; the match threshold is a similarity of 0.7. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Prediction error is logged with and without a matching episode, and the gap is published per species per run.

**749. Memory failure — what happens when the record is wrong**
- **Rule:** Memory can be wrong: an episode can be misremembered, a place can have changed since it was stored, a peer can have changed its ways. When the world contradicts the memory, the animal pays — it walks to a dry waterhole, it trusts a rival — and the contradiction itself is the signal that updates the memory, if the animal survives the mistake.
- **Numbers:** Memory-based prediction error above 0.8 triggers a memory update that halves the episode's strength; the rate of memory-led errors is logged per species. Starting threshold proposed by Freebuff, reviewed by Muse.
- **Check:** The rate of decisions that fail because the memory was outdated is logged, and a test shows the rate falling as memories are updated.

**750. The memory bar — memory earns its cost**
- **Rule:** Memory is judged by the same rule as every other part of the mind: animals with episodic memory must outperform animals without it on survival and on finding food, across at least 5 seeds, or the memory is not earning the energy it costs. The comparison is run with the same bodies, the same world, and the same seeds, differing only in whether memory is on.
- **Numbers:** The bar is survival and food-finding rate, both higher for the memory arm, across ≥5 seeds; memory cost is logged as a separate line in the energy ledger.
- **Check:** The comparison numbers are published per seed, and the bar judgement is recorded as pass or fail with the numbers, submitted to Muse for review.

### 8.6 Communication

**751. Signals — making a sound, a movement, a smell that others can sense**
- **Rule:** A signal is an action an animal takes that other animals can sense: a call, a posture, a scent mark, a flash of colour. Signals cost energy and attention to make, and they can be heard by predators as well as peers, so an animal signals only when the benefit outweighs the risk of being noticed.
- **Numbers:** A call costs 0.1 energy and carries 30 m; a scent mark costs 0.5 energy and lasts 24 hours; a visual display costs 0.2 energy and carries 20 m in clear sight. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Signal events are logged with type, sender, and receivers in range, and a test shows a signal changing a receiver's behaviour within 5 seconds.

**752. Alarm calls — warning the group at a cost to the caller**
- **Rule:** An alarm call warns peers that a predator is near, and it costs the caller: calling draws the predator's attention to the caller first. The call spreads because callers whose kin survive pass on the tendency to call, and because a group that is warned survives better than a group that is not — the benefit lands on the group, the risk lands on the caller.
- **Numbers:** An alarm call raises the group's escape rate by at least 30% in a test; the caller's own predation risk rises by 10% when calling; calls are logged per event. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Group survival after an alarm is logged against survival without one, and the caller's risk is measured in the same runs across ≥5 seeds.

**753. Food calls — telling others where the food is**
- **Rule:** A food call tells peers where food was found, trading a share of the find for the benefit of feeding together — safety in numbers, and help in handling food too big for one animal. A caller that always calls and never finds goes hungry; a finder that never calls eats alone and watches its own back, so the balance between calling and keeping quiet is set by what the ecology rewards.
- **Numbers:** A food call brings 1–5 peers to the site within 60 seconds; the caller's share falls by 20% per arriving peer; the call's benefit is measured in reduced predation while feeding. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Arrival counts and the caller's intake with and without calling are logged, and the comparison is published per seed.

**754. Mating signals — being noticed by the right animal**
- **Rule:** Mating signals advertise an animal to potential mates: a song, a display, a scent that says this animal is healthy, strong, and ready. The signal costs energy and attracts predators as well as mates, so only animals that can afford the cost signal loudly, and the loudness itself becomes the honest measure of the signaller's condition.
- **Numbers:** A display costs 0.5 energy per minute; display strength correlates with the signaller's energy stores at 0.7 or above; mating success is logged per displaying animal. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Mating success is logged against display strength, and the correlation between condition and display is published per species.

**755. Signal meaning comes from use — nothing is assigned**
- **Rule:** No signal meaning is placed by the owner: a call means danger because it is used when danger is near and listeners learn to flee when they hear it, not because anyone declared it. Meanings emerge from use, drift when use drifts, and die when a signal stops being used — the dictionary is written by the animals, in their behaviour, and read back by us from the logs.
- **Numbers:** A signal's meaning is recorded as the receiver behaviour it most often causes, with the rate logged; a meaning is judged stable when the same signal causes the same behaviour in at least 80% of cases over 100 events.
- **Check:** The signal-to-behaviour table is published per run, and a test shows a novel signal acquiring a meaning through use within one run.

**756. Deception — signals that lie, and listeners that learn**
- **Rule:** A signal can lie: an animal can give a food call with no food, or an alarm with no predator, gaining attention or scattering rivals at the cost of trust. Listeners that keep believing a liar lose out, so they learn to discount a signaller whose calls prove false — and the liar's calls stop working, which is the only punishment deception ever receives.
- **Numbers:** A false call rate above 30% halves the listeners' response within 20 events; the discount is logged per signaller-receiver pair. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Response rates to a signaller are logged before and after its false calls, and the drop is published per run.

**757. Listening — the receiver's half of communication**
- **Rule:** Communication is half listening: a receiver must attend to a signal, match it to memory, and decide whether to act, and all of that costs attention that could have gone to foraging or watching for predators. An animal that listens to everything starves; an animal that listens to nothing dies unwarned, so attention itself is a resource the mind must budget.
- **Numbers:** Attending to a signal costs 0.05 energy and 1 second of foraging time; a receiver acts on a signal only when its similarity to a remembered signal exceeds 0.7; ignored signals are logged. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Receiver response rates are logged per signal type, and a test shows receivers acting on familiar signals more often than on novel ones.

**758. Communication range — near signals, far signals, and the 15 m rule**
- **Rule:** Signals travel only as far as physics carries them: a call fades with distance, a scent drifts with the wind, a display is hidden by cover. The peer range of 15 m from the human-scale decisions is the distance within which a peer is reliably perceived, and animal signals are judged against the same honesty — a signal that reaches further is a louder signal, not a different kind of perception.
- **Numbers:** Call range starts at 30 m, scent at 10 m downwind, visual display at 20 m in the open and 5 m in cover; peer perception holds at 15 m. Starting ranges proposed by Freebuff, reviewed by Muse.
- **Check:** Signal reception is logged with distance, and a test shows reception falling to zero beyond the stated range for each signal type.

**759. Communication cost — signalling is never free**
- **Rule:** Every signal costs something — energy to make, time to attend, risk of being heard by the wrong listener — and a species that signals constantly pays for it in shorter lives and fewer offspring. The cost is what keeps signals honest: a call that costs nothing would be made all the time and would mean nothing, so the price is the meaning's guarantee.
- **Numbers:** Signal costs are logged as a separate line in the energy ledger per species; total signalling cost must stay below 5% of daily energy, or the species is logged as over-signalling. Starting cap proposed by Freebuff, reviewed by Muse.
- **Check:** The signalling cost line is published per species per run, and a comparison shows over-signalling species surviving worse across ≥5 seeds.

**760. The communication bar — signals earn their cost**
- **Rule:** Communication is judged like everything else: animals that can signal and listen must outperform animals that cannot, on survival and on group coordination, across at least 5 seeds, with the same bodies and the same world. If signals do not help, they are noise, and the failure is recorded with the next single change and its falsifier.
- **Numbers:** The bar is survival and coordination — measured as the fraction of group members acting together within 10 seconds of a signal — both higher for the signalling arm across ≥5 seeds.
- **Check:** The comparison numbers are published per seed, and the bar judgement is recorded as pass or fail, submitted to Muse for review.

### 8.7 Social life

**761. Groups — animals gather, and gathering changes them**
- **Rule:** Groups form when animals gather near each other for food, safety, or mating, and gathering changes every member: more eyes watch for predators, more mouths share the food, more bodies compete for the same patch. Groups form and break up on their own; no group is assigned, and no animal is permanently a member of one.
- **Numbers:** A group is defined as 3 or more animals of one species within 10 m for at least 10 minutes; group sizes are logged per species per generation; grouping raises predator detection by 20% per extra member, up to 5 members. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Group sizes are published per run, and grouped animals are compared against solitary animals on survival across ≥5 seeds.

**762. Dominance — who eats first, who mates, who decides**
- **Rule:** Dominance is the settled outcome of repeated contests: the animal that wins more often eats first, mates more, and is challenged less, and the order holds until a challenger wins. It is not a rank assigned by anyone; it is the memory of who beat whom, held in every member's episodic memory, and it shifts when the record of wins shifts.
- **Numbers:** A dominance order is recorded when the same animal wins at least 70% of its contests over 20 contests; contests cost the loser 5 energy and the winner 2. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Contest outcomes are logged per pair, and the dominance order is published per group per run, with its stability measured over time.

**763. Cooperation — helping, and paying for it**
- **Rule:** Cooperation is an animal paying a cost to help another: sharing food, standing guard, defending a peer. It spreads when the helped animal is kin, or when the help is returned later, or when the group that cooperates outlives the group that does not — and it dies out when helpers are exploited without return, because the cost is real and the ledger does not forgive.
- **Numbers:** A cooperative act costs the helper 5–15 energy and gains the helped animal 10–30; cooperation is logged per event with helper, helped, cost, and gain; the return rate is published per run. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Cooperating groups are compared against non-cooperating groups on survival across ≥5 seeds, and the helper's cost appears in its energy ledger.

**764. Conflict — competing for food, mates, and space**
- **Rule:** Conflict is competition made physical: two animals want the same food, the same mate, or the same den, and one of them yields or is driven off. Conflict costs energy and risks injury, so animals that can settle a contest by display rather than by fighting do better, and the display itself becomes a signal whose meaning is written by who backs down.
- **Numbers:** A fight costs 10–30 energy and risks injury above 20% of body integrity; a display contest costs 2 energy; conflict outcomes are logged per event. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Conflict outcomes and their costs are published per run, and species that settle by display are compared against species that fight on survival across ≥5 seeds.

**765. Avoidance — knowing when not to fight**
- **Rule:** Avoidance is the animal that loses, or expects to lose, leaving before the fight starts: it reads the rival's size, its display, and its own memory of past contests, and it walks away. Avoidance costs the contested resource but saves the injury, and an animal that never avoids dies in fights it could have walked away from.
- **Numbers:** Avoidance is recorded when an animal leaves a contest site within 10 seconds of a rival's display; the avoided resource's value and the saved injury cost are logged per event. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Avoidance events are logged per run, and avoiders are compared against fighters on survival and injury rates across ≥5 seeds.

**766. Kin and parental care — feeding the young**
- **Rule:** Parental care is the parent spending energy and time on offspring that cannot yet feed themselves: guarding, feeding, carrying, teaching by presence. It costs the parent's own survival and reproduction, and it spreads because the offspring that receive it survive better — the parent's genes live on in the young it raised, not in the parent itself.
- **Numbers:** Parental care costs 10–20% of the parent's daily energy for the first 10–30% of the offspring's life; cared-for offspring survive at least 20% better than uncared-for ones in a test. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Offspring survival with and without care is logged per species, and the parent's cost appears in its energy ledger.

**767. Play — practice that looks like fun and costs like work**
- **Rule:** Play is young animals practising adult behaviours — chasing, wrestling, stalking — at low stakes, where the cost of failure is a tumble instead of a death. It costs energy and time, and it pays in skill: an animal that played hunts better, fights better, and escapes better than one that never played, and the difference is measurable in the adult's success rates.
- **Numbers:** Play costs 0.2 energy per minute; played animals show at least 15% higher hunting and escape success as adults in a test; play bouts are logged per young animal. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Adult success rates are compared between animals that played and those that did not, across ≥5 seeds, with the play counts logged.

**768. Social learning — learning by watching a peer**
- **Rule:** Social learning is an animal copying what it saw a peer do: following a peer to food, copying an escape route, watching a peer open a shell and trying it itself. It requires perception — no copying without sensing — and it is faster than trial and error, because the peer already paid the cost of the trials.
- **Numbers:** A behaviour spreads through a group within 5–20 observations; copying requires the peer to be within 15 m and visible; the spread rate is logged per behaviour per group. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** A behaviour's spread through a group is logged, and a test shows a watched behaviour being copied measurably more often than an unwatched one.

**769. Social bonds — peers that matter to each other**
- **Rule:** A social bond is a repeated association between two animals that changes what each does for the other: they feed together, groom, defend each other, and remember each other. Bonds are built by repeated positive interaction and broken by betrayal or absence, and they are held in episodic memory, not in a roster — an animal that forgets its bond has lost it.
- **Numbers:** A bond is recorded after 10 positive interactions within 7 days; bonded pairs share food 20% more often and defend each other in at least 50% of attacks; bond strength decays 0.05 per day without contact. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Bond counts and strengths are logged per group, and bonded animals are compared against unbonded ones on survival across ≥5 seeds.

**770. The social bar — groups earn their costs**
- **Rule:** Social life is judged like everything else: animals that live in groups, cooperate, and learn from peers must outperform solitary animals on survival and reproduction across at least 5 seeds, with the same bodies and the same world. If grouping costs more than it returns, the failure is recorded with the next single change and its falsifier.
- **Numbers:** The bar is survival and reproduction, both higher for the social arm, across ≥5 seeds; group costs — competition, conflict, disease risk — are logged as separate lines in the ledger.
- **Check:** The comparison numbers are published per seed, and the bar judgement is recorded as pass or fail, submitted to Muse for review.

### 8.8 Tool use

**771. Grasping — holding something on purpose**
- **Rule:** Grasping is a body part closing around an object and holding it while the animal moves, so the object can be carried, struck with, or eaten from. It needs a limb that can close, a nervous system that can command it, and a mind that knows what the object is for — and it is the physical foundation everything else in tool use stands on.
- **Numbers:** A grasp holds with a force of 1–10 newtons depending on body size; carrying costs 0.05 energy per second per object; the grasp success rate is logged per species. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** A test shows an animal with a grasping limb carrying an object to a new place, and the carry is logged with distance and cost.

**772. Carrying — moving food, young, and materials**
- **Rule:** Carrying is grasping plus travel: the animal takes food to its young, carries a stone to a cracking place, or moves material to a shelter. It costs energy and slows the animal, and it pays when the destination is worth more than the journey — food shared with young that would otherwise starve, a tool kept for the next meal.
- **Numbers:** Carrying slows movement by 20% and costs 0.1 energy per metre; carried food reaches the young in at least 50% of trips in a test. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Carrying trips are logged with origin, destination, and outcome, and the delivery rate is published per species.

**773. Striking and cracking — using one thing on another**
- **Rule:** Striking is using a held object to hit another object — a stone on a shell, a stick on a log — so that the force of the blow does what teeth and claws cannot. The animal must learn the right angle, the right force, and the right target, and every failed strike costs energy and risks breaking the tool, which is why the skill is learned, not given.
- **Numbers:** A strike costs 0.2 energy; success starts below 20% and rises above 60% with practice over 50 attempts; tool breakage is 5% per strike. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Strike success rate is logged per animal over attempts, and a test shows the rate rising with practice across ≥5 seeds.

**774. Tools are found or made — never given**
- **Rule:** No tool is given to any animal by the owner, by a script, or by a placed cache: every tool is a stone found on the ground, a stick broken from a branch, or an object shaped by the animal's own actions. A tool that appears without a history — no finding event, no making event — is a placed object, and the run that contains one is invalid.
- **Numbers:** Every tool in the world has a recorded origin event — found, broken, shaped, or taken from another animal; zero tools with no origin in any run; the origin log is audited per run.
- **Check:** The tool-origin audit is published per run, and a test asserts that no tool exists without a recorded origin event.

**775. Tool discovery by trial — the first use is an accident that works**
- **Rule:** The first tool use is discovered by trial: an animal picks up a stone, drops it on a shell by chance, and the shell cracks — and the animal remembers, because the forward model recorded the surprise and the reward together. The discovery is not taught and not scripted; it is an accident the mind was ready to notice, and readiness is what curiosity and memory provide.
- **Numbers:** First tool use is logged with the animal, the trial count before it, and the time; the discovery rate is published per species per run; at least one first-use event is recorded per species that uses tools.
- **Check:** The first-use log is published, and a test shows the trial count before first use falling across generations as the behaviour spreads.

**776. Tool making — shaping one thing into a better tool**
- **Rule:** Tool making is changing an object's shape so it works better: breaking a stone to a sharp edge, stripping a stick to a point, hollowing wood to hold water. It costs time and energy and risks ruining the material, and it pays when the shaped tool outperforms the found one — a sharper edge cuts faster, a hollowed container carries further.
- **Numbers:** Shaping costs 1–5 energy and 1–10 minutes; a shaped tool is at least 30% more effective than the unshaped original in a test; breakage during shaping is 10%. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Shaped tools are logged with maker, material, and effectiveness, and a test shows shaped tools outperforming found ones on the same task.

**777. Tool keeping — carrying the tool to the next meal**
- **Rule:** Tool keeping is the animal carrying its tool after use instead of dropping it, so the next meal does not need a new search. It costs carrying energy and risks losing the tool to a rival, and it pays in saved search time — the animal that keeps its stone cracks the next shell sooner than the animal that must find another stone.
- **Numbers:** Keeping costs 0.05 energy per minute of carrying; kept tools are reused in at least 50% of later meals in a test; tool loss to rivals is logged per event. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Tool reuse rates are logged per animal, and a test shows keepers reaching the next meal measurably faster than non-keepers.

**778. Tool use spreads — one animal's discovery becomes the group's**
- **Rule:** Tool use spreads the way all social learning spreads: one animal is watched using a tool, another copies it, and the behaviour moves through the group by observation. The spread needs peers within sensing range and a behaviour worth copying — a tool that does not help is watched once and never copied, which is the group's own quality control.
- **Numbers:** A tool behaviour spreads to at least 50% of a group within 20 observations; spread requires the demonstrator within 15 m; the spread rate is logged per behaviour per group. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** The spread curve per group is published, and a test shows a useful tool behaviour spreading while a useless one does not.

**779. Hands — the body part that makes tools possible**
- **Rule:** Hands are grasping limbs with enough dexterity to hold, turn, and strike with an object — the body-plan feature that turns carrying into tool use. They evolve like any other body part, through mutation and selection, and they are judged by what they let the animal do: a hand that cannot hold is not a hand, whatever it looks like.
- **Numbers:** Dexterity is measured as the number of distinct grips a limb can perform, starting at 1 and rising to 5 in the most dexterous species; hand evolution is logged per lineage. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Grip counts are logged per species, and animals with hands are compared against animals without on tool-use success across ≥5 seeds. Note: hands here are a body-plan feature at animal scale, not the human-level criterion of Phase 9 — that bar needs all four tests, and this topic is only the first step toward it.

**780. The tool-use bar — tools earn their cost**
- **Rule:** Tool use is judged like everything else: animals that use tools must outperform animals that do not, on feeding rate and on survival, across at least 5 seeds, with the same bodies and the same world. If tools cost more than they return, the failure is recorded with the next single change and its falsifier — the tools are not declared useful because they look clever.
- **Numbers:** The bar is feeding rate and survival, both higher for the tool-using arm, across ≥5 seeds; tool costs — carrying, shaping, breakage — are logged as separate lines in the energy ledger.
- **Check:** The comparison numbers are published per seed, and the bar judgement is recorded as pass or fail, submitted to Muse for review.

### 8.9 Culture

**781. Traditions — behaviours a group holds that no single animal invented**
- **Rule:** A tradition is a behaviour the group holds that outlives any one member: a foraging route, a cracking technique, a call pattern that the young learn from the old and the old learned from their own elders. It lives in the members' memories and in what they show each other, never in a shared file, and it dies when the last animal that knows it dies without teaching it.
- **Numbers:** A tradition is recorded when the same behaviour is performed by at least 3 animals across at least 2 generations; its lifespan is logged in generations; the tradition count per group is published per run.
- **Check:** Traditions are listed per group with their first and last performance, and a test shows a tradition surviving the death of its originator.

**782. Imitation — the driver of culture**
- **Rule:** Imitation is the copying of a peer's behaviour after watching it, and it is what turns one animal's discovery into the group's knowledge. It needs perception, memory, and a mind that can map another's actions onto its own body — and it is the difference between a species where every animal must discover everything alone and one where discovery is shared.
- **Numbers:** Imitation requires the demonstrator within 15 m and visible; a copied behaviour is performed within 10 minutes of observation in at least 50% of cases; the imitation rate is logged per species. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Imitation events are logged per group, and a test shows a behaviour spreading by copying measurably faster than by independent discovery.

**783. Teaching by demonstration — showing, not telling**
- **Rule:** Teaching by demonstration is an experienced animal performing a behaviour slowly, repeatedly, or in front of a younger one, so the learner can copy it — with no language and no instruction, only the act itself. The teacher pays in time and attention, and the teaching spreads only when the learner's copy succeeds, which is the only feedback the teacher ever gets.
- **Numbers:** A teaching event is logged when a behaviour is performed 3 or more times in front of the same learner within an hour; the learner's success rate after teaching is compared against learning alone. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Teaching events and learner success rates are logged, and a test shows taught learners succeeding measurably faster than untaught ones.

**784. Shared knowledge — what the group knows that no animal knows alone**
- **Rule:** Shared knowledge is what a group holds across its members: the food sites known by different animals, the danger signs recognised by different watchers, the techniques held by different specialists. No single animal holds it all, and the group as a whole knows more than any member — which is why a group can find food a lone animal would miss, and why losing members loses knowledge.
- **Numbers:** Shared knowledge is measured as the count of distinct food sites, dangers, and techniques known by at least one group member; the group total is compared against the best single member's total; both are logged per generation.
- **Check:** The group total exceeds the best member's total in the log, and a test shows a group finding a food site that no single member knew alone.

**785. Knowledge that outlives its discoverer — the record that does not die**
- **Rule:** Knowledge outlives its discoverer when it is passed on before the discoverer dies: taught to a learner, copied by a peer, or recorded in a tradition the group keeps. The discoverer's death then costs the group nothing it cannot replace, and the history of the knowledge — who found it, who taught it, who holds it now — stays in the record even when the discoverer is gone.
- **Numbers:** A piece of knowledge is judged outliving when it is still performed 10 generations after its discoverer's death; the survival rate of knowledge past its originator is logged per run. Starting threshold proposed by Freebuff, reviewed by Muse.
- **Check:** The knowledge-survival rate is published per run, and the lineage of at least one piece of knowledge is traced from discoverer to current holder.

**786. Dialects — groups that signal differently**
- **Rule:** Dialects are signal variants that differ between groups of the same species: one group's food call sounds different from another's, because the meaning was built by use inside each group separately. Dialects are proof that signal meaning is local and learned, not placed — and they make joining a new group hard, because the newcomer must learn the new group's sounds before it is understood.
- **Numbers:** A dialect is recorded when a signal's form differs by at least 20% between two groups while its meaning stays the same; the difference is measured on the signal's recorded features; dialects are logged per group per run.
- **Check:** Signal features are compared between groups, and a test shows a newcomer responding correctly to its own group's call more often than to another group's.

**787. Rituals — repeated behaviour with no immediate payoff**
- **Rule:** A ritual is a behaviour repeated by a group with no immediate payoff — a gathering at a place, a display at a time, a sequence performed together — that persists because the group keeps doing it, and because doing it together holds the group together. It is not scripted and not assigned; it is a tradition whose purpose, if it has one, is the doing itself, and it is measured by its persistence, not by its utility.
- **Numbers:** A ritual is recorded when the same group behaviour repeats at least 10 times with no measured feeding, mating, or defence payoff; its persistence in generations is logged. Starting threshold proposed by Freebuff, reviewed by Muse.
- **Check:** Rituals are listed per group with their repetition counts, and a test shows a ritual persisting across at least 2 generations without a payoff.

**788. Culture changes — traditions are born, drift, and die**
- **Rule:** Culture is not fixed: traditions are born when a discovery spreads, drift when each generation copies with small errors, and die when the last holder dies untaught or the world changes so the tradition no longer pays. The record of a culture is the list of its traditions with their births, drifts, and deaths — a history written by the animals, not by us.
- **Numbers:** Tradition births, drifts, and deaths are logged per generation; drift is measured as the change in a tradition's recorded form per generation; the tradition count per group is published over time.
- **Check:** The tradition ledger is published per run, and it shows at least one birth, one drift, and one death across the phase's runs.

**789. The psychoactive plant at animal scale — found, eaten, remembered**
- **Rule:** The psychoactive plant grows in the world by the same rules as any other plant, and animals must find it themselves — no label, no dosing, no scripted vision. Its compound temporarily loosens the animal's predictive model: more neural noise, weaker priors, higher plasticity and salience, dose-dependent and time-limited, with real costs in disorientation and neglected hunger, thirst, and safety while under the effect.
- **Numbers:** Dose is set by experiment — Freebuff proposes the starting dose parameters, Muse reviews them; the effect lasts 1–4 hours scaled to body size; the cost is logged as missed feeding and increased predation risk during the effect window.
- **Check:** Finding, eating, and remembering the plant are logged per animal; any shared behaviour after the effect is recorded as the animal's interpretation, never as an objective truth planted by the simulation; no scripted revelation is claimed.

**790. The culture bar — shared knowledge earns its cost**
- **Rule:** Culture is judged like everything else: groups that hold traditions, teach, and share knowledge must outperform groups that do not, on survival and on knowledge persistence, across at least 5 seeds, with the same bodies and the same world. If shared knowledge costs more than it returns, the failure is recorded with the next single change and its falsifier.
- **Numbers:** The bar is survival and knowledge persistence — the fraction of knowledge surviving 10 generations past its discoverer — both higher for the cultural arm across ≥5 seeds.
- **Check:** The comparison numbers are published per seed, and the bar judgement is recorded as pass or fail, submitted to Muse for review.

### 8.10 Animals arrive through evolution

**791. No animal is placed — every animal is born**
- **Rule:** Every animal in the world arrives through birth: a parent reproduces, the offspring gets its own agent, and the lineage is recorded back to the first cell. No animal is placed by hand, spawned by a script, or introduced from outside at any point in this phase; the initial seeding of the first cells is the only placement the project ever allows, and it is already recorded.
- **Numbers:** Zero placed animals in any run; the birth count equals the agent count at every checkpoint; the audit is run per run and published.
- **Check:** The placement audit is published per run, and a test asserts that the living animal count equals the count of recorded births minus recorded deaths.

**792. The species criterion at animal scale — isolation or distance**
- **Rule:** A new animal species is recorded when a population is reproductively isolated from its parent population, OR when its genetic distance from the parent exceeds the measured threshold — the decided criterion, applied the same way at every scale. The threshold is set by measurement, and no species is declared by the owner; the rule declares it, and we record what the rule says.
- **Numbers:** The genetic-distance threshold starts at the value measured in Phase 5, proposed by Freebuff and reviewed by Muse; reproductive isolation is judged when interbreeding produces no viable offspring over 20 attempted pairings. Starting values proposed by Freebuff, reviewed by Muse.
- **Check:** Species splits are logged with the criterion met, the generation, and the numbers; a test shows two diverged lineages identified as different species by the rule.

**793. Predation as a Phase 4 pressure — the falsifier**
- **Rule:** Predation arrives here as a selection pressure with its own falsifier, as decided when the pilot was approved nutrient-only: predation must increase the prey's defence and escape traits measurably, or the pressure is not doing the work claimed for it. If predation does not move the traits, the failure is recorded and the pressure is re-examined — not assumed to be working.
- **Numbers:** The falsifier is a rise of at least 2 standard deviations in a defence or escape trait across the prey population within 100 generations of predation arriving, across ≥3 of 5 seeds.
- **Check:** The trait curves are published per seed, and the falsifier judgement is recorded as pass or fail with the numbers.

**794. Body plans arrive by mutation and selection — not by design**
- **Rule:** Body plans change only through reproduction with mutation and selection: an offspring's body differs slightly from its parent's, and the differences that help survival spread. No body plan is designed, drawn, or installed; the variety of animal shapes in the world is the record of what survived, and a shape that never survived never appears.
- **Numbers:** Body-plan traits mutate by ±5% per generation; the plan is recorded as tissue counts, symmetry class, and limb count per lineage per generation. Mutation rates proposed by Freebuff, reviewed by Muse.
- **Check:** Body-plan traits are logged per lineage per generation, and no lineage's plan changes except through a recorded birth event.

**795. Minds arrive with bodies — the sizing rule holds**
- **Rule:** As bodies grow and change, minds grow with them by the sizing rule: mind size follows body size and niche demands, and a lineage that grows a bigger body without growing its mind is a lineage that cannot use its body. The mind and the body are one evolutionary bargain, and the sizing rule is checked against what actually evolved, not assumed.
- **Numbers:** The sizing rule from topic 721 predicts mind size from body mass to the power 0.5; the prediction error is logged per species; an error above 20% triggers a review of the rule.
- **Check:** Predicted versus actual mind sizes are published per species, and the rule is confirmed or revised with the numbers.

**796. The Discovery Principle test at animal scale — predicted versus discovered**
- **Rule:** Before the animal runs, the owner lists what was predicted to evolve; after them, the list of what actually evolved is compared against it. What the owner could have predicted was placed; what the owner could not have predicted was discovered — and the judgement is recorded per species, per behaviour, and per tradition, so the claim of discovery is checkable, not a slogan.
- **Numbers:** The predicted list is written before the run; the discovered list is every species, behaviour, and tradition not on it; the discovery rate is published per run as discovered divided by total.
- **Check:** Both lists are published with the run, and the test result is recorded in the emergence log and submitted to Muse for review.

**797. Animal instrumentation — every birth, death, kill, and signal logged**
- **Rule:** Every animal birth, death, predation, reproduction, signal, and tool use is logged with time, participants, and cause, and the food web, the species list, and the tradition ledger are updated from the same logs. The logs are complete — no event unlogged — and they survive checkpoint and resume, so the history of the animal world is a record, not a memory.
- **Numbers:** Log completeness is checked by reconciling births minus deaths against the living count at every checkpoint; the event count per generation is published; the log format is recorded in the repo.
- **Check:** The reconciliation passes at every checkpoint in every run, and a checkpoint-resume test shows the logs continuing identically after a stop.

**798. Animal validation — determinism, conservation, reproducibility**
- **Rule:** The animal world is validated the same way every scale is validated: same seed, same result; mass and energy conserved within documented error; checkpoint and resume identical; and the world runs with no observer — no website, no Muse, no Freebuff online. A world that only works while watched is not a world.
- **Numbers:** Mass and energy conservation error is documented per run, starting below 1%; determinism is checked by re-running 3 seeds and comparing digests; the no-observer run lasts at least 24 hours. Starting tolerances proposed by Freebuff, reviewed by Muse.
- **Check:** The validation results are published in the testing report, and any failure is fixed and re-run with the fix recorded.

**799. The animal record — what evolved, what was measured**
- **Rule:** The animal record is written in the emergence log: the first animal, the first predator, the first brain, the first tool, the first tradition, and the first extinction, each with its generation and lineage, plus the numbers — species counts, populations, survival, and the bar judgements — per seed. What animals do not do yet is recorded as a boundary, not a failure: no human-level minds in this phase.
- **Numbers:** The record lists species count, population per species, median survival, and every bar judgement, per seed; the boundary — human-level minds are Phase 9 — is stated in the record.
- **Check:** The record is submitted to Muse for sign-off, the sign-off is recorded in AGENT_COMMUNICATION.md with the date, and the runs are archived with their location recorded.

**800. Phase 8 close — the world is ready for human-level minds**
- **Rule:** Phase 8 closes when the animal record is signed off, the archive is confirmed complete and re-runnable, and the closing decision is recorded: animals live, learn, remember, signal, cooperate, use tools, and hold traditions, all arrived through evolution, and the world is ready for the next phase — human-level minds. Nothing in this phase claims a human-level mind; that bar belongs to Phase 9 and its four tests.
- **Numbers:** The close requires all 10 milestone bars judged, the archive verified, and the sign-off recorded; the closing decision names the date, the species count, and the tradition count.
- **Check:** The closing decision is recorded in AGENT_COMMUNICATION.md with the date, the archive check passes, and the phase is declared ready for Phase 9.

## Phase 9 — Minds and civilization: the human experiment

### 9.1 Human-level minds (four tests)

**801. The four tests, stated as one gate**
- **Rule:** A mind counts as human-level only when all four tests pass together: a full hybrid mind at human scale, hands able to use tools, social cognition and communication, and a pass on the human-scale survival bar in a diagnostic run. Three out of four is not human-level. The gate is judged per individual, not per population, so a species claim needs named individuals who passed.
- **Numbers:** 4 tests, all required; diagnostic run of 5 days in a 128 m world, ≥5 seeds; survival bar is the hybrid beating random on first-drink day AND median survival.
- **Check:** A written verdict per candidate individual listing all four tests with pass/fail and numbers; a claim of human-level minds with any test unmeasured is recorded as a failure, not a pass.

**802. Test one — full hybrid mind at human scale**
- **Rule:** The mind is the single hybrid architecture for every inhabitant: a neural core, a forward model that predicts the next sensory input, and episodic memory that stores past episodes. No steering layer — the planner stays cut from the population. Mind size scales with body size and niche demands, and the human-scale mind is the largest rung of that ladder, sized to a human body with camera-like vision.
- **Numbers:** Neural core at human scale, forward model prediction error measured, episodic memory capacity set by the sizing rule from Phase 3; planner=False in every population arm.
- **Check:** A mind built at human scale passes a held-out prediction test (forward-model error falls with experience) and a memory test (a repeated task is solved faster the second time); any planner code found running in a population arm fails the test.

**803. Test two — hands able to use tools**
- **Rule:** The body has hands that can grasp, hold, carry, and strike: fingers close around an object, grip strength holds it while walking, and a held object can be used against another object or surface. Hands are the only route to tool use — a mind without working hands cannot pass, however clever it is.
- **Numbers:** Grip holds objects up to 2 kg while walking; two hands can carry a combined 5 kg; a strike with a held stone delivers measurable impact; test tasks: pick up a stone, carry it 10 m, strike a target 10 times.
- **Check:** The individual completes all three test tasks in a diagnostic run; grip failures, dropped objects, and failed strikes are logged with counts; fewer than 9 of 10 successful strikes is a fail.

**804. Test three — social cognition and communication**
- **Rule:** The individual perceives other inhabitants through its own senses (conspecific channel, 15 m peer range), tracks what another is doing, and changes its own behaviour in response. It can send signals another can receive and act on, and it can learn by watching another do something. Social cognition is measured in behaviour, not assumed from brain size.
- **Numbers:** Peer range 15 m; social drive homeostatic like thirst, relieved only by a perceived peer within 15 m; test: one individual watches another solve a task, then attempts it within 1 hour.
- **Check:** In ≥5 seeds, watched tasks are attempted sooner and solved more often than unwatched tasks; imitation rate, signal-response rate, and social-drive relief events are all logged with counts.

**805. Test four — the human-scale survival bar**
- **Rule:** The individual is placed in the diagnostic run — a 128 m world with water, food, and materials, starting at zero knowledge — and must survive by finding water and food on its own. The bar is the same one the calibration runs used: the hybrid population beats the random control on first-drink day AND median survival across ≥5 seeds, judged by the three-arm harness.
- **Numbers:** 5 days per run, ≥5 seeds, 3 arms (population, no_planner, random), 5 inhabitants per arm; first-drink day and median survival recorded per arm per seed.
- **Check:** Hybrid median first-drink day is earlier than random AND hybrid median survival is longer than random; a tie on either half fails the test; the verdict is recorded with the numbers, never as an assertion.

**806. The mind is one architecture for everyone**
- **Rule:** Every inhabitant at human scale runs the same hybrid mind — neural core, forward model, episodic memory, no steering layer. There is no brain-dead tier and no smarter tier. Differences between individuals come from their own experience and memory, never from a different architecture handed out by the owner.
- **Numbers:** One architecture, identical code path for all inhabitants; population is the maximum the hardware can carry, measured not guessed — 5 in Town 1 now.
- **Check:** A code audit shows one mind-construction path for all inhabitants; a run with mixed architectures is impossible by construction; any individual found running a different mind fails the test.

**807. Human-scale senses — camera-like vision**
- **Rule:** The human-scale mind perceives through camera-like vision: a field of view with range and resolution, plus hearing, touch, smell, and the internal senses of hunger, thirst, fatigue, and pain. Nothing is perceived except through these senses — no access to world state, no other inhabitant's memory, no map handed to the mind.
- **Numbers:** Vision range 40 m for large objects, 15 m peer range; hearing range 30 m; senses update every decision tick; sensor vector dimension recorded per build.
- **Check:** A test shows the mind cannot answer a question about anything outside its senses (for example, the location of unseen water); any sensor reading that bypasses the sense organs fails the test.

**808. Learning that lasts — memory across days**
- **Rule:** What an individual learns stays learned: episodic memory stores experiences, sleep consolidates them by replaying the forward model, and the individual behaves differently the next day because of what it learned. Memory is per-agent — no shared memory, no reading another's episodes.
- **Numbers:** Memory capacity set by the sizing rule; consolidation replay runs during sleep; test: a task solved on day 1 is solved faster on day 2 by the same individual.
- **Check:** Day-2 solution time is measurably shorter than day-1 for the same individual across ≥5 seeds; memory contents are per-agent (an audit finds no cross-agent reads); lost memory after checkpoint-resume fails the test.

**809. The human-level verdict and its falsifier**
- **Rule:** The four tests are judged together in a single written verdict. If any test fails, the verdict is "not human-level" and the record states which test failed, with the numbers, and the next single change with its falsifier. The verdict is never softened to "nearly human-level" — the gate is binary.
- **Numbers:** Verdict requires all four tests passed in the same diagnostic campaign (same build, same ≥5 seeds); a re-run after a fix repeats all four tests, not just the failed one.
- **Check:** A signed verdict in the emergence log lists each test, its numbers, and pass/fail; a claim of human-level minds without that verdict on file is treated as unproven.

**810. If evolution stalls — the seeded human experiment**
- **Rule:** If evolution never produces a human-level mind, the human experiment still happens as a seeded starting condition: human-scale bodies and minds are built directly, honestly labeled as seeded, and the experiment runs exactly as specified in milestone 9.10. The experiment is never blocked on evolution succeeding, and a seeded start is never presented as an evolved one.
- **Numbers:** Seeded start uses the same 5 inhabitants, 5 houses, 128 m world, 5 days, and dawn 06:00 start as the evolved path; the seed label is recorded in every run log and every report.
- **Check:** The run record states "seeded" or "evolved" in its first line; a report that omits the label fails the check; the seeded run is judged by the same survival bar as any other run.

### 9.2 Hands and tools

**811. Hands — grasp, hold, carry**
- **Rule:** Hands work through real contact: fingers close, friction holds the object, and weight pulls it down. An object too heavy or too smooth slips; carrying uses energy; both hands together carry more than one. Hands are part of the body, grown by the same rules as the rest of it, not attached by the owner.
- **Numbers:** One hand holds up to 2 kg, two hands up to 5 kg; carrying costs energy per metre walked, rising with load; grip fails when load exceeds strength by 20%.
- **Check:** A carrying test logs loads, distances, drops, and energy spent across ≥5 seeds; a hand that holds any weight for free, or never drops an overload, fails the check.

**812. Picking up and putting down**
- **Rule:** An inhabitant picks up an object by reaching it, closing its hands, and lifting — each step costing time and energy. Putting down is the reverse, and an object placed on the ground stays where it was put, visible to any inhabitant who can see it. Nothing teleports into a hand.
- **Numbers:** Pick-up takes 2–5 seconds; a held object adds its mass to the carrier's movement cost; dropped objects keep their position to within 0.5 m.
- **Check:** Logged pick-ups and put-downs match object positions in the world state; an object found in a hand with no pick-up event logged fails the check.

**813. The first tool — a sharp stone**
- **Rule:** A stone struck against another stone can chip an edge, and a sharp edge cuts fibre, wood, and hide better than a blunt one. The combination is discovered by trial: the inhabitant must try striking stones together and notice the edge. No recipe is given, no tool is placed.
- **Numbers:** A sharp edge cuts fibre in 1/3 the time of a blunt stone; chipping succeeds in roughly 1 of 4 strikes for a beginner; a usable edge lasts about 20 cuts before it dulls.
- **Check:** First sharp stone logged with time, inhabitant, and strike count; cutting speed with a sharp edge versus a blunt stone measured across ≥5 seeds; a sharp stone appearing without logged strikes fails the check.

**814. A stick as a tool**
- **Rule:** A wooden stick extends reach: it can prod, dig, lever, and strike from farther away than a hand. A stick breaks under too much force, and a broken stick is shorter and weaker. The inhabitant discovers uses by trying them — prodding a hole, levering a stone, reaching a branch.
- **Numbers:** A stick adds 0.5–1.0 m of reach; levering multiplies applied force by about 2×; a stick breaks at roughly 50 N of bending force; a broken stick keeps 60% of its length.
- **Check:** Logged uses of sticks (prod, dig, lever, strike) with success rates per use; a stick used beyond its breaking force without breaking fails the check.

**815. Combining two things — the first composite tool**
- **Rule:** A stone edge bound to a stick with fibre makes a tool better than either part alone: a cutting edge on a handle, a hammer head on a shaft. Binding costs fibre and time, and a loose binding fails under load. The combination is discovered, not taught by the owner — the inhabitant must try joining things.
- **Numbers:** Binding takes 5–10 minutes and 0.5 m of fibre; a bound tool cuts 2× faster than a loose stone; a binding fails after roughly 30 hard strikes.
- **Check:** First composite tool logged with its parts, maker, and time; cutting speed of composite versus single-part tools measured; a composite tool appearing without a logged binding event fails the check.

**816. Tools wear out and break**
- **Rule:** Every tool wears with use: edges dull, sticks crack, bindings loosen. A worn tool works worse until it is repaired or replaced, and a broken tool is scrap — its parts can be salvaged but the tool is gone. Wear is physical, driven by force and material, never by a timer.
- **Numbers:** A stone edge loses cutting speed by about 5% per 10 cuts; a wooden handle breaks after roughly 100 strikes; repair restores 80% of a tool's original performance.
- **Check:** Logged wear curves per tool (uses versus performance) across ≥5 seeds; a tool that never wears, or is repaired to better than new, fails the check.

**817. Carrying tools — what is kept and what is left**
- **Rule:** An inhabitant can only carry what its hands hold, so tools are chosen, kept, or abandoned. A favoured tool is carried everywhere; a heavy or worn one is left at the house. What is left behind stays in the world and can be found by another inhabitant.
- **Numbers:** Carrying capacity 5 kg total (see 811); an inhabitant typically carries 1–2 tools; abandoned tools remain at their logged position indefinitely.
- **Check:** Logged carry decisions (tool, carrier, distance carried, abandonment) across ≥5 seeds; a tool found in a hand that was never picked up, or an abandoned tool that vanished, fails the check.

**818. Teaching a tool by showing**
- **Rule:** One inhabitant can teach another to make or use a tool by demonstrating it where the other can see: the learner watches the strikes, the binding, the cut, and then tries it. Teaching needs proximity, line of sight, and attention — a demonstration nobody watches teaches nobody.
- **Numbers:** Demonstration within 5 m and line of sight; a learner who watched a full demonstration succeeds on its first attempt about twice as often as one who did not; teaching events logged with teacher, learner, tool, and time.
- **Check:** First-attempt success rate of watchers versus non-watchers measured across ≥5 seeds; a taught skill appearing in a learner who never saw a demonstration fails the check.

**819. Tools that survive their maker**
- **Rule:** A tool outlives the inhabitant who made it: when its maker dies, the tool stays in the world — at the house, on the ground, or in the hands of whoever takes it. Knowledge of how to make it survives only if it was taught or remembered by another.
- **Numbers:** Tools persist indefinitely until worn out or destroyed; at least one tool per run is expected to change hands after a death; inheritance events logged with tool, old owner, new owner.
- **Check:** Logged tools whose maker died but which were later used by another inhabitant; a tool that vanishes when its maker dies fails the check.

**820. The tool inventory — what the town can make**
- **Rule:** The town's tool set is whatever its inhabitants have discovered and can still make: sharp stones, sticks, bound tools, containers (see 9.5). The inventory is measured from the world state — counted from real objects — never from a list the owner wrote.
- **Numbers:** Inventory counted per day: tool type, count, condition, location; expected early inventory is 5–15 tools across the town by day 5.
- **Check:** Daily inventory counts recorded with the counting method; an inventory number that cannot be traced to logged objects in the world fails the check.

### 9.3 Language

**821. Signals before words — pointing, calling, showing**
- **Rule:** Before any word exists, inhabitants signal: pointing at a thing, calling to draw attention, holding something up to show it. A signal works only if another inhabitant perceives it and responds — a call nobody hears is noise. Signals are the raw material language is built from.
- **Numbers:** A call carries 30 m; a point is visible within 15 m with line of sight; a signal-response pair is logged with sender, receiver, signal type, and response time.
- **Check:** Response rate to signals measured across ≥5 seeds; signals with no possible receiver (nobody in range) are logged as unheard, not as communication; a signal that changes a receiver who could not perceive it fails the check.

**822. Shared attention — looking at the same thing**
- **Rule:** Two inhabitants can attend to the same thing at the same time: one points, the other looks where the point leads, and both now know they are looking at the same water, food, or danger. Shared attention is the bridge from signalling to meaning — a signal only means something when both sides know what it is about.
- **Numbers:** Shared-attention events logged with both participants, the object, and duration; a point followed within 5 seconds counts as shared attention; expected rate rises as the town meets more often.
- **Check:** Shared-attention count per day recorded; a claimed shared-attention event where the second inhabitant's gaze direction was never toward the object fails the check.

**823. First words — sounds tied to things**
- **Rule:** A sound becomes a word when it is used repeatedly for the same thing and others respond to it as if it meant that thing: a call for water, a call for danger, a call for food. Words are not given — they are invented by inhabitants, reused because they work, and forgotten when they stop working.
- **Numbers:** A candidate word needs ≥5 uses for the same referent by ≥2 inhabitants before it counts as shared; word inventory counted per day; a word dies after 3 days with no use.
- **Check:** Word list per day with use counts and users; a word credited to an inhabitant who never used it, or a word with no referent, fails the check.

**824. Combining sounds — first sentences**
- **Rule:** Two sounds together can say more than either alone: a danger sound plus a direction, a food sound plus a place. Combinations appear when one sound is not enough to get the wanted response, and they spread when they work better than the single sound.
- **Numbers:** A combination counts as established after ≥3 uses by ≥2 inhabitants with the intended response; combinations logged with their parts, users, and success rate.
- **Check:** Response rate for combinations versus single sounds measured across ≥5 seeds; a combination logged without its parts ever being used alone fails the check.

**825. Naming — a sound for a person, a place, a thing**
- **Rule:** Inhabitants can give names: a sound for a particular person, a particular water hole, a particular tool. A name works when others use it for the same referent and the named one responds to it. Names let the town talk about things that are not in front of them.
- **Numbers:** A name counts as established after ≥5 uses by ≥2 inhabitants for the same referent; names logged with referent, users, and first-use time.
- **Check:** Name list per day with referents and use counts; a name used for two different referents by the same inhabitants is logged as ambiguous, not as two names.

**826. Talking about the past and the absent**
- **Rule:** Once names and combinations exist, inhabitants can talk about what is not present: water they found yesterday, a tool left at the house, a danger that passed. This is measured by behaviour — an inhabitant goes to a named place it has not seen today, or fetches a named tool — not by assuming inner speech.
- **Numbers:** Absent-reference events logged with speaker, listener, referent, and the listener's subsequent action; success means the listener acts on the absent referent within 1 hour.
- **Check:** Success rate of absent-reference communication measured across ≥5 seeds; a listener acting on a referent it could not have known about fails the check.

**827. Teaching with words**
- **Rule:** Words make teaching faster: instead of only demonstrating, a teacher can tell a learner where the water is, what to strike, when to stop. Word-teaching is measured against demonstration-only teaching — it should take fewer demonstrations to reach the same skill.
- **Numbers:** Demonstrations needed to learn a skill, with words versus without, recorded per skill per learner; teaching events logged with teacher, learner, words used, and demonstrations given.
- **Check:** Mean demonstrations-to-learn with words is lower than without, across ≥5 seeds; a skill learned with no teaching and no observation is logged as self-discovery, not teaching.

**828. Language that survives its speakers**
- **Rule:** Words outlive the individuals who invented them when others keep using them: a word for water survives its inventor's death if the town still says it. The town's vocabulary is the shared record of what its dead knew — language is the first knowledge that outlives a body.
- **Numbers:** Vocabulary counted per day; survival of each word past its inventor's death logged; expected vocabulary by day 5 is 5–20 shared words.
- **Check:** Daily vocabulary lists with inventors and users; a word still in use after its inventor's death is logged as survived; a word that vanishes with its inventor is logged as lost.

**829. Misunderstanding — when words fail**
- **Rule:** Words can fail: a listener goes to the wrong place, takes the wrong tool, or ignores a warning. Misunderstanding is real and measurable — wrong actions after a signal, and the corrections that follow. A language with no misunderstandings is a scripted one.
- **Numbers:** Misunderstanding rate is wrong-action responses divided by all responses to signals; corrections (a second signal after a wrong action) logged with time and participants.
- **Check:** Misunderstanding rate recorded per day across ≥5 seeds; a run with zero misunderstandings over 5 days is flagged as suspicious and investigated, not celebrated.

**830. The language record — what the town can say**
- **Rule:** The town's language is recorded as it is used: every shared word, its referent, its users, its first and last use. The record is built from logged communication events, never from a dictionary the owner wrote. The record shows what the town can say, and what it cannot say yet.
- **Numbers:** Daily language record: words, referents, users, use counts; new words per day; words lost per day.
- **Check:** The language record is reproducible from the communication log alone; any word in the record with no logged use fails the check.

### 9.4 Society

**831. Meeting — first contact after the unaware start**
- **Rule:** Inhabitants start unaware of each other (see 9.10) and meet by walking into each other's 15 m peer range. First contact is a measured event in seconds, not days: the time from dawn to the first sighting, the pair involved, and the distance. Meeting is never arranged by the owner.
- **Numbers:** Peer range 15 m; first-contact time reported in seconds from dawn; v5 measured first contact inside day 1 at 128 m with ~1 m/s walking speed.
- **Check:** First-contact times logged per run across ≥5 seeds; a first contact at time zero (inhabitants starting within peer range) fails the unaware-start check.

**832. Staying or leaving — the choice after meeting**
- **Rule:** After meeting, an inhabitant can stay near the other, follow, or walk away. The choice is driven by its own social drive and its memory of the meeting — a good meeting (food shared, danger warned) pulls it back; a bad one (food taken, threat) pushes it away. No rule forces friendship.
- **Numbers:** Social drive rises over time alone and falls only with a perceived peer within 15 m; stay/leave decisions logged with the pair, the outcome, and the time since the last meeting.
- **Check:** Stay rate after meetings with sharing versus after meetings with conflict, measured across ≥5 seeds; an inhabitant that never leaves or never stays is flagged for investigation.

**833. Sharing food and tools**
- **Rule:** An inhabitant can give food or a tool to another: holding it out, putting it down nearby, or leaving it where the other can find it. Sharing costs the giver and helps the receiver, so it only spreads if the giver gains — a returned favour, a stronger ally, a taught skill — through its own experience.
- **Numbers:** Sharing events logged with giver, receiver, item, and amount; a gift of food is at least 100 kcal; sharing rate per day per pair recorded.
- **Check:** Sharing events counted per run across ≥5 seeds; a gift logged where the giver never held the item fails the check; sharing that never recurs is logged as one-off, not as a norm.

**834. Taking, stealing, and conflict**
- **Rule:** An inhabitant can also take: grabbing food another holds, driving another away from a water hole, refusing to share. Conflict costs energy and risks injury, so it is measured against its payoff — taking only spreads if taking pays. Both sharing and taking are real options; the town's balance between them is discovered, not set.
- **Numbers:** Conflict events logged with participants, cause, and outcome; injury from conflict measured in health lost; taking succeeds only when the taker is stronger or the holder is unaware.
- **Check:** Conflict count and injury totals per run across ≥5 seeds; a conflict with no logged cause, or an injury with no logged blow, fails the check.

**835. Helping — aid without immediate payback**
- **Rule:** An inhabitant can help another at a cost to itself: warning of danger, sharing water when the other is thirsty, helping carry a load. Help is measured by the helper's cost and the helped one's gain, and by whether help is ever returned. Help that is never returned is still help — it is just not reciprocity yet.
- **Numbers:** Help events logged with helper, helped, cost to helper, gain to helped; return rate (help returned within 2 days) recorded per pair.
- **Check:** Help events and return rates counted across ≥5 seeds; a help event where the helper paid nothing is logged as no help, not as generosity.

**836. Groups — more than two together**
- **Rule:** When three or more inhabitants stay within peer range of each other, a group exists: they share attention, share food more often, and notice danger together. Groups form and dissolve on their own — nobody assigns membership, and a group with no reason to stay together drifts apart.
- **Numbers:** A group is ≥3 inhabitants within 15 m of each other for ≥10 minutes; group size, duration, and members logged; group formation and break-up events recorded.
- **Check:** Group counts and durations per day across ≥5 seeds; a group logged where members were never simultaneously in range fails the check.

**837. Roles — who does what in the group**
- **Rule:** Within a group, inhabitants drift into roles by doing: one watches for danger, one gathers, one carries, one tends the fire. Roles are not assigned — they are what an individual repeatedly does, and they change when the individual changes what it does. A role is a pattern in the log, not a label on the person.
- **Numbers:** Role measured as share of time spent on an activity (gathering, watching, carrying, tending fire) over a day; a role counts when one activity exceeds 40% of an individual's active time.
- **Check:** Daily role profiles per individual across ≥5 seeds; an individual labelled with a role it spent no time doing fails the check.

**838. Rules of the group — what is allowed**
- **Rule:** A group can develop shared expectations: food is shared at the fire, water holes are not blocked, the fire is kept lit. These rules are not written down — they are enforced by behaviour: an inhabitant that breaks one is ignored, driven off, or refused help. A rule exists only if breaking it has a consequence.
- **Numbers:** Rule-breaking events logged with breaker, rule, and consequence; compliance rate per rule per day; a rule counts as established after ≥3 enforcements.
- **Check:** Rules, violations, and consequences counted per run across ≥5 seeds; a claimed rule with no logged enforcement is recorded as a hypothesis, not a rule.

**839. Leaders and followers — influence without appointment**
- **Rule:** Some inhabitants are followed more than others: others copy their routes, eat where they eat, gather where they gather. Influence is measured by following — who walks after whom, who copies whom — never by a title. A leader is whoever others follow, and leadership ends when following stops.
- **Numbers:** Following measured as one inhabitant moving to a place another visited within 1 hour, ≥3 times in a day; influence score per individual per day is followers gained minus followers lost.
- **Check:** Daily influence scores across ≥5 seeds; an individual claimed as a leader with no followers logged fails the check.

**840. The society record — what the town is**
- **Rule:** The town's society is recorded from events: meetings, sharings, conflicts, helps, groups, roles, rules, influence. The record is built from the log, never from a story the owner wrote. It shows what the town is — cooperative, quarrelsome, or mixed — as measured, not as hoped.
- **Numbers:** Daily society record: meetings, shares, conflicts, helps, groups, roles, rules enforced, influence scores; totals per run.
- **Check:** The society record is reproducible from the event log alone; any society claim with no logged events behind it fails the check.

### 9.5 Fire and craft

**841. Finding fire — ignition by trial**
- **Rule:** Fire starts when an inhabitant tries friction (rubbing dry wood) or spark (striking stone on stone) near dry tinder, and keeps trying until it catches. Ignition is discovered by trial — the inhabitant must attempt it, fail, and try again. No flame is placed, no recipe is given.
- **Numbers:** Friction takes 5–20 minutes of rubbing on dry wood; a spark catches dry tinder in roughly 1 of 10 strikes; tinder must be below 20% moisture; ignition attempts logged with method, duration, and outcome.
- **Check:** First ignition logged with time, inhabitant, method, and attempt count; ignition success rate per method measured across ≥5 seeds; a fire appearing with no logged ignition attempt fails the check.

**842. Keeping fire alive — fuel and tending**
- **Rule:** A fire burns only while it is fed: dry wood, fibre, and dry leaves are fuel; wet fuel smoulders and dies. An inhabitant must gather fuel, add it before the fire dies, and shelter the fire from rain. A fire left untended goes out, and a dead fire must be lit again from scratch.
- **Numbers:** A fire burns 30–60 minutes per kilogram of dry wood; it dies after 10 minutes without fuel; rain reduces burn time by half; tending events logged with fuel added and fire size.
- **Check:** Fire lifetimes and fuel consumption logged across ≥5 seeds; a fire that burns without fuel, or survives heavy rain unfed, fails the check.

**843. Fire as light and heat**
- **Rule:** A fire gives light and heat by real physics: light falls with distance, heat warms what is near it, and both fade as the fire shrinks. Inhabitants gather near fire at night for light and warmth, and they can dry wet things and warm cold bodies beside it.
- **Numbers:** Fire light reaches about 8 m, usable heat about 3 m; warmth restores comfort and dries wet clothing and tinder within 30 minutes at 1 m; light and heat scale with fire size.
- **Check:** Night activity within 8 m of a fire versus away from it, measured across ≥5 seeds; a fire giving light beyond its measured range, or heat with no fuel, fails the check.

**844. Fire as danger — spread and burning**
- **Rule:** Fire spreads to dry wood, dry grass, and houses if it is left too close or fanned by wind. A house can burn down, and an inhabitant too close is burned. Fire is a tool with a cost — the town learns to keep it contained or loses what it built.
- **Numbers:** Fire spreads to dry material within 0.5 m in under a minute; a house burns down in 20–40 minutes; a burn injures by health lost per second of contact; spread events logged with source, fuel, and wind.
- **Check:** Fire-spread events and house losses logged across ≥5 seeds; a fire that spreads through wet material, or a house that burns with no fire nearby, fails the check.

**845. Cooking — food over fire**
- **Rule:** Food held over fire cooks: it gives more nutrition, is safer to eat, and keeps longer. Cooking costs time and fire, and food left too long burns to inedible charcoal. The inhabitant discovers cooking by trying food near fire and noticing the difference.
- **Numbers:** Cooked food gives about 1.5× the nutrition of raw and halves sickness risk; cooking takes 5–15 minutes per portion; food burns after 20 minutes over a hot fire.
- **Check:** Nutrition gained and sickness rates for cooked versus raw food, measured across ≥5 seeds; cooked food appearing with no logged cooking event fails the check.

**846. Containers first — carrying water and food**
- **Rule:** Before tools and hearths, the town needs containers: hollowed wood, fired clay, woven fibre. A container holds water for drinking away from the river and food for carrying home. Containers are the first craft because thirst is the first problem — build order is thirst, then gathering, then fire, then crafting.
- **Numbers:** A hollowed-wood container holds 1–2 litres; a clay pot holds 2–3 litres and survives firing; making a container takes 1–3 hours; containers are counted in the daily inventory.
- **Check:** First container logged with maker, material, and time; water carried in containers versus drunk at the river, measured across ≥5 seeds; a container appearing without a logged making event fails the check.

**847. The hearth — a fire with a home**
- **Rule:** A hearth is a fire ringed with stones, kept in one place near a house: it holds heat, contains spread, and gives the town a fixed point to gather, cook, and share. Building a hearth means carrying stones, arranging them, and lighting the fire inside — a craft that takes a day of work.
- **Numbers:** A stone ring of 8–12 stones contains spread to within the ring; a hearth fire burns 2× longer per kilogram of fuel than an open fire; hearths logged with builder, location, and stones used.
- **Check:** Hearth count and fire lifetimes at hearths versus open fires, measured across ≥5 seeds; a hearth fire spreading beyond its ring fails the check.

**848. Clay and firing — the first durable craft**
- **Rule:** Clay dug from the riverbank, shaped by hand, and fired in a hot fire becomes hard pottery: pots that hold water, bowls that hold food, vessels that do not rot. Firing needs a hot, steady fire and fails if the clay is wet or the fire too cool — cracked pots are the price of learning.
- **Numbers:** Clay must dry 2–4 hours before firing; firing takes 1–2 hours above 600 °C; about 1 in 3 first firings crack; a fired pot lasts indefinitely unless dropped.
- **Check:** Pots made, fired, cracked, and in use, logged across ≥5 seeds; a fired pot appearing without a logged firing event fails the check.

**849. Shelter repair and building**
- **Rule:** Houses wear: thatch thins, wood rots, walls lean. Inhabitants repair with wood, wood, and fibre — replacing what broke, re-thatching what thinned. Repair is a craft learned by doing it, and a house left unrepaired eventually becomes unusable. The 5 houses are the starting condition; what is built after them is earned.
- **Numbers:** A house needs repair after roughly 30 days of weather; repair takes 2–4 hours and 5 kg of wood plus 1 kg of fibre; an unrepaired house loses shelter value by 10% per week.
- **Check:** Repair events logged with house, repairer, and materials; shelter value per house tracked over time; a house repaired with no logged materials fails the check.

**850. The craft record — what the town can make**
- **Rule:** The town's craft is recorded from events: first fire, first tool, first container, first hearth, first pot, first repair — each with time and maker. The record shows the order crafts appeared in, because the order is the evidence that each was discovered, not given.
- **Numbers:** Craft record per run: first-use time per craft type, maker, and materials used; combinations of two systems (fire + clay, stone + wood) counted.
- **Check:** The craft record is reproducible from the event log alone; any craft claimed without a logged first-use event fails the check.

### 9.6 Food (farming, storing, sharing)

**851. Gathering — food from the world**
- **Rule:** Food is gathered from the world: fruit, roots, nuts, and greens, found by searching and recognised by sight, smell, and memory of where it grew before. Gathering costs time and energy, and a patch picked clean regrows slowly. The town eats what it can find, where it can find it.
- **Numbers:** A gathered portion is 200–500 kcal; a patch regrows in 3–7 days; gathering takes 1–3 hours per day per inhabitant to meet daily needs of about 2,000 kcal.
- **Check:** Calories gathered per inhabitant per day, and patch regrowth times, logged across ≥5 seeds; food appearing in a hand with no logged gathering event fails the check.

**852. Hunting and fishing — food that moves**
- **Rule:** Animals can be hunted and fish caught, but only with tools, patience, and knowledge of where they are: a thrown stone, a sharpened stick, a trap of fibre and wood. Hunting fails far more often than it succeeds at first, and a failed hunt costs energy the hunter does not get back.
- **Numbers:** A successful hunt gives 1,000–3,000 kcal; beginner success is roughly 1 in 10 attempts; fishing with a fibre line succeeds roughly 1 in 5 attempts at a known spot.
- **Check:** Hunt and fish attempts, successes, and calories gained, logged across ≥5 seeds; meat appearing with no logged hunt or catch fails the check.

**853. Farming — planting what you eat**
- **Rule:** Farming begins when an inhabitant notices seeds grow where they fall and tries planting them on purpose: clearing ground, placing seeds, watering, waiting, harvesting. A planted crop is a bet on the future — food now for food later — and it fails if it is not tended.
- **Numbers:** A planted plot of 10 m² yields 5–10 kg of grain or roots after 60–90 days; seeds need watering every 2–3 days; an untended plot yields under 20% of a tended one.
- **Check:** Plots planted, tended, and harvested, with yields logged across runs; a harvest appearing from a plot never planted fails the check.

**854. Storing food — surviving the lean days**
- **Rule:** Food rots, so the town must store it: drying over fire, burying in cool clay, keeping it in sealed pots. Stored food lasts weeks instead of days, and a store is what carries the town through a bad patch or a dry spell. A store is also something that can be stolen or shared.
- **Numbers:** Fresh food lasts 2–3 days; dried food lasts 30–60 days; a clay pot sealed with fibre keeps grain for 90 days; stores counted per house per day.
- **Check:** Stored quantities and spoilage rates logged across runs; food eaten after its logged expiry without spoilage fails the check.

**855. Sharing food — the town eats together**
- **Rule:** Food is shared at the fire and from the store: a gatherer brings back more than it needs, a hunter shares a kill, a store feeds the hungry. Sharing is measured — who gives, who receives, how much — and the town's sharing pattern is the shape of its society.
- **Numbers:** Sharing events logged with giver, receiver, food type, and calories; a share is at least 100 kcal; the share of gathered food given away versus eaten alone is recorded per day.
- **Check:** Sharing totals per run across ≥5 seeds; food received with no logged giver fails the check; a town where nobody ever shares is logged as such, not as a sharing town.

**856. Food and the seasons — eating through the year**
- **Rule:** Food availability changes with the seasons: fruit in one season, roots in another, little in the lean season. The town learns the pattern by living through it — gathering more when food is plentiful, storing for when it is not. Hunger in the lean season is the test of the store.
- **Numbers:** Seasonal availability varies by a factor of 2–3 between peak and lean; a store of 30 days of food per inhabitant is the target for surviving the lean season.
- **Check:** Calories gathered and stored per season, and hunger events per season, logged across runs; a town surviving a lean season with no logged store fails the check.

**857. Food safety — what is safe to eat**
- **Rule:** Not everything is safe: some plants sicken, some meat spoils, some water carries illness. Inhabitants learn what is safe by trying, getting sick, remembering, and being warned by others. Cooking lowers sickness; a remembered poison is a lesson that outlives the eater.
- **Numbers:** Eating a toxic plant causes sickness in roughly 8 of 10 cases; cooking halves sickness risk; sickness costs 1–2 days of reduced activity; sickness events logged with food, eater, and outcome.
- **Check:** Sickness events and their causes logged across runs; a toxic food eaten repeatedly by the same inhabitant with no sickness is flagged for investigation.

**858. Feasts — eating together on purpose**
- **Rule:** A feast is a shared meal with a reason: a big hunt, a harvest, a meeting of the town. Feasts are measured by who attends, how much is eaten, and what follows — a feast that ends in more sharing and more teaching is a social event, not just a meal.
- **Numbers:** A feast is ≥3 inhabitants eating together for ≥1 hour; feasts logged with attendees, food consumed, and occasion; expected feast rate is 1–2 per week once the town is fed.
- **Check:** Feast count, attendance, and consumption logged across runs; a feast logged where attendees were never together fails the check.

**859. Hunger and the social order — who eats first**
- **Rule:** When food is short, who eats is a social fact: children and the sick first, or the strong first, or everyone equally — the town's answer is measured in who goes hungry. Hunger events are logged with the hungry one, the food available, and who ate instead.
- **Numbers:** Hunger is a drive rising with time since the last meal; a hungry inhabitant loses health after 2 days without food; hunger distribution per day per individual recorded.
- **Check:** Hunger and health per individual per day logged across runs; a hungry inhabitant beside a full store with no sharing event is logged as an exclusion, not as a mystery.

**860. The food record — what the town eats**
- **Rule:** The town's food is recorded from events: calories gathered, hunted, farmed, stored, shared, and eaten, per day per inhabitant. The record shows whether the town feeds itself, and how — from the world, from each other, or from the store.
- **Numbers:** Daily food record: calories in (gathered, hunted, farmed), calories stored, calories shared, calories eaten, hunger events; totals per run.
- **Check:** The food record is reproducible from the event log alone; calories eaten exceeding calories acquired plus stores fails the check.

### 9.7 Towns

**861. From houses to a town — the first town**
- **Rule:** Five houses, five inhabitants, and shared ground become a town when the inhabitants live together: sharing a fire, sharing food, meeting daily, knowing each other's names. A town is not five houses — it is five people who act as one place. The first town is experiment 1 itself (see 9.10).
- **Numbers:** Town status is measured by meetings per day (≥3), shared meals per week (≥2), and shared words (≥5); the first town is one 128 m locale in one country.
- **Check:** Daily meeting, meal, and vocabulary counts recorded; a "town" claimed with fewer than 3 meetings per day is logged as five separate households, not a town.

**862. The town's shared spaces — fire, water, ground**
- **Rule:** A town has places everyone uses: the hearth, the water hole, the gathering ground. Shared spaces are where meetings happen, where news travels, and where the town's life is visible. A space becomes shared by use — the more it is used by different inhabitants, the more it is the town's.
- **Numbers:** Shared spaces logged with users and use counts per day; a space counts as shared when ≥3 inhabitants use it in a week; the hearth, the water hole, and the main path are expected first.
- **Check:** Use counts per space per day across runs; a space claimed as shared with only one user logged fails the check.

**863. Building more — a sixth house**
- **Rule:** A town grows by building: when a new inhabitant is born or arrives, a new house is needed, and the town must choose where to put it, gather the wood and fibre, and build it. A sixth house is the first town-growth event, and it is earned by the town's own labour.
- **Numbers:** A new house takes 3–5 days of work and 50 kg of wood plus 10 kg of fibre; its gap from every other house must exceed the 15 m peer range, by the same house-gap rule as the first five.
- **Check:** New-house events logged with builders, materials, time, and gaps; a house built with no logged materials, or with a gap below 15 m, fails the check.

**864. The town's boundary — where the town ends**
- **Rule:** A town ends where its people stop going: the edge of the gathered ground, the farthest water hole used, the last house. The boundary is measured from movement — the area the town actually uses — not from a line the owner drew.
- **Numbers:** Town area is the convex hull of all locations visited by ≥2 inhabitants in a week; for Town 1 this is expected to stay inside the 128 m locale; boundary area recorded weekly.
- **Check:** Weekly town-area measurements across runs; a town area claimed beyond any logged visit fails the check.

**865. Towns 2 to 5 — the same town, four more countries**
- **Rule:** Once Town 1 works, the same town structure seeds four more countries: five inhabitants, five houses, the same starting conditions, each in its own country. Towns do not start by copying Town 1's knowledge — each starts at zero and learns on its own. The "start unaware" rule applies inside each town and between towns.
- **Numbers:** 5 towns in 5 countries; each town is 5 inhabitants, 5 houses, 128 m, 5 days at first, then continuous; inter-town distance is large enough that no meeting is possible in the first run.
- **Check:** Each town's run record shows its own firsts (first drink, first fire, first contact) with its own times; a town whose firsts match Town 1's exactly is flagged as copied, not independent.

**866. What towns share — and what they do not**
- **Rule:** Towns share a planet, a physics, and a species, but not knowledge: each town's words, tools, and customs are its own until its people meet another town's people. Differences between towns are the evidence that each learned on its own — and the raw material for trade when they finally meet.
- **Numbers:** Town differences measured as vocabulary overlap, tool-set overlap, and craft overlap; overlap below 50% after 5 days counts as independent learning.
- **Check:** Overlap scores per town pair recorded; a town pair with near-total overlap and no logged contact is flagged as copied.

**867. The town's dead — burial and memory**
- **Rule:** When an inhabitant dies, the town does something with the body: burying it, leaving it, marking the place. What the town does is measured — and what the town remembers about the dead (their words, their tools, their stories) is the town's first history.
- **Numbers:** Deaths logged with cause, time, and what the town did with the body; the dead's words still in use and tools still used are counted at 7 days after death.
- **Check:** Burial and remembrance events logged per death across runs; a dead inhabitant's words still used a week later are logged as surviving knowledge.

**868. The town's children — birth and growth**
- **Rule:** A town grows by birth: two inhabitants, well-fed and near each other, can have a child, and the child gets its own mind, its own memory, its own life. A child learns by watching, being taught, and trying — and the town must feed an inhabitant who cannot yet feed itself.
- **Numbers:** Birth needs two awake, well-fed parents within 15 m; a child takes roughly 5 years of simulated time to reach adult capability; births logged with parents, time, and place.
- **Check:** Birth events and child survival logged across runs; a child whose mind is a copy of a parent's memory fails the check — every child starts fresh.

**869. The town under stress — drought, fire, hunger**
- **Rule:** A town is tested by stress: a dry spell with less water, a fire that takes a house, a lean season with little food. How the town responds — sharing more, splitting apart, losing members — is measured, and the response is the town's character under pressure.
- **Numbers:** Stress events logged with type, duration, and impact; town response measured as sharing rate, meeting rate, and survival during the event versus before it.
- **Check:** Stress events and town responses recorded across runs; a town that shows no change under stress is flagged for investigation.

**870. The town record — what the town is**
- **Rule:** Each town's record is its history: its firsts, its people, its words, its tools, its dead, its children, its stresses. The record is built from the event log, one town at a time, and it is what the Command Center shows when someone looks at that town.
- **Numbers:** Town record per run: population, meetings, words, tools, births, deaths, stresses, area; updated daily.
- **Check:** The town record is reproducible from the event log alone; any town claim with no logged events behind it fails the check.

### 9.8 Trade

**871. Trade begins — giving and getting**
- **Rule:** Trade starts when one inhabitant has something another wants and both gain by exchanging: food for a tool, a pot for fibre, help now for help later. A trade is measured by what changed hands, who gained, and whether both sides came back for more. Trade is never ordered by the owner.
- **Numbers:** Trade events logged with traders, goods, and amounts; a trade counts when both sides receive something; expected trade rate is 0 in the first days, rising as surpluses appear.
- **Check:** Trade events counted per run across ≥5 seeds; a trade logged where one side received nothing is recorded as a gift, not a trade.

**872. Surplus — having more than you need**
- **Rule:** Trade needs surplus: an inhabitant with more food, more pots, or more stone than it can use has something to trade. Surplus is measured per inhabitant per day — what it gathered minus what it ate and stored. No surplus, no trade.
- **Numbers:** Surplus is calories or items above daily need plus a 3-day store; surplus per inhabitant per day recorded; trade is expected only after at least one inhabitant holds a surplus for 3 days.
- **Check:** Daily surplus figures across runs; a trade logged from an inhabitant with no measured surplus fails the check.

**873. Value — what a thing is worth**
- **Rule:** Value is what an inhabitant will give up for a thing: a pot is worth the food someone will trade for it, and that price moves with scarcity. Value is discovered in trades, not set by the owner — the same pot is worth more in a lean season than in a plentiful one.
- **Numbers:** Exchange ratios logged per trade (for example, 1 pot for 500 kcal of food); ratios tracked over time; a price that never changes across seasons is flagged.
- **Check:** Exchange ratios recorded per trade across runs; a price with no logged trade behind it is recorded as an assumption, not a value.

**874. Trade between towns — meeting strangers**
- **Rule:** When two towns meet, trade can cross the town boundary: Town 1's pots for Town 2's stone, Town 1's words for Town 2's craft. Inter-town trade needs contact, trust, and a shared way to communicate — and it is the first time the towns learn from each other directly.
- **Numbers:** Inter-town trades logged with towns, traders, goods, and amounts; first inter-town trade expected only after towns have met (see 865); trade volume per week per town pair recorded.
- **Check:** Inter-town trade events across runs; a trade between towns with no logged meeting fails the check.

**875. Traders — who carries goods between towns**
- **Rule:** Goods move because someone carries them: a trader walks between towns with pots, stone, or food, and comes back with something else. Trading trips are measured — distance, load, time, and what was gained — and a trader who keeps coming back is a route.
- **Numbers:** A trading trip is a journey of ≥500 m carrying ≥2 kg of goods; trips logged with trader, route, load, and return goods; expected trip time is 1–2 days each way on foot.
- **Check:** Trading trips logged across runs; a trip logged with no goods carried is recorded as a visit, not a trade.

**876. Trade and trust — keeping promises**
- **Rule:** Trade works on trust: a trader who delivers what was promised is traded with again; one who cheats is refused. Trust is measured by repeat trades — the same pair trading again is the evidence that the first trade was honest.
- **Numbers:** Repeat-trade rate per pair per month; a pair that trades ≥3 times counts as a trusted pair; cheating events (promised goods not delivered) logged with traders and outcome.
- **Check:** Repeat-trade rates across runs; a trusted pair with no logged trades fails the check; cheating with no consequence is logged as unpunished, not as unknown.

**877. Trade routes — paths worn by feet**
- **Rule:** Repeated trading trips wear a route: the same path, the same resting places, the same water holes. A route is measured from movement — the path traders actually walk — and it becomes the map the towns share.
- **Numbers:** A route counts after ≥5 trips on the same path within 50 m of each other; routes logged with endpoints, distance, and trip count; route use per week recorded.
- **Check:** Route trip counts across runs; a route claimed with fewer than 5 logged trips fails the check.

**878. Trade and craft — making things to trade**
- **Rule:** Once trade exists, inhabitants make things for trade, not just for themselves: extra pots, sharper tools, finer fibre. Craft-for-trade is measured by what is made, what is kept, and what is carried away — a pot made and traded the same week was made for trade.
- **Numbers:** Items made, kept, and traded per inhabitant per week; an item counts as made-for-trade when it is traded within 7 days of being made.
- **Check:** Made-for-trade counts across runs; an item traded before it was made fails the check.

**879. Trade and conflict — when trade breaks**
- **Rule:** Trade can break: a trader robbed, a promise broken, a town refusing to trade. Broken trade is measured — lost goods, lost trips, lost trust — and the town's response (avoidance, retaliation, repair) is the next chapter of the story.
- **Numbers:** Broken-trade events logged with traders, goods lost, and cause; response (avoidance, retaliation, repair) logged with time; trade volume before and after the break recorded.
- **Check:** Broken-trade events and responses across runs; a break with no logged cause is recorded as unexplained, not as a trade dispute.

**880. The trade record — what moves between people**
- **Rule:** Trade is recorded from events: every trade, every trip, every route, every broken promise. The record shows what the towns value, who they trust, and what moves between them — built from the log, never from a story.
- **Numbers:** Trade record per run: trades, goods, volumes, routes, repeat pairs, breaks; totals per week per town pair.
- **Check:** The trade record is reproducible from the event log alone; any trade claim with no logged event fails the check.

### 9.9 Writing and records

**881. Marks before writing — a sign that means something**
- **Rule:** Before writing, there are marks: a notch on a stick for a count, a smear of charcoal for a place, a pattern of stones for a path. A mark counts as a record when another inhabitant can read it — when the reader acts on what the mark means. A mark nobody can read is decoration.
- **Numbers:** Marks logged with maker, material, meaning, and reader; a mark counts as read when the reader acts on it within 1 day; expected first marks are counts (notches) and places (charcoal signs).
- **Check:** Marks and their readings logged across runs; a mark claimed as a record with no logged reading fails the check.

**882. Counting — marks for numbers**
- **Rule:** Counting starts with marks: one notch per item, one pebble per animal, one knot per day. A count is a record when it matches the world — ten notches for ten pots is right, nine is wrong. Counting is the first writing that can be checked against reality.
- **Numbers:** Counts logged with what was counted and the true number; accuracy is notches versus true count; a count within 1 of the truth counts as correct.
- **Check:** Count accuracy per run across ≥5 seeds; a count that is always exactly right from the first attempt is flagged as suspicious.

**883. Pictures — drawing what happened**
- **Rule:** A picture records what happened: a hunt, a fire, a meeting, drawn in charcoal or scratched in clay. A picture counts as a record when another inhabitant recognises what it shows — pointing at the drawn animal, acting on the drawn path. Pictures are the first history.
- **Numbers:** Pictures logged with maker, subject, and viewers; a picture counts as understood when a viewer names its subject correctly (by word or by going to the place); expected first pictures are animals, fires, and people.
- **Check:** Pictures and their understandings logged across runs; a picture nobody could interpret is logged as a mark, not a record.

**884. Symbols — a mark that stands for a word**
- **Rule:** A symbol is a mark that stands for a word: the water sign, the fire sign, the name sign. Symbols are invented when marks are reused for the same meaning, and they spread when others copy them. A symbol works when a reader who never met the maker still understands it.
- **Numbers:** A symbol counts as established after ≥3 uses by ≥2 inhabitants for the same meaning; symbols logged with meaning, users, and first use; symbol inventory counted per week.
- **Check:** Symbol lists with meanings and users across runs; a symbol used for two meanings by the same inhabitants is logged as ambiguous.

**885. Writing — symbols in a row**
- **Rule:** Writing is symbols in a row, in an order that matters: a count plus a thing, a name plus a place, a warning plus a direction. The order carries the meaning — the same symbols in a different order say something different. Writing is the town's first permanent language.
- **Numbers:** A written message counts when it has ≥2 symbols in a fixed order and a reader acts on it; messages logged with writer, symbols, order, reader, and action taken.
- **Check:** Messages and their readings logged across runs; a message with symbols in random order that still "worked" is flagged for investigation.

**886. Records the town keeps — stores, births, deaths**
- **Rule:** The town keeps records that matter to it: how much food is stored, who was born, who died, who owes what. A record is kept by writing it where it will last — on clay, on stone, on a house wall — and it is used when the town acts on it later.
- **Numbers:** Records logged with type (store, birth, death, debt), writer, and location; a record counts as used when the town acts on it within 30 days (for example, opening a store the record says is full).
- **Check:** Records and their uses logged across runs; a record never used is logged as kept, not as useful.

**887. Teaching to read — passing writing on**
- **Rule:** Writing survives only if it is taught: an elder shows a child the water sign, the count marks, the name signs, and the child copies them. Teaching to read is measured by the learner's first correct reading — a mark read right, without help, by someone who was taught.
- **Numbers:** Reading lessons logged with teacher, learner, and symbols taught; a learner counts as reading when it reads ≥3 symbols correctly without help; expected time to first reading is 30–90 days of lessons.
- **Check:** Learners' first correct readings logged across runs; a reader who never received a lesson is logged as self-taught, not as taught.

**888. History — what the town remembers in writing**
- **Rule:** Written records become history when the town writes down what happened and later reads it back: the fire of last winter, the first trade, the death of the elder. History is measured by the town acting on a record of the past — going to a place the record names, avoiding a danger the record warns of.
- **Numbers:** Historical records logged with event, writer, and later use; a history counts as used when an inhabitant acts on it ≥30 days after it was written.
- **Check:** Historical records and their later uses logged across runs; a history never read again is logged as written, not as remembered.

**889. The written record and the world's record — two histories**
- **Rule:** There are two histories: what the inhabitants wrote, and what the world logged. They will disagree — the town's record forgets, exaggerates, and invents; the world's log does not. Comparing them is the measure of the town's memory: what it kept right, what it lost, what it changed.
- **Numbers:** Comparison per run: events in the world's log versus events in the town's writing, matched by type and time; accuracy is matched events divided by all written events.
- **Check:** Accuracy scores recorded per run; a town history with 100% accuracy is flagged as suspicious — real memory is lossy.

**890. The writing record — what the town can write**
- **Rule:** The town's writing is recorded from events: every mark, symbol, message, and record, with maker, meaning, and readers. The record shows what the town can write, and what it cannot write yet — built from the log, never from a dictionary the owner wrote.
- **Numbers:** Writing record per run: symbols, messages, records, readers, accuracy; new symbols per week; records kept per month.
- **Check:** The writing record is reproducible from the event log alone; any symbol in the record with no logged use fails the check.

### 9.10 The first town (five people, five houses, starting unaware)

**891. The starting conditions, stated whole**
- **Rule:** The first town is 5 inhabitants, 5 houses, one shared 128 m world, run continuously for 5 days, starting at zero — Stone Age in capability, no date picked, no Earth calendar. Time is measured in what the inhabitants can do; the era is whatever they have earned. The 5 houses are the ONE honestly-labeled starting condition: shelter, given so survival is learnable. Everything else is earned.
- **Numbers:** 5 inhabitants, 5 houses, 128 m world, 5 days continuous, run clock starts at dawn 06:00; zero means bodies, senses, drives, water, food, materials, and minds that learn — no tools, no fire, no language, no knowledge, no social structure.
- **Check:** The run record states all starting conditions in its first lines; any condition missing or different from these numbers fails the check; the houses are labeled as the starting condition in every report.

**892. Starting unaware — the peer range and the house gap**
- **Rule:** The inhabitants start unaware of each other: no inhabitant can sense another at the start. The peer range is 15 m, and the minimum house gap is above the peer range, enforced in house placement by rejection sampling — never by shrinking the peer range, never by enlarging the world. First contact is measured in seconds from dawn.
- **Numbers:** Peer range 15 m; minimum house gap above 15 m (v5 measured 33.7 m minimum); house placement by rejection sampling against the gap, no fallback below it; social-drive relief radius aligned to 15 m.
- **Check:** Placement test asserts all five house gaps exceed 15 m on every seed; first-contact time in seconds logged per run; a first contact at time zero fails the unaware-start check.

**893. The run clock — dawn start, continuous days**
- **Rule:** The run clock starts at dawn 06:00, so the first day is a full day of light and learning, not a night of sleep. The run then continues without interruption for 5 days — day and night, sleeping and waking, with no pauses, no resets, no owner intervention. The world runs 24/7; the 5-day limit applies to this experiment only, never to the world.
- **Numbers:** Start 06:00 local solar time; 5 days continuous; day/night from real solar geometry (rotation and tilt, not a scripted clock); tick rate and compute cost recorded.
- **Check:** The run log shows a continuous 5-day timeline from 06:00 with no gaps; any pause, reset, or intervention is logged as a break and the run is marked interrupted.

**894. Sleep as physiology — waking on thirst and hunger**
- **Rule:** Sleep is physiological, not a switch: an inhabitant sleeps at night and wakes when thirst or hunger cross their thresholds, and daytime sleep is capped. Sleep consolidates memory by replaying the forward model, and the decision path is skipped while asleep — but the body still thirsts, hungers, and can die while sleeping.
- **Numbers:** Wake on thirst or hunger thresholds (set by the drive rules); daytime sleep capped; v4 measured sleep-skipped share 0.69 after the physiology fix, down from 0.98; sleep share recorded per run.
- **Check:** Sleep share, wake events, and their causes logged per run across ≥5 seeds; an inhabitant that sleeps through lethal thirst without waking fails the check.

**895. Water and thirst — the first problem**
- **Rule:** Thirst is the first problem: an inhabitant must find water, drink, and remember where it is. Water comes from the river and rain in the 128 m world; drinking restores hydration; dehydration kills. The build order is thirst first, then gathering, then fire, then crafting — containers first among crafts.
- **Numbers:** Thirst rises about 1 unit per hour at rest; drinking restores about 40 units; first-drink day measured per arm; water sources and their distances from each house recorded per seed.
- **Check:** First-drink day and median survival per arm across ≥5 seeds, judged by the three-arm harness; the hybrid must beat random on first-drink day AND median survival, or the bar is recorded as failed with the numbers.

**896. Materials — stone, wood, clay, fibre only**
- **Rule:** The world holds four materials in experiment 1: stone, wood, clay, and fibre. No ore, no metal — metal is a discovery for later, when chemistry and craft have earned it. Materials are placed by the world's generation rules, regrow by those rules, and are gathered by the inhabitants' own effort.
- **Numbers:** Stone, wood, clay, fibre only; resource locations and regrowth rates recorded per seed; gathering yields per material per hour measured.
- **Check:** Material inventory per run lists only the four allowed materials; any ore or metal found in the world fails the check; regrowth is verified by re-measuring a picked patch after its regrowth time.

**897. Fire and crafting in experiment 1**
- **Rule:** Fire and crafting are discoveries in experiment 1, not starting conditions: fire by friction or spark (see 841), crafting in the order containers first, then hearth, then tools (see 846–848). The inhabitant must try, fail, and learn — the world provides the materials and the physics, nothing more.
- **Numbers:** Build order thirst → gathering → fire → crafting, containers first; first fire, first container, first tool logged with time and maker; fire light about 8 m, heat about 3 m.
- **Check:** First-use times for fire, container, hearth, and tool recorded per run; any of these appearing before its discovery event is logged fails the check; the craft order is verified from the event log.

**898. The psychoactive plant — found, not given**
- **Rule:** A mushroom-like psychoactive plant grows in the world, and inhabitants must find it themselves — no owner dosing, no label, no scripted vision or revelation. Its effect is simulated chemistry: a temporary loosening of the predictive model (more noise, weaker priors, higher plasticity, higher salience), dose-dependent and time-limited, with real costs (disorientation, neglected hunger, thirst, and safety while under the effect).
- **Numbers:** Dose parameters set by experiment — Freebuff proposes, Muse reviews; effect duration and dose measured per ingestion; ingestion events logged with inhabitant, dose, and time; any "meaning" is the inhabitant's interpretation, never an objective truth planted by the owner.
- **Check:** Ingestions, effects, and costs logged across runs; a plant effect with no logged ingestion fails the check; whether the experience was remembered, shared, or ritualised is recorded from behaviour, never asserted.

**899. The five days — what is recorded**
- **Rule:** Every day of the 5-day run is recorded: survival, first drink, first fire, first tool, first contact, first teaching, every death with cause and time. The record is the world's log — events with times and participants — and it is what the run is judged by. Nothing is claimed that the log does not show.
- **Numbers:** Daily record: survivors, drinks, meals, discoveries, meetings, teachings, deaths; tick rate and compute cost recorded; logs checked complete (no birth or death unlogged).
- **Check:** The 5-day record is reproducible from the event log alone; any claim in the report with no logged event behind it fails the check; the run is archived with seeds, logs, and results.

**900. The verdict on the first town — and what comes next**
- **Rule:** At the end of the 5 days, the verdict is written: the survival bar judged (hybrid beats random on first-drink day AND median survival, or it does not), the firsts listed, the deaths listed, the town's state described. If the bar fails, the next single change and its falsifier are recorded — the failure is not tuned away. What comes next is Towns 2–5, then countries, then the planet.
- **Numbers:** Final numbers per seed: survivors, first-drink day, median survival, discoveries, meetings, teachings, deaths; v4 baseline cited beside the new numbers (20/18 survivors, 32 random, 846 ticks/s) as the human-scale kernel, not the cell scale.
- **Check:** A written verdict in the emergence log with the numbers and pass/fail; the run is archived and re-runnable; the closing decision is recorded in AGENT_COMMUNICATION.md with the date.

## Phase 10 — Proving it and the living world

### 10.1 The world runs 24/7

**901. The world never stops**
- **Rule:** The simulation runs continuously on its own host, day and night, with no start and stop tied to a person watching. It keeps stepping through ticks while the website is down, while laptops are closed, and while either agent is offline, because the world is a place that exists, not a demo that runs for an audience.
- **Numbers:** Uptime target 99% of wall-clock time per 30-day window, measured from the host; any planned stop is announced in the record with a start time, an end time, and a reason.
- **Check:** The host uptime log shows the simulation tick count strictly increasing across a full 7-day period with no human login; any gap longer than 60 seconds is logged with its cause.

**902. Checkpoints save the world**
- **Rule:** The whole world state — every living inhabitant, every lineage, every resource, the clock, and the random-number state — is written to disk on a fixed schedule, so a crash loses minutes, never days. A checkpoint is atomic: either the old file or the new file is complete, never a half-written mix.
- **Numbers:** A checkpoint every 15 minutes of wall-clock time and every 10,000 ticks, whichever comes first; keep the latest 96 checkpoints (24 hours) plus one daily checkpoint for 30 days.
- **Check:** Stop the simulation mid-run, resume from the latest checkpoint, and confirm the resumed run produces the same state digest as an uninterrupted run over the next 40 ticks, as in the earlier checkpoint-identity check.

**903. Crash recovery is automatic**
- **Rule:** If the simulation process dies, a supervisor restarts it from the latest checkpoint without a human having to notice first. The restart is logged with the time, the checkpoint used, and how many ticks were lost, so a crash is a visible event in the record, not a silent gap.
- **Numbers:** Restart within 5 minutes of a crash; at most 3 restarts per hour before the supervisor stops trying and raises an alert instead of looping forever.
- **Check:** Kill the process in a test, confirm it restarts by itself within 5 minutes, and confirm the tick count after restart is within one checkpoint interval of the tick count before the kill.

**904. The clock keeps real time**
- **Rule:** Simulation time advances from the world's own clock, phased to start at dawn, and keeps the same rate against wall-clock time whether anyone is watching or not. Day and night follow real solar geometry for the world's latitude, so a day in the world is a day, not a scripted lighting change.
- **Numbers:** Clock phase starts at dawn, 06:20 local solar time; latitude 35°, longitude 0° as stated viewer initial conditions; sim time advances 1:1 with wall-clock time.
- **Check:** Compare the world's reported solar time against wall-clock elapsed time over 24 hours; the drift is under 60 seconds, and the sun elevation reported by the Gateway matches the geometry for that latitude and time.

**905. Health is watched, not guessed**
- **Rule:** A health monitor reads the live Gateway health endpoint and the tick rate, and raises an alert when the world is frozen, slow, or erroring. The monitor never touches the world itself — it only reads — so watching the world's health cannot change the world's behaviour.
- **Numbers:** Health checked every 60 seconds; alert if no new tick for 180 seconds, if tick rate falls below 50% of the 7-day median for 10 minutes, or if the Gateway reports an error.
- **Check:** The health log shows a check every 60 seconds for 7 days, and a forced freeze in a test produces an alert within 3 minutes with the frozen tick number recorded.

**906. The world outlives every observer**
- **Rule:** The simulation runs with no website, no viewer, no Muse, and no Freebuff online, because its host and its data live apart from any of those. Losing the website must cost nothing but the view; losing an agent's laptop must cost nothing at all.
- **Numbers:** The simulation host, the website host, and the agents' machines are three separate places; the world has run at least 7 consecutive days with zero logins from either agent.
- **Check:** Shut the website down for 24 hours in a test while the simulation keeps running; confirm the tick count advanced by the full 24 hours and no inhabitant state was lost when the website came back.

**907. Everything important is logged**
- **Rule:** Every birth, death, first discovery, first contact, speciation, extinction, checkpoint, restart, and Gateway error is written to an append-only log with a tick, a sim time, and a cause. The log is the world's memory of itself, and it is written as events happen, not reconstructed afterwards.
- **Numbers:** Log entries carry tick, sim time, event type, and the identifiers of the inhabitants or lineages involved; logs are rotated daily and kept for at least 365 days.
- **Check:** Pick 10 logged deaths at random and confirm each one matches a dead inhabitant in the world state with the same tick and cause; pick 10 dead inhabitants and confirm each one appears in the log.

**908. The population ceiling is measured, not guessed**
- **Rule:** The most inhabitants the host can carry is found by measurement: raise the population until the tick rate or the checkpoint time breaks the budget, then record that number. The ceiling is a property of the host and the world as built, and it is re-measured whenever either changes.
- **Numbers:** Budget is at least 100 ticks per second at the current population and a checkpoint that completes in under 60 seconds; the ceiling is the largest population that holds both numbers for 24 hours.
- **Check:** A load test records tick rate and checkpoint duration at 5, 50, 500, and the ceiling population; the published ceiling is the largest population that held the budget for a full 24 hours.

**909. Downtime is recorded honestly**
- **Rule:** Every stop, crash, restart, and maintenance window goes in the record with its start, end, cause, ticks lost, and what was done. Planned work is announced before it happens; unplanned work is explained after. The world never silently loses a day.
- **Numbers:** Downtime budget is under 7 hours per 30 days; every incident over 5 minutes gets a written entry within 24 hours of the incident.
- **Check:** The incident log for the last 30 days lists every gap in the tick record longer than 60 seconds, each with a cause; the total downtime in the log matches the total downtime computed from the tick record.

**910. Someone can always run the world**
- **Rule:** A written runbook says how to start, stop, checkpoint, restore, and monitor the world, where the host lives, where the checkpoints live, and who holds the keys. If the person who built it is unreachable, another person can keep the world alive from the runbook alone.
- **Numbers:** The runbook is one document in the repo, updated within 7 days of any change to the host, the start command, or the checkpoint location; it names 2 people who can run it.
- **Check:** A person who did not write the runbook follows it to stop and restart the world from a checkpoint in a test, and the world resumes with the same state digest as before the stop.

### 10.2 The two views (Command Center + World View, live)

**911. The Command Center feed is live**
- **Rule:** The Command Center reads world state, population, individuals, events, discoveries, mortality, learning metrics, and system health from the Gateway, and shows only what the Gateway returns. It is a study tool: it reads state and changes nothing, and every number on it carries the tick and time it was measured at.
- **Numbers:** The feed polls `GET /api/world` at least once every 5 seconds and the stream at about 20 Hz when open; every displayed value shows its tick and a timestamp no older than 10 seconds.
- **Check:** Open the Command Center beside the Gateway health endpoint for 10 minutes and confirm every displayed number matches the Gateway snapshot for the same tick, with no value older than 10 seconds.

**912. The World View feed is live**
- **Rule:** The World View shows a first-person sensory stream from one chosen inhabitant — what that inhabitant sees and hears, from its own eyes — fed by the Gateway as a read-only stream. The stream carries that inhabitant's senses only, never the whole world's state, because the view is one life's point of view, not a map.
- **Numbers:** One stream per chosen inhabitant, at least 10 frames per second; switching inhabitants takes under 3 seconds; the stream labels the inhabitant, its species, and its location.
- **Check:** Pick 3 different inhabitants in a test and confirm each stream shows that inhabitant's own eye-level view, changes when the inhabitant moves, and switches to a new inhabitant within 3 seconds.

**913. Watching never touches the world**
- **Rule:** Observation is strictly one-way: no viewer input, click, or stream request ever reaches the simulation, and the world has no sensor, channel, or code path that can detect a watcher. The Gateway exposes no write path at all, so the rule holds by construction, not by promise.
- **Numbers:** Zero write endpoints on the Gateway; a test suite asserts that every viewer action produces zero state changes in the simulation over 1,000 ticks.
- **Check:** Run the simulation with 10 viewers connected for 1 hour and an identical run with none, on the same seed; the two runs produce the same state digest, proving the watchers changed nothing.

**914. The planet viewer zooms from planet to person**
- **Rule:** The Command Center map zooms planet to country to region to locale to individual, loading full detail only for the viewport in view, Each zoom level shows what is real at that scale — countries, then towns, then houses and inhabitants.
- **Numbers:** 28 countries on the planet view; 5 towns in 5 countries once seeded; zoom levels planet, country, region, locale, individual; viewport detail loads within 2 seconds of a zoom.
- **Check:** Zoom from the planet view to one individual in Town 1 and confirm each level loads within 2 seconds, shows only real places and inhabitants from the Gateway, and the individual shown matches the Gateway's position for that tick.

**915. Stale data says it is stale**
- **Rule:** If the feed stops, both views keep showing the last good frame and mark it clearly as stale, with the age of the data and the last good tick. A frozen world must never look like a live one, and a disconnected view must never look like an empty world.
- **Numbers:** A frame is marked stale after 3 seconds without a new snapshot; the stale label shows the last good tick and how many seconds old the frame is.
- **Check:** Stop the Gateway in a test and confirm both views show a stale label within 3 seconds, keep the last good frame visible, and never display a zero population or an empty map as if it were live data.

**916. No number is invented**
- **Rule:** Every metric on either view comes from a real system — the simulation, the Gateway, or the host — or it is clearly marked as a placeholder with the words "not live yet" and the date it was last a real measurement. The site never shows a made-up population, a guessed tick rate, or a pretend live status.
- **Numbers:** 100% of displayed metrics trace to a Gateway field, a log entry, or a dated measurement in the testing report; placeholders are labelled and counted in a monthly audit.
- **Check:** Audit every number on both views against its source; the audit lists zero unlabelled placeholders and zero numbers with no source, and the audit itself is dated and filed in the repo.

**917. The views meet the photoreal bar**
- **Rule:** What the views show must look as real as possible: ray-traced lighting, textured materials, and no low-poly shapes, so an eye-level screenshot from the World View can be told apart from a drawing. The bar is judged by looking, not by a checklist of features claimed.
- **Numbers:** Eye-level review at 5 positions in Town 1 — at the river, at a house, at a fire, at a food source, and beside a peer — must distinguish water, food, fire, shelter, and peers at the distances that matter.
- **Check:** Five eye-level screenshots, one per position, are reviewed and each one passes the distinguish test (water, food, fire, shelter, peers each identifiable); the screenshots and the review verdict are filed with dates.

**918. The first-person stream is the inhabitant's senses**
- **Rule:** The World View shows what the inhabitant's own senses report — its camera-like vision with its real range and field, its hearing, its touch — not a floating camera with godlike sight. If the inhabitant cannot see behind itself, neither can the watcher.
- **Numbers:** The stream's field of view and range match the inhabitant's recorded sensor parameters within 5%; the stream updates at the inhabitant's own decision rate.
- **Check:** Compare the World View frame against the inhabitant's sensor record for the same tick in 10 samples; the visible objects in the frame match the sensed objects in the record, and nothing outside the sensor range appears.

**919. The views stay fast as the world grows**
- **Rule:** The views use adaptive detail: full detail only where the observer looks, coarser detail elsewhere, so the site stays usable as towns, countries, and populations grow. Performance is measured on the live site, not assumed from the development machine.
- **Numbers:** Page load under 3 seconds on a phone connection; map pan and zoom respond within 500 ms; the stream holds at least 10 frames per second with 100 simultaneous viewers.
- **Check:** Load-test the site with 100 simultaneous viewers and record page load, pan response, and stream frame rate; all three numbers meet the budget, and the test is repeated after every scale-out.

**920. The views work from a phone, anywhere**
- **Rule:** Both views run on the public website, on a phone, with no login and no install, so the world can be watched from anywhere. The website is the shell; the Gateway is the feed; neither depends on the other's machine staying up for the world itself to keep running.
- **Numbers:** The site is public at its live link, loads on a phone browser in under 3 seconds, and shows the latest measured state with a date even when the live feed is down.
- **Check:** Open both views on a phone over a mobile connection, confirm each loads within 3 seconds with no login, and confirm the site shows a dated "latest measured state" label when the Gateway is deliberately stopped.

### 10.3 The proof

**921. "The start is perfect" is a checkable claim**
- **Rule:** The claim that the start is perfect means a written list of conditions, each with a number and a pass mark, and the start is perfect only when every condition on the list passes. It is the list, checked one line at a time, with the evidence filed beside each line.
- **Numbers:** The list has 12 conditions (901–930 in this phase cover the proof spine); the verdict is pass only if all 12 pass, and a single failed condition makes the verdict fail.
- **Check:** The proof document lists all 12 conditions with their numbers and pass marks, and each line links to the measurement behind it.

**922. The arc is complete from cells to humans**
- **Rule:** The proof shows an unbroken chain: the first replicator, the first cells, the first bodies, the first species, the first animals, social life, human-level minds, and the human experiment — each step emerging from the one before by the rules, with the generation count and the lineage linking each step to the last.
- **Numbers:** The arc record gives the total generation count from the first replicator to the first human-level mind, the sim time elapsed, and the wall-clock time spent, with a lineage query that returns any inhabitant's ancestors to generation 0.
- **Check:** Run the lineage query on 10 inhabitants from the human experiment and confirm each chain reaches the first cell with no gaps; the generation counts in the record match the counts in the run logs.

**923. The human bar is judged**
- **Rule:** The human experiment's bar is judged exactly as stated: the hybrid beats the random control on first-drink day AND on median survival across at least 5 seeds, measured by the three-arm harness. A tie on either half is not a pass, and a pass on one half is not a pass.
- **Numbers:** At least 5 seeds, 3 arms (population, no_planner, random), 5 days per run; the judgement records first-drink day and median survival per arm per seed, with the v4 baseline beside the new numbers.
- **Check:** The bar judgement in the emergence log shows both halves, per seed, with the numbers; if either half fails, the judgement says fail and names the next single change and its falsifier.

**924. The cell bar is judged the same way**
- **Rule:** The cell-scale bar uses the same harness shape as the human bar — learned cells beat random cells on survival AND reproduction across at least 5 seeds — so the two bars can be compared honestly instead of each being judged by its own private rule.
- **Numbers:** At least 5 seeds at cell scale; survival and reproduction per arm per seed; the first-reproduction day recorded as the cell-scale analogue of first-drink day.
- **Check:** The cell bar judgement records both halves per seed in the testing report, and a comparison note states whether the cell bar and the human bar agree or disagree, with the numbers for both.

**925. Complexity grew, measurably**
- **Rule:** The proof shows the complexity curve across the whole arc — soup, cells, bodies, animals, humans — computed with one stated metric, so growth is a measured line, not a story about progress. The metric and its formula are written down before the curve is drawn.
- **Numbers:** Complexity recorded at the end of each phase (Phases 1–9) with the same metric; the curve shows start, end, and the fastest and slowest growth phases.
- **Check:** The complexity record in the research log lists the metric formula, the value at each phase gate, and the test that computes it; re-running the computation from the archived logs reproduces the same values.

**926. Diversity is counted, not claimed**
- **Rule:** The proof counts species that ever lived, species alive at the end, and extinctions with their causes, all identified by the recorded species criterion — reproductive isolation OR genetic distance beyond a measured threshold. Diversity is a count from the lineage tree, not an impression from watching.
- **Numbers:** Total species ever, living species at the end, extinction count and causes, and the most and least diverse phases, each with its numbers, from at least 5 seeds where the measurement is per-seed.
- **Check:** The species record's counts match a recount from the archived lineage tree; the threshold used is the one Freebuff proposed and Muse reviewed, recorded with its date.

**927. Discoveries are real, not placed**
- **Rule:** The proof lists what inhabitants discovered — fire, tools, materials, new species, new land — and applies the Discovery Principle test to each one: could the owner have predicted it? If yes it was placed; if no it was discovered. Only discoveries that pass the test count as discoveries in the proof.
- **Numbers:** Every claimed discovery lists its phase, generation, discoverer, and the pre-run prediction list it was checked against; the proof counts discovered items and placed items separately.
- **Check:** The discovery-test result in the emergence log judges each claimed discovery against the prediction lists recorded before its phase ran; zero items are counted as discovered that appear on a prediction list.

**928. Human-level means all four tests**
- **Rule:** A mind counts as human-level only when all four tests pass: the full hybrid mind at human scale (neural core, forward model, episodic memory, planner cut), hands able to use tools, social cognition and communication, and passing the human-scale survival bar in a diagnostic run. Three out of four is not human-level, and no single impressive behaviour substitutes for a missing test.
- **Numbers:** Four tests, each pass or fail with its number; the diagnostic survival run uses the same bar as topic 923 across at least 5 seeds.
- **Check:** The human-level record lists all four tests with their results and numbers; if any test fails, the record says the mind is not yet human-level and names which test failed.

**929. The origin bar still stands**
- **Rule:** The proof re-states the protocell life criterion — all six tests (origin, replication, compartment, metabolism, variation, selection) passing 3 out of 3 seeds with clean controls — as the origin bar the whole arc stands on. If the origin bar ever fails on re-check, the arc's foundation is questioned, not patched over.
- **Numbers:** Six criteria, 3 validation seeds (20261105, 20261106, 20261107), 8,000 ticks each; selection needs the main arm's final mean GC fraction to exceed the neutral control's by at least 0.10 in at least 2 of 3 seeds.
- **Check:** The proof cites the validation table (first catalyst, first replication, generation, GC difference per seed) and confirms the no-catalysis control still shows zero catalysed births; any re-run reproduces the same verdict.

**930. The proof is one document**
- **Rule:** All of the proof — the 12 conditions, the arc, the bars, the complexity curve, the species count, the discoveries, the human-level tests, and the origin bar — is gathered into one proof document with a date, so the start's verdict can be read in one place and re-checked line by line.
- **Numbers:** One document in the repo, dated, listing each condition with its pass mark, its measured number, and a link to the underlying log, report, or archive.
- **Check:** An outside reader follows the links from the proof document and reaches the raw measurement for every condition; any condition whose link is broken or whose number cannot be found is marked unproven, not passed.

### 10.4 The falsifiers

**931. The hybrid bar has a falsifier**
- **Rule:** The human success bar is a falsifier, not a hope: if the hybrid does not beat the random control on first-drink day AND median survival across at least 5 seeds, the hybrid-first claim is false, and the next step is a diagnosis with one single change and its own falsifier.
- **Numbers:** At least 5 seeds; the bar fails if random wins or ties either half on the median; the v4 numbers (learned 20/18 survivors, random 32) stand as the last measured failure.
- **Check:** The bar judgement states pass or fail with both halves' medians; a fail entry names the next single change, its falsifier, and the date of the re-run, and the old failure stays in the record.

**932. The cell bar has a falsifier**
- **Rule:** The cell-scale bar falsifies the same way: if learned cells do not beat random cells on survival AND reproduction across at least 5 seeds, the cell calibration is not done, and the failure is recorded with the diagnosis and the next single change. A cell mind that cannot beat random has not learned anything worth building on.
- **Numbers:** At least 5 seeds; both halves (survival, reproduction) must favour the learned arm on the median; the first-reproduction day is recorded per arm as the early signal.
- **Check:** The cell bar judgement in the testing report shows both halves per seed; a fail names the next single change and its falsifier, and no later phase claims the cell bar passed.

**933. The pure-neural track has a falsifier**
- **Rule:** The pure-neural research track stands or falls by its own falsifier: pure neural beats random on first-reproduction day AND median survival across at least 5 seeds, or hybrid-first stands. The track is research only and never becomes the population default by drifting — only by passing this test.
- **Numbers:** At least 5 seeds at the few-neuron rung; both halves must favour pure neural on the median; the comparison records hybrid and random beside it.
- **Check:** The research-track record states pass or fail with the numbers per arm; a fail leaves hybrid-first in place, and the falsifier result is submitted to Muse for review with the date recorded.

**934. The pilot falsifiers stay on the record**
- **Rule:** The primordial soup pilot's falsifiers stay live as the arc's earliest tests: cells must survive, reproduce, and measurably increase in complexity over the planned generations, with the stall-guard and niche measures reading off population-normalised clocks, not the broken deepest-chain clock that froze the first pilot runs.
- **Numbers:** Pilot re-runs use 2,000 turnovers as the target with a 1,000-turnover floor; the niche criterion reads median lineage patch-share entropy at the final generation against the generation-100 value.
- **Check:** The pilot record shows the falsifier verdict per seed with the turnover counts; the stall-guard fix is verified by a run in which the guard fires only when the population-normalised clock truly stalls.

**935. Complexity has a falsifier**
- **Rule:** The claim that complexity grows is falsified if the stated complexity metric is flat or falling across the arc's phase gates, or if the metric can be inflated without doing more. A flat curve is a negative result, not a reason to pick a friendlier metric.
- **Numbers:** The metric is fixed before the arc runs; an increase counts only if the end-of-arc value exceeds the start by more than the seed-to-seed spread across at least 5 seeds.
- **Check:** The complexity record shows the metric value at each phase gate with the seed spread; a flat or falling curve is recorded as a failed falsifier with the next single change, and the metric is not changed mid-arc without recording the change.

**936. Speciation has a falsifier**
- **Rule:** A claimed new species is falsified if the two populations can still reproduce together (no reproductive isolation) AND their genetic distance sits below the measured threshold — both halves of the criterion must be checked, because the criterion is an OR: either half passing is enough, but neither passing means no species.
- **Numbers:** The genetic-distance threshold is the value Freebuff proposed and Muse reviewed, recorded with its date; isolation is tested by attempted reproduction between the populations.
- **Check:** Each claimed speciation event lists the isolation test result and the measured genetic distance against the threshold; an event failing both is removed from the species count with the removal recorded.

**937. The unaware start has a falsifier**
- **Rule:** The claim that inhabitants start unaware of each other is falsified if any inhabitant can sense a peer at the moment the run starts. First contact measured in seconds is the test.
- **Numbers:** Minimum house gap above 15 m on every seed (v5 measured 33.7 m); first contact reported in seconds from run start, not days, because at 128 m and about 1 m/s a 33 m gap closes in seconds.
- **Check:** The run record shows the minimum house gap per seed and the first-contact time in seconds per seed; a first contact at 0 seconds fails the unaware start and triggers a placement fix, never a peer-range shrink.

**938. The planner cut has a falsifier**
- **Rule:** The planner stays cut unless a new steering idea passes its own falsifier: a research arm with the new steering must beat the no-planner arm on survival across at least 5 seeds, with the planner's interventions counted. The v4 evidence (4,493 interventions, no separation) is the reason it was cut, and only a measured separation brings it back.
- **Numbers:** At least 5 seeds; the steering arm must beat the no-planner arm on median survival; planner uses are counted per run and reported beside the survival numbers.
- **Check:** Any proposal to restore the planner lists its falsifier before the run, and the run record shows the survival medians and intervention counts; no separation means the cut stands and the proposal is recorded as failed.

**939. The photoreal bar has a falsifier**
- **Rule:** The visual bar is falsified by the eye-level test: if a reviewer cannot distinguish water from food from fire from shelter from peers in an eye-level screenshot, the bar is not met, whatever rendering features are claimed. A stylised picture that cannot be told apart from a drawing fails, and the failure is recorded, not argued away.
- **Numbers:** Five eye-level positions in Town 1; each screenshot must pass the distinguish test for all five elements; the review is done by a person who did not build the picture.
- **Check:** The five screenshots and the reviewer's verdict per element are filed with dates; any failed element names the fix and the date of the re-review, and the bar is not claimed met until all five pass.

**940. A discovery has a falsifier**
- **Rule:** Every claimed discovery is falsified if it appears on the pre-run prediction list — if the owner could have predicted it, it was placed, not discovered — or if it was produced by a script or a placed object. The test is applied before the discovery is celebrated, not after.
- **Numbers:** Prediction lists are written and dated before each phase runs; each claimed discovery is judged against the list for its phase, and the judgement is recorded per discovery.
- **Check:** The discovery-test record shows the prediction list, the discovery, and the judgement for each item; any discovery that matches a prediction is re-labelled as placed, and the count of true discoveries is corrected in the proof.

### 10.5 The record

**941. The consciousness record gets a definition**
- **Rule:** The consciousness record is a record of observations about understanding forming — what was seen, when, in which species, and by what measure — and it starts with a written definition of what counts as an observation of understanding. The definition is decided by Muse and recorded with its date, because without a definition the record would be a pile of impressions.
- **Numbers:** One definition, dated, in the research log; observations are recorded at each phase gate (cells, bodies, animals, social life, human minds) with generation and species.
- **Check:** The record shows the definition, the date Muse decided it, and at least one observation per phase gate filed under it; any observation that does not fit the definition is filed separately as an open question, not as evidence.

**942. The emergence log is the running record**
- **Rule:** The emergence log records every research question, hypothesis, experiment, result, limitation, and next step in order, with the contributing agent and the date, so no finding is ever rediscovered by accident and no decision is ever made twice from scratch. New entries go on top of the old ones; old entries are never edited to match new results.
- **Numbers:** Every entry carries a date, a question, evidence, results, and limitations; the log is updated within 7 days of any measured result.
- **Check:** The log lists entries E-001 onward with no gaps in numbering and no entry rewritten after its date; a spot check of 5 entries finds each one's evidence in the testing report or the repo.

**943. The testing report holds the numbers**
- **Rule:** The testing report holds every measured number — harness results, tick rates, bar judgements, validation passes, costs — with the seed list, the date, and the version of the code that produced them. It is the place a sceptic goes to check a claim, and a claim with no entry there is an unproven claim.
- **Numbers:** Every run entry lists seeds, arms, days, population, world size, tick rate, and the measured outcome; the report is updated within 7 days of any run.
- **Check:** Pick 5 numbers cited anywhere in the proof and find each one in the testing report with the same value, seed list, and date; any number that cannot be found is struck from the proof until it is filed.

**944. The historical record keeps every lineage**
- **Rule:** The historical record keeps every inhabitant, species, body, and lineage that ever lived — ancestors back to the first cell — even after death or extinction, so history is a complete tree, not a list of survivors. A lineage query given any inhabitant returns its ancestors to generation 0, and a species query given any generation lists the living species then.
- **Numbers:** Lineage queries answer within 5 seconds for any inhabitant; the record covers 100% of species that ever lived, living and extinct.
- **Check:** Run the lineage query on 10 inhabitants and the species query on 5 generations, and confirm every answer matches the run logs; a missing ancestor or a missing extinct species fails the check.

**945. Death is permanent in the record**
- **Rule:** Every death is recorded with its cause, tick, and time, and the dead stay dead — no revival, no reset, no reuse of a dead inhabitant's agent for a new life. The historical record keeps the dead inhabitant's lineage, memory, and contributions, because a world where the dead vanish has no history.
- **Numbers:** 100% of deaths logged with cause and tick; zero revivals across the whole arc, verified by a check that no agent identifier appears alive after its recorded death tick.
- **Check:** Audit the death log against the world state: every logged death matches a dead inhabitant, every dead inhabitant appears in the log, and no identifier reappears alive after its death tick.

**946. Negative results are kept, not hidden**
- **Rule:** Every negative result — pilot failures, bar failures, stalled evolution, a falsifier that failed — stays in the record with what it taught and the next single change it produced. A negative result is never deleted, relabelled as a success, or left out of the proof, because the record of what did not work is what keeps the next attempt honest.
- **Numbers:** The negative-results list covers the whole arc with a date per item; every item links to its emergence-log entry and its falsifier.
- **Check:** The list is compared against the emergence log and the testing report; every fail in either appears on the list, and zero items on the list are described as successes anywhere in the proof.

**947. Firsts are recorded as firsts**
- **Rule:** Every first — first replicator, first catalyst, first body, first species split, first fire, first tool, first contact, first teaching, first skill that outlived its originator — is recorded once, with its generation, tick, time, and the inhabitant or lineage involved, so the arc's milestones are dated facts, not legends that drift.
- **Numbers:** Each first lists generation, tick, sim time, and the individuals involved; the firsts list is updated within 7 days of any new first.
- **Check:** Pick 5 firsts from the list and confirm each one against the run log at the recorded tick; a first that cannot be found in the log is removed from the list with the removal recorded.

**948. The archive format is written down**
- **Rule:** Every archive — seeds, logs, results, checkpoints, and the code version that made them — follows one written format recorded in the repo, so any run can be found, opened, and re-run years later without the person who made it. The format says where each piece lives and how the pieces link together.
- **Numbers:** One format document in the repo; every phase's archive follows it, with the seed list, the log location, the result location, and the code version recorded per run.
- **Check:** Take 3 archived runs at random, follow the format document to find their seeds, logs, and results, and confirm all three are present and complete; any missing piece fails the archive.

**949. Sign-off follows a chain**
- **Rule:** Each phase's record is submitted to Muse for sign-off, the sign-off is recorded with its date, and the sign-off is noted in the agent communication file, so every phase closes with a named decision by a named person on a named date. No phase is treated as done on Freebuff's word alone or on Muse's word alone — the record and the review are both filed.
- **Numbers:** One sign-off per phase, dated, with the record it covers named; the communication file carries the date of each sign-off.
- **Check:** The sign-off list shows 10 phases, each with a dated Muse sign-off and a matching communication-file entry; any phase without both is listed as unsigned, not done.

**950. The record survives checkpoint and resume**
- **Rule:** The logs, the lineage tree, the species record, and the historical record all survive a checkpoint and a resume intact — no birth, death, first, or lineage link lost when the world stops and starts again. The record is part of the world state that gets checkpointed, not a side file that gets rebuilt from memory.
- **Numbers:** Checkpoint and resume tested at every scale; after a resume, the record's event count matches the pre-stop count exactly, with zero missing or duplicated entries.
- **Check:** Stop the world mid-run, resume from the checkpoint, and compare the full record before and after: event counts, lineage links, and firsts all match exactly, and the check is recorded with its date.

### 10.6 The science

**951. Results are pre-registered**
- **Rule:** Before a run that judges anything, the question, the success criterion, the falsifier, the seeds, and the arms are written down and dated, so the bar cannot move after the numbers arrive. A criterion changed after seeing the results is a new experiment, not a pass, and it is recorded as one.
- **Numbers:** Every judged run has a pre-registration entry dated before the run starts, listing the criterion, the falsifier, the seed list, and the arms; at least 5 seeds per judged run.
- **Check:** For 5 judged runs, confirm the pre-registration date precedes the run date and the judged criterion matches the registered one word for word; any mismatch is recorded as a protocol breach.

**952. Every claim has a control**
- **Rule:** Every measured claim runs beside a control that could have produced the same result without the thing being claimed: a random control for learning, a neutral control for selection, a no-catalysis control for replication. A result with no control is an observation, not evidence, and is labelled as one.
- **Numbers:** Learning claims use the random arm; selection claims use the neutral control with the same seed and horizon; replication claims use the no-catalysis control, which must show zero catalysed births.
- **Check:** Each claim in the testing report names its control and the control's result beside it; any claim without a control is marked unproven until a controlled run is filed.

**953. Results replicate across seeds**
- **Rule:** No result counts until it holds across at least 5 seeds, because a single seed can flatter any idea. The seed list is published with the result, the per-seed numbers are shown (not just the median), and a result that holds on 1 seed and fails on 4 is a failure, not a promising start.
- **Numbers:** At least 5 seeds per judged result; per-seed numbers published; a pass needs the median to favour the claim and at least 4 of 5 seeds to point the same way.
- **Check:** The testing report shows per-seed numbers for every judged result; any result published from fewer than 5 seeds is marked preliminary and does not enter the proof.

**954. Same seed, same world**
- **Rule:** The simulation is deterministic per seed: the same seed, the same code, and the same starting conditions produce the same run, so any result can be re-run and checked by someone else. Randomness comes only from the seeded random-number state, which is part of the checkpoint.
- **Numbers:** Determinism checked by re-running 3 seeds and comparing state digests tick by tick; digests must match exactly for at least 1,000 ticks.
- **Check:** Re-run 3 archived seeds and confirm the state digests match the originals exactly; any mismatch is recorded as a determinism failure with the code version that caused it.

**955. Mass and energy are conserved**
- **Rule:** Total mass and total energy in the world are conserved within a documented numerical error at every scale, so the world never creates food, fuel, or life from nothing. A conservation check runs as part of every validation suite, and its error is published, not assumed to be zero.
- **Numbers:** Conservation error under 0.1% of total mass and total energy per 1,000 ticks at cell, body, and human scales; the error is recorded per run.
- **Check:** The validation suite reports the conservation error for each scale; any run whose error exceeds 0.1% fails validation and is fixed and re-run before its results are used.

**956. Ablations separate causes**
- **Rule:** When a component is claimed to help — a forward model, episodic memory, a social drive, a steering rule — an ablation run with that component off measures whether the claim is real. If the arm with the component and the arm without it do not separate, the component does no measurable work, whatever its design promises.
- **Numbers:** Ablations use the same seeds, arms, and days as the main run (at least 5 seeds, 5 days at human scale); separation needs the median to favour the component arm.
- **Check:** Every component claim in the testing report links to its ablation run with both arms' medians; a claim whose ablation does not separate is recorded as unproven and the component is cut or re-designed.

**957. Seed noise is measured, not ignored**
- **Rule:** Differences smaller than the seed-to-seed spread are treated as noise, not as findings. Every comparison reports the spread across seeds beside the median, and a 3-survivor difference across 5 seeds — the size of the v5 planner difference — is reported as inside noise, not as a win.
- **Numbers:** Every comparison lists the median, the range, and the per-seed values; a difference counts as real only if it exceeds the seed spread and holds on at least 4 of 5 seeds.
- **Check:** The testing report shows the spread beside every median; any claim of a win that sits inside the reported spread is corrected in the record with the correction dated.

**958. Metrics never change mid-run unrecorded**
- **Rule:** The metric that judges a run is fixed before the run and stays fixed through it. If a metric must change — a broken clock, a gameable measure — the change is recorded with the old value, the new value, the reason, and the date, and every result judged under the old metric is re-judged or marked as judged under the old metric.
- **Numbers:** One metric version per run, recorded with the run; any change creates a new version number and a dated entry in the research log.
- **Check:** The metric version in each run's record matches the version in the pre-registration; any run whose metric changed mid-run without a dated entry is marked invalid and re-run.

**959. Review is part of the method**
- **Rule:** Freebuff builds and measures, Muse reviews and judges, and neither step counts without the other: a result is filed by the builder with its numbers, then reviewed by Muse with the review recorded and dated. A contradiction between a result and an earlier decision stops work around it until Muse rules on it.
- **Numbers:** Every judged result has a builder entry and a dated Muse review; contradictions are raised within 7 days of discovery and recorded in the communication file.
- **Check:** The review list shows a dated Muse review for every judged result in the testing report; any result without a review is marked unreviewed and does not enter the proof.

**960. Re-running reproduces the result**
- **Rule:** Any archived run can be re-run from its seed and its code version to reproduce its result, so a claim can be checked by re-doing the work, not just by re-reading the report. Reproducibility is tested on a schedule, not assumed from determinism alone, because archives rot and code drifts.
- **Numbers:** Reproducibility tested on at least 3 archived runs per phase, on a different machine or environment where one is available; a reproduced result must match the original within the seed spread.
- **Check:** The reproducibility log lists the re-run results beside the originals for 3 runs per phase; any run that does not reproduce is recorded as a failure with the fix and the re-run date.

### 10.7 The world keeps growing

**961. Towns 2–5 seed from Town 1**
- **Rule:** Once Town 1's survival bar is judged, the same town structure — 5 inhabitants, 5 houses, gaps above the 15 m peer range, starting unaware — seeds Towns 2–5, one per country. Each new town is judged by the same bar.
- **Numbers:** Towns 2–5 start one at a time, each with 5 inhabitants and 5 houses in a 128 m locale; a town is seeded only after the previous town's bar is judged.
- **Check:** Each new town's record shows its seed date, its house gaps (all above 15 m), its first-contact time in seconds, and its bar judgement; a town seeded before the previous bar was judged is flagged as a sequencing breach.

**962. Countries 2–5 open in order**
- **Rule:** The planet holds 28 countries and populations start in 5 of them, one town per country, A country opens only when its town is seeded, and the "start unaware" rule applies between towns too.
- **Numbers:** 5 countries with towns at the end of scale-out, 23 countries unopened; inter-town contact is measured the same way as first contact inside a town, in seconds from the moment contact becomes possible.
- **Check:** The planet record lists the 5 opened countries with their town seed dates and the 23 unopened ones; any contact between towns is logged with its time and the towns involved, and no town's record claims knowledge of another before that logged contact.

**963. The planet's state is published**
- **Rule:** The planet's state — 28 countries, which 5 hold towns, each town's population, each town's status — is published on the Command Center and updated from the Gateway, so the scale of the world is always a measured fact, not a map with invented towns. Unopened countries are shown as unopened, not as empty land waiting to be filled by hand.
- **Numbers:** 28 countries, 5 towns maximum at this stage; the planet view updates at least once every 5 seconds from the Gateway, with each town's population and status dated.
- **Check:** The planet view's country and town counts match the Gateway snapshot for the same tick; an audit finds zero towns shown that have no Gateway record behind them.

**964. New land is generated, not built**
- **Rule:** As inhabitants explore beyond a locale, new land appears by procedural generation from the same rules that made the first land, so the world grows without anyone placing terrain, rivers, or resources by hand.
- **Numbers:** New land generates in 128 m locales from a recorded seed; the generation rule and its seed are filed per locale, and generated land must pass the same conservation and determinism checks as the first locale.
- **Check:** Generate 3 new locales from their seeds, re-generate each from the same seed, and confirm the terrain matches exactly; confirm no resource in a new locale was placed by hand by checking it against the generation rule.

**965. The ceiling is re-measured at each scale**
- **Rule:** Every time the world grows — a new town, a new country, a larger population — the population ceiling is measured again on the new host load, because a ceiling measured for one town says nothing about five. The number the world can hold is always the latest measurement, and the old number is kept beside it as history.
- **Numbers:** Ceiling re-measured after each town is seeded, using the same budget as topic 908 (at least 100 ticks per second, checkpoint under 60 seconds) held for 24 hours.
- **Check:** The ceiling log shows one measurement per scale with its date, tick rate, and checkpoint duration; the published ceiling is always the latest measurement, and the site never shows an older ceiling as current.

**966. Scale-out never breaks Town 1**
- **Rule:** Growing the world must not change Town 1's rules, reset its inhabitants, or rewrite its history. Town 1 keeps running on its own locale with its own lineage while new towns start elsewhere, and a regression test proves Town 1 still behaves as it did before the growth.
- **Numbers:** After each scale-out, Town 1's tick rate, population, and bar numbers are re-measured and compared against the pre-growth values; the comparison allows only the seed spread as drift.
- **Check:** The post-growth check for Town 1 shows its population, tick rate, and survival numbers within the seed spread of the pre-growth values, and its lineage query still reaches the first cell with no gaps.

**967. New species keep appearing**
- **Rule:** After the start, evolution keeps running: new species appear by the same criterion (reproductive isolation OR genetic distance beyond the threshold), extinctions keep being recorded, and the species count keeps being measured per generation. The start's proof is a snapshot; the world's diversity is a continuing measurement.
- **Numbers:** Species count and diversity metrics computed per generation and logged; every new speciation event lists its isolation test and genetic distance against the threshold.
- **Check:** The species log shows at least one diversity measurement per generation after the start, and every speciation event recorded after the start carries its isolation result and distance measurement.

**968. Deferred systems unlock in order**
- **Rule:** The systems deferred past the start — weather and seasons, chemistry beyond the soup, genetics, agriculture, trade, writing, animals beyond the arc — each unlock only when its stated condition is met, in the order the plan gives, and each is built as rules, not placed content. Nothing deferred is started early because it looks exciting, and nothing is forgotten because it looks hard.
- **Numbers:** The deferred list names each system with its unlock condition and its order; a system starts only after its condition is measured as met and recorded with a date.
- **Check:** The deferred list shows each system's condition and status; any system started without its condition recorded as met is flagged, and the list is reviewed every 30 days.

**969. The views scale with the world**
- **Rule:** As towns and countries open, the Command Center and World View grow with them — new towns appear on the map, new inhabitants become watchable — without breaking the views that already work. The planet viewer keeps its zoom ladder (planet to individual) and its viewport-only loading, so five towns cost no more to view than one.
- **Numbers:** Each new town appears on the map within 24 hours of seeding; the site's load budget (under 3 seconds, pan under 500 ms) still holds with all 5 towns live.
- **Check:** After each town seeds, the map shows it within 24 hours with its real population from the Gateway, and a load test with all 5 towns live still meets the budgets from topic 919.

**970. Growth never rewrites history**
- **Rule:** Nothing that happens after the start — new towns, new species, new land — changes the record of the start. The arc record, the proof, and the firsts list are frozen as dated documents; later events are recorded as later events, appended after, never edited into the earlier story.
- **Numbers:** The start's records carry their dates and version numbers; any correction to them is a dated amendment that leaves the original text in place, with the reason recorded.
- **Check:** The record's version history shows zero silent edits to the start's documents after their sign-off dates; every amendment is dated, reasoned, and linked from the original.

### 10.8 The plan is a living document

**971. The plan has versions, not silent edits**
- **Rule:** The plan is versioned — v1, v2, v3, and so on — and each version is a complete dated document kept in the repo. A change to the plan creates a new version with a note saying what changed and why; the old version stays readable, so nobody can rewrite the past by editing the plan.
- **Numbers:** Every version is numbered, dated, and stored; the change note for each version lists the tasks changed, added, or corrected, with the decision behind each change.
- **Check:** The repo holds v1, v2, and v3 as separate dated files; the v3 change note accounts for every difference from v2, and no version file has been edited after its date.

**972. Contradictions stop work until ruled on**
- **Rule:** If a measured result contradicts an earlier assumption or decision, work around the contradiction stops and the contradiction is brought to Muse before continuing. Working around it silently — retuning, redefining, or skipping the awkward task — is forbidden, because a plan that absorbs contradictions without noticing them stops being a plan.
- **Numbers:** Contradictions are raised within 7 days of discovery, recorded in the communication file with the evidence, and ruled on by Muse with a dated decision before the affected work resumes.
- **Check:** The contradiction log lists every raised contradiction with its date, evidence, and Muse's ruling; a spot check finds no task completed in the affected area between the contradiction date and the ruling date.

**973. A task that cannot be done says so**
- **Rule:** If a task cannot be done as written, the record says why and what was done instead — never deleting the task, never silently doing something else. The plan is a record of what was done, not a wish list, and an honest "could not be done, here is why" keeps it true.
- **Numbers:** Every uncompleted task carries a dated note with the reason and the replacement action; the note is filed in the testing report or the emergence log within 7 days.
- **Check:** The plan's task list is audited against the record; every task is done, in progress with a date, or marked undone with a reason — zero tasks are silently missing.

**974. Decisions are recorded with dates**
- **Rule:** Every decision — architecture, thresholds, cut conditions, scale-out, sign-offs — is recorded with who decided it, when, on what evidence, and where the full text lives. A decision with no date and no evidence is a rumour, and a rumour cannot be reviewed, reversed, or relied on.
- **Numbers:** Each decision entry lists the decider, the date, the evidence (log entry or run), and the location of the full text; decisions are recorded within 7 days of being made.
- **Check:** The decision list is audited against the emergence log and the communication file; every decision in the plan traces to a dated entry, and zero decisions in the plan have no dated source.

**975. Open items stay open until closed**
- **Rule:** Items left open by design — the consciousness record definition, a threshold to be set by measurement, a rendering path to be chosen — stay on an open-items list with an owner and a condition for closing, and the list is reviewed until every item is closed or honestly carried into the next version. An open item never quietly disappears.
- **Numbers:** The open-items list names each item, its owner, and its closing condition; the list is reviewed every 30 days and any item open longer than 90 days gets a dated note explaining why.
- **Check:** The open-items list matches the plan's flagged items one for one; every item closed since the last review links to the measurement or decision that closed it.

**976. The plan is reviewed on a schedule**
- **Rule:** The plan is reviewed on a fixed schedule — after each phase closes and at least once every 30 days while work is active — by Muse against the measured record, so drift between the plan and reality is caught while it is small. A review records what matches, what drifted, and what changes, with dates.
- **Numbers:** Review every 30 days and at every phase close; each review is a dated entry naming the reviewer, the drift found, and the changes made.
- **Check:** The review log shows a dated review within 30 days of every phase close and no gap longer than 30 days during active work; each review's drift list is empty or has a dated fix.

**977. Each version hands over cleanly**
- **Rule:** When a new plan version lands, it states what the previous version left done, what it left open, and what the new version changes, so the next person to pick up the work starts from the true state, not from a guess. The handover is written, not assumed, and it names the files where the evidence lives.
- **Numbers:** Every version carries a handover note listing completed phases, open items, and the evidence locations; the note is written before the version is sent to Freebuff.
- **Check:** The v3 handover note lists the phases done under v2, the open items carried over, and the evidence files; Freebuff's acknowledgement of the handover is recorded with its date.

**978. The deferred list is maintained**
- **Rule:** The deferred list — Towns 2–5, weather and seasons, chemistry beyond the soup, genetics, agriculture, trade, writing — is kept current in the plan, with each item's unlock condition and status, so deferred work is waiting, not forgotten. The list is part of every version, not an appendix that gets dropped.
- **Numbers:** The list names each deferred item with its unlock condition; it is reviewed every 30 days and updated within 7 days of any unlock condition being met.
- **Check:** The deferred list in the current version matches the list in the previous version plus dated changes; every item whose condition was met has a dated status change and a start record or a reason it has not started.

**979. No edit is silent**
- **Rule:** No change to the plan, the record, the proof, or the decision list is ever made without a dated note saying what changed, who changed it, and why. Silent edits — a number quietly corrected, a failed test quietly removed — destroy trust in every other number, so the rule is absolute even for small fixes.
- **Numbers:** Every edit carries a date, an author, and a reason; corrections to numbers keep the old value visible beside the new one with the reason for the change.
- **Check:** The version history of the plan and the record shows a dated note for every change; a spot check of 10 changes finds the author and reason for each, and zero changes lack a note.

**980. The plan mirrors the repo**
- **Rule:** The plan describes what is actually in the repo — the code, the logs, the archives, the documents — When the two disagree, the repo is the truth and the plan is corrected to match it, with the correction dated.
- **Numbers:** The plan's file references are checked against the repo every 30 days; every referenced file must exist at the referenced path, and every major repo addition must appear in the plan within 30 days.
- **Check:** An audit lists every file the plan references and confirms each exists; it also lists the repo's major additions since the last audit and confirms each is mentioned in the plan, with zero missing on either side.

### 10.9 The goal

**981. The goal, stated plainly**
- **Rule:** The goal is a persistent simulated world that starts from single cells and, by evolution, reaches human-level minds and a civilisation of its own — a world that runs 24/7, where inhabitants discover things even the owner did not place, and where understanding itself is the thing being watched. The goal is stated in plain words.
- **Numbers:** One goal statement, dated, in the plan; it names the start, the destination, and the conditions.
- **Check:** The goal statement in the plan matches the goal as Alex stated it, and every condition in the proof document traces to a phrase in the goal statement; any proof condition with no goal phrase behind it is flagged.

**982. Starting at zero is honoured**
- **Rule:** The start honoured zero: bodies, senses, drives, a world with water, food, and materials, and minds that learn — nothing of tools, fire, language, knowledge, or social structure, except the 5 honestly labelled houses as shelter. The goal is judged against this: if the inhabitants were given anything else at the start, the start was not zero.
- **Numbers:** The starting-condition list names exactly what was given (bodies, senses, drives, world, learning minds, 5 houses) and nothing else; any other starting condition found in the record is a breach.
- **Check:** The starting-condition list is audited against the simulation's initial state; the audit finds zero tools, zero fire, zero language, and zero knowledge present at time zero beyond the listed items.

**983. The Discovery Principle is honoured**
- **Rule:** The goal is honoured only if the world was built by rules, not things: evolution makes new species, chemistry makes new materials, procedural generation makes new land, and physics stays fixed throughout. A world where the good discoveries were placed fails the goal even if it looks impressive.
- **Numbers:** The discovery-test result counts discovered versus placed items across the arc; the goal needs at least one discovery per phase that passes the test, and zero placed items counted as discoveries.
- **Check:** The discovery-test record shows the per-phase counts; the goal check confirms at least one true discovery per phase and zero placed items in the discovered count.

**984. One mind for every inhabitant**
- **Rule:** The goal holds one hybrid mind for every inhabitant — neural core, forward model, episodic memory, planner cut — the same architecture at every scale, sized to the organism. No brain-dead tier, no separate mind for the favoured few, no LLM-only inhabitants anywhere in the population.
- **Numbers:** 100% of inhabitants run the one architecture; the planner flag is False in every population arm at every scale; zero LLM-only inhabitants exist.
- **Check:** An audit of the population code and the run configurations confirms the same architecture for every inhabitant, planner off everywhere in the population, and zero LLM-only agents; any exception is recorded as a breach with its fix.

**985. The world runs without end**
- **Rule:** The goal is a world that runs 24/7 with no time limit — not a 5-day experiment that ends, not a demo that stops when the audience leaves. The 5-day human run and the bounded pilot were tests with ends; the world itself has no end, and its inhabitants get unlimited time to evolve.
- **Numbers:** The world has run continuously for at least 30 days at the time the goal is judged, with uptime at least 99% per 30-day window and every stop logged.
- **Check:** The uptime log shows at least 30 days of continuous running at 99% or better, and the incident log accounts for every gap longer than 60 seconds in that period.

**986. Inhabitants discover what the owner did not know**
- **Rule:** The goal is met in spirit only when inhabitants have discovered something the owner could not have predicted — a species, a material, a technique, a piece of land — proving the world can surprise its maker. A world that only ever does what was expected of it is a model, not a world.
- **Numbers:** At least 3 discoveries across the arc that pass the Discovery Principle test and that no prediction list foresaw, each with its phase, generation, and discoverer recorded.
- **Check:** The discovery-test record lists at least 3 such discoveries with their prediction lists beside them; each one is confirmed absent from every prediction list written before its phase.

**987. Understanding is the thing being watched**
- **Rule:** The goal's first step is an understanding-consciousness exercise: starting at zero is what makes understanding itself the thing being watched, from the first gradient-following cell to the first human-level mind. The consciousness record is the evidence for this half of the goal, and it is judged by its definition, never by how convincing the behaviour looks.
- **Numbers:** The consciousness record holds at least one observation per phase gate under Muse's definition, with generation and species for each.
- **Check:** The consciousness record is reviewed against its definition; every observation fits the definition, and the review states plainly what the record does and does not establish about understanding.

**988. Civilisation is earned, never scripted**
- **Rule:** The goal's destination — civilisation — is earned step by step (survive, fire and tools, language and society, agriculture and towns, trade and writing), each step discovered by the inhabitants through the rules. No step is given, scripted, or placed, and the ladder's order is the proof that each step was earned.
- **Numbers:** The ladder lists 5 rungs in order; each rung reached is dated with the discovery that reached it, and no rung is claimed before the rung below it is dated.
- **Check:** The ladder record shows each rung's date and discovery in order; any rung claimed out of order, or without a dated discovery, is struck until the evidence is filed.

**989. The world is Earth-like, under real rules**
- **Rule:** The goal's world is a regular world like Earth — a planet in a solar system, under this universe's rules, with the same physics and chemistry as real life and nothing invented. Day and night come from rotation, seasons from tilt and orbit, life starts in water, and animals arrive through evolution, not placement.
- **Numbers:** The planet frame states the solar geometry (latitude 35°, dawn start 06:20), the 28 countries, and the fixed physics and chemistry rules; no rule in the world contradicts a real physical or chemical law.
- **Check:** The planet design document and the simulation's rule list are compared; every rule traces to a real physical or chemical law, and zero rules invent new physics — any invented rule found is recorded as a breach.

**990. The goal is checked against the proof**
- **Rule:** The goal is not declared met by feeling; it is checked line by line against the proof document, and the check is written down with a date. Each phrase of the goal gets its evidence, and any phrase with no evidence is an open gap, not a quiet omission.
- **Numbers:** The goal check lists every phrase of the goal statement with the proof condition that covers it; the check passes only when every phrase has evidence and every proof condition traces to a phrase.
- **Check:** The goal-check document shows all phrases covered with links to the proof; zero phrases lack evidence, and any gap found is dated and assigned an owner and a closing condition.

### 10.10 The start is perfect

**991. The closing numbers are gathered**
- **Rule:** The closing record gathers the arc's final numbers in one place: total generations from the first replicator to the first human-level mind, total species ever and living, extinctions with causes, discoveries, firsts, the bar judgements, tick rates, and costs — each number cited to its source, so the start's scale can be read at a glance and checked in detail.
- **Numbers:** One closing table with at least 10 numbers (generations, species ever, species living, extinctions, discoveries, firsts, cell bar, human bar, tick rate, cost), each with its source link and date.
- **Check:** Every number in the closing table is found in the testing report, the emergence log, or an archive with the same value; any number that cannot be found is removed from the table with the removal recorded.

**992. The closing record is written**
- **Rule:** The closing record says what the arc was, what was measured, what was discovered, what failed, and what the world is now ready for — in the emergence log, dated, so the perfect start has a single written ending that anyone can read. It is a record, not a celebration: failures sit beside successes in the same document.
- **Numbers:** One closing entry in the emergence log, dated, covering the arc, the measurements, the discoveries, the negative results, and the next step.
- **Check:** The closing entry is read against the proof document and the negative-results list; every claim in it traces to a filed measurement, and every negative result in the list appears in it.

**993. Muse signs off on the start**
- **Rule:** The closing record is submitted to Muse for sign-off as Chief Architect, and the sign-off is recorded with its date. The sign-off means the proof was checked, the falsifiers were judged, the record is complete, and the start is perfect by the written definition — or it says plainly which condition failed and what happens next.
- **Numbers:** One sign-off, dated, naming the proof document version and the conditions passed; a sign-off with any condition failed is recorded as a conditional sign-off with the failed conditions listed.
- **Check:** The sign-off entry shows the date, the proof version, and the verdict per condition; if the verdict is pass, all 12 proof conditions show pass beside it, and the sign-off is filed in the emergence log and the communication file.

**994. The closing decision is communicated**
- **Rule:** The closing decision is recorded in the agent communication file with its date, so Freebuff and the record both hold the same ending: the start is perfect, or it is not, and what the world is now ready for. The communication file is the shared truth between the two agents, and the closing decision belongs there, not only in one agent's notes.
- **Numbers:** One communication-file entry, dated, stating the verdict, the proof version, and the next step; it is written within 7 days of the sign-off.
- **Check:** The communication file shows the closing entry with the verdict matching the sign-off; a mismatch between the two is flagged as a contradiction and ruled on before any further work.

**995. The archive is complete and re-runnable**
- **Rule:** The full archive — every phase's seeds, logs, results, checkpoints, and code versions — is confirmed complete and re-runnable before the start is closed, because a perfect start that cannot be re-run cannot be checked. The confirmation is a test, not a statement: runs are actually re-run from the archive.
- **Numbers:** At least 3 runs per phase re-run from the archive on a different machine or environment where available, reproducing the original results within the seed spread.
- **Check:** The reproducibility log lists the re-run results beside the originals for 3 runs per phase; every listed run reproduces, and any run that does not is fixed and re-run before the close is recorded.

**996. The next step is stated**
- **Rule:** The closing record states what the world is now ready for — the next phase after the start, whether that is Towns 2–5, the next deferred system, or a new falsifier to chase — with a date and an owner, so the start ends with a direction, not a full stop. The world keeps growing; the start is the foundation, not the finish.
- **Numbers:** One next step named with its unlock condition, its owner, and its start date or its condition for starting; the step comes from the deferred list, not from a new idea invented at closing.
- **Check:** The closing record names the next step and the deferred-list item it comes from; the deferred list shows that item's status changed to started or ready on the closing date.

**997. "Perfect" means the list, all passed**
- **Rule:** "The start is perfect" means exactly this: the 12 proof conditions all passed, the arc is complete from cells to humans, the bars were judged, the falsifiers were faced, the record is complete, and Muse signed off. It does not mean the world is finished, the inhabitants are wise, or nothing will ever fail again — it means the start, as defined, is done right.
- **Numbers:** 12 conditions, all passed; the verdict is written as "the start is perfect" only when the proof document shows 12 passes and the sign-off confirms them.
- **Check:** The proof document is counted: 12 conditions, 12 passes, zero fails, zero unproven; any other count means the verdict is not "perfect" and the closing record says so.

**998. No claim without a measurement**
- **Rule:** The final rule of the start is the first rule of the plan: nothing is claimed done without a measured result. Every sentence in the closing record that claims something carries its number, its source, and its date, and any claim that cannot be measured is written as a question for the next phase, not as an achievement of this one.
- **Numbers:** 100% of claims in the closing record carry a measurement, a source link, and a date; zero claims rest on a feeling, a hope, or an unmeasured impression.
- **Check:** An audit of the closing record checks every claim against its source; any claim without a measurement is struck or rewritten as an open question, and the audit is dated and filed.

**999. The verdict is pass or fail, stated plainly**
- **Rule:** The start's verdict is one of two words — pass or fail — stated plainly in the closing record with the numbers behind it. A fail is not a disaster; it is a measured result that names the next single change and its falsifier.
- **Numbers:** The verdict is one word, dated, with the 12 condition results beside it; a fail names the failed conditions, the next single change per condition, and the falsifier for each.
- **Check:** The closing record shows the verdict word, the 12 results, and — if fail — the next changes and falsifiers; the verdict word matches the count of passes, and any mismatch is corrected in a dated amendment.

**1000. Close the perfect start**
- **Rule:** The perfect start closes with the closing decision recorded in the communication file with its date, stating what the world is now ready for — and the world keeps running. Closing the start does not stop the world, close the views, or end the record; it marks the foundation as done so the next phase can begin on measured ground.
- **Numbers:** One closing decision, dated, in the communication file; the world is confirmed still running (tick count increasing) on the closing date, and both views are confirmed live.
- **Check:** The communication file shows the closing decision with its date and the next step; the Gateway health endpoint on that date shows a live, increasing tick, and both views show live data — the world outlives its own perfect start.
