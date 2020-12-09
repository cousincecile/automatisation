case class Artists(
                    id: String,
                    name: String,
                  )

case class Album(
                  id: String,
                  name: String,
                )

case class JsonObject(
                      album: Album,
                      artists: Artists,
                      id: String,
                      name: String,
                      popularity: Double,
                     )
