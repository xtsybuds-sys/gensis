# Retired: cosmogony viewer

`cosmos.html` and `cosmos.js` were the viewer for the reduced cosmogony in
`genesis/cosmos/cosmogony.py`. They were retired from the served world on 2026-11-06.

Why: the scene presented a hand-authored sequence — fixed phase thresholds, a 90-second cycle,
a selected "first world" and a banner — as the origin of the world. That is staging, not
simulation, and it contradicted the project rule that nothing is placed and no story is
scripted.

What remains: the model and its tests stay in the repository as a reduced experiment. They are
not served and must not be presented as the world. `/` serves the live baseline instead.

To run it again for research, serve the file yourself from a local static server; do not wire
it back into the gateway without an explicit decision.
