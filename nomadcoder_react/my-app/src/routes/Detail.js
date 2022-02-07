import { object } from "prop-types";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import DetailMovie from "../components/DetailMovie";

function Detail() {
  const [detail, setDetail] = useState([]);
  const [loading, setLoading] = useState(true);
  const { id } = useParams()
  const getMovie = async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json();
    setDetail(json.data.movie);
    setLoading(false);
  }
  useEffect(() => {
    getMovie();
  }, [])
  return (
    <div>
      {loading ? <h1>Loading...</h1> :
        <div> {
          <DetailMovie
            key={detail.id}
            medium_cover_image={detail.medium_cover_image}
            title_long={detail.title_long}
            runtime={detail.runtime}
            rating={detail.rating}
            genres={detail.genres}
            description_full={detail.description_full}
            genres={detail.genres} />
        }
        </div>
      }
    </div >
  )
}

export default Detail;