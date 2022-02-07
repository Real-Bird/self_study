import PropTypes from "prop-types";
import { Link } from "react-router-dom";

function DetailMovie({ medium_cover_image, title_long, runtime, rating, genres, description_full }) {
  return (
    <div>
      <div>
        <nav><Link to="/">Home</Link></nav>
      </div>

      <img src={medium_cover_image} />
      <h1>{title_long}</h1>
      <hr />
      <span>runtime: {runtime} || </span>
      <span>rating: {rating} || </span>
      <span>genres: {genres.map((g) => <span key={g}>◎
        {g} </span>)}</span>
      <hr />
      <h3>Description</h3>
      <p>{description_full}</p>
    </div>
  )
}

DetailMovie.propTypes = {
  medium_cover_image: PropTypes.string.isRequired,
  title_long: PropTypes.string.isRequired,
  runtime: PropTypes.number.isRequired,
  rating: PropTypes.number.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
  description_full: PropTypes.string.isRequired,
}

export default DetailMovie;