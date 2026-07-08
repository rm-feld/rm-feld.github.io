---
type: dataset-schema
material-source: https://lila.science/datasets/snapshot-serengeti-addendum
modified: 2026-04-07T12:47:21-07:00
created: 2026-04-07T12:44:10-07:00
---
from `raw_data_README.docx`

```
Raw classification data: Classifications made on camera trap imagery by volunteers via the [www.SnapshotSerengeti.org](http://www.SnapshotSerengeti.org) interface. Raw classifications are reported as 1 record per unique user, capture event, and species, and include images retired as “blank.”

·      _CaptureEventID:_ A unique identifier for each capture event and resultant image set.

·      _ClassificationID_: A unique identifier for each classification event (one user classifying a single capture event). If a single user identifies multiple species within a capture event, they share the same classification ID.

·      _UserID_: Unique user ID for logged-in users; sessionID (unique computer & browser information) for non-logged-in users.

·      _Species_: Species selected from a list of 48 options or “blank”

·      _Count_: Number of individuals, estimated as 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11-50 or 51+.

·      _Standing:_ Binary indicator of whether any of the individuals of that species are standing.

·      _Resting:_ Binary indicator of whether any of the individuals of that species are resting.

·      _Moving:_ Binary indicator of whether any of the individuals of that species are moving.

·      _Eating:_ Binary indicator of whether any of the individuals of that species are eating.

·      _Interacting:_ Binary indicator of whether any of the individuals of that species are interacting (both intra- and inter-specific interactions are included).

·      _Babies_: binary indicator of whether young were present for that species.
```

