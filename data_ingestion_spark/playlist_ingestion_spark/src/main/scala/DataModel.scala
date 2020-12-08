case class Artists(
                    id: String,
                    name: String
                  )

case class Playlist(
                     playlist_country: String,
                     playlist_id: String,
                     playlist_name: String,
                   )

case class JsonObject(
                       artists: Artists,
                       id: String,
                       name: String,
                       playlist: Playlist,
                       popularity: Double,
                       `type`: String,
                     )