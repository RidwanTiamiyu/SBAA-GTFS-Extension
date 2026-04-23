# SBAA GTFS-Behavior Extension: Data Dictionary

## Schema Definition: `behavioral_constraints.txt`

This document defines the strict data types and compliance constraints for the behavioral metadata extension. It is engineered to standardize data for federal infrastructure auditing, specifically to support compliance oversight for the **$1.2 Trillion IIJA** mandates.

### Field Specifications

* **`stop_id`**
  * **Type:** String (ID)
  * **Definition:** The unique identifier for a physical transit node.
  * **Relational Mapping:** Foreign key strictly linked to the primary GTFS `stops.txt` file.

* **`slope_gradient`**
  * **Type:** Float (Percentage)
  * **Definition:** The maximum measured topological grade within a 50-foot pedestrian approach radius, derived from Digital Elevation Models (DEM).
  * **Audit Threshold:** Critical for verifying the **8.33% ADA maximum slope** mandate. Values exceeding this limit trigger an automatic compliance failure in the routing logic.

* **`safety_score`**
  * **Type:** Integer
  * **Definition:** A normalized quantitative value ranging from 1 to 10 representing physical crossing security (e.g., presence of crosswalks, traffic speed).

* **`lighting_level`**
  * **Type:** Float
  * **Definition:** The objectively measured nighttime illumination at the physical node, recorded in lumens. This metric is utilized to calculate the workforce vulnerability penalty during off-peak routing.

* **`behavioral_cost`**
  * **Type:** Float (Currency)
  * **Definition:** The calculated algorithmic penalty applied to the node, mathematically simulating the localized out-of-pocket friction or perceived physical cost.

* **`compliance_flag`**
  * **Type:** String (Enumeration)
  * **Definition:** A binary validation flag for federal grant eligibility reporting.
  * **Accepted Values:** `PASS` or `FAIL_ADA_SLOPE`.
