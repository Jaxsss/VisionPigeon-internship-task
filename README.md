# VisionPigeon-internship-task

## Description
The task is to parse the data from JSON file and compute:

1. number of unique users in one day
2. number of unique requests (unique = multiple requests of the same item count as one)
3. average time between item_id requests (in the sample data above, the average time between the requests would be 1 minute - computed from the item_id 494398, since the item_id 3147684 was requested only once, so the average would only be computed from )
4. median time between item_id requests (-||-),
5. maximum number of requests per a single item_id for which the variant similarInJsonList was returned.
