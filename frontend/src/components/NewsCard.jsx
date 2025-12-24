const NewsCard = ({ news }) => {
  return (
    <div className="border rounded-lg shadow-sm p-4 bg-white">
      {news.image && (
        <img
          src={news.image}
          alt={news.title}
          className="w-full h-48 object-cover rounded-md mb-3"
        />
      )}

      <h2 className="text-lg font-semibold mb-2">
        {news.title}
      </h2>

      <p className="text-sm text-gray-600 mb-3">
        {news.summary || "Summary not available"}
      </p>

      <div className="flex justify-between text-xs text-gray-500">
        <span>{news.source}</span>
        <span>{news.category}</span>
      </div>

      <a
        href={news.url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-block mt-3 text-blue-600 text-sm font-medium"
      >
        Read full article →
      </a>
    </div>
  );
};

export default NewsCard;
