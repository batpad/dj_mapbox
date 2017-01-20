Root: /api/v1/
  - /collections/
    - GET: List all Collections
    - POST: POST a new collection: {"name": "foobar", "description": "blah", "features": []}`

  - /collections/<id>
    - GET: Retrieve single collection
    - PUT: Send entire representation of collection to update

  - /collections/<id>/features
    - GET: Get FeatureCollection for collection. Supports a `bbox` query parameter to filter by bbox.
    - POST: Single `Feature` object: add a Feature to the Collection.

  - /collections/<collection_id>/features/<feature_id>
   - GET: Retrieve single feature
   - PUT: Send full representation of feature to update
   - DELETE: Delete feature