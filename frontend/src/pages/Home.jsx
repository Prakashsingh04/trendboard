import { useEffect, useState } from "react";
import { fetchNews } from "../api/news";
import NewsCard from "../components/NewsCard";

const Home = () => {
  const [newsList, setNewsList] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadNews = async () => {
      const data = await fetchNews();
      setNewsList(data);
      setLoading(false);
    };

    loadNews();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-10">
        Loading news...
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">
        📰 Trending News
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {newsList.map((item, index) => (
          <NewsCard key={index} news={item} />
        ))}
      </div>
    </div>
  );
};

export default Home;
