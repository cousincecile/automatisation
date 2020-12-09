case class Artists(
                    id: String,
                    name: String
                  )

case class Playlist(
                     id: String,
                     name: String,
                   )

case class JsonObject(
                       artists: Artists,
                       id: String,
                       name: String,
                       playlist: Playlist,
                       popularity: Double,
                       `type`: String,
                     )