import PropTypes from "prop-types";
import { Link } from "react-router-dom";
function Movie({ id, medium_cover_image, title_long, summary, genres }) {
  return (
    <div>
      <img src={medium_cover_image} />
      <h2>
        <Link to={`/movie/${id}`}>{title_long}</Link>
      </h2>
      <p>{summary}</p>
      <ul>
        {genres.map((g) => <li key={g}>{g}</li>)}
      </ul>
    </div>
  );
}

Movie.propTypes = {
  id: PropTypes.number.isRequired,
  medium_cover_image: PropTypes.string.isRequired,
  title_long: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
}

export default Movie;