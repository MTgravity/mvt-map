# mvt-map


The app relies on a local environment file( [example.env](https://github.com/MTgravity/mvt-map/blob/master/example.env) ). 
Chang values as necessary and make sure to rename the file to `.env`.

|Env Var|Ex|Desc|
|--|--|--|
|POSTGRES_USER|`mapnerd`|Database username|
|POSTGRES_PASSWORD|`mapnerd`|Database password|
|POSTGRES_DB|`mapdb`|Database Name|
|MAPBOX_TOKEN|`pk.ey...`|Public Mapbox Access Token|

The webmap utilizes the Mapbox JS API, which requires an access token. Information about setting up a token can be found in the documentation on thier [website](https://docs.mapbox.com/help/getting-started/access-tokens/)
