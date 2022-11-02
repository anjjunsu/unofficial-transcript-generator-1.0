import React from "react";
import PageLinkBtn from "components/PageLinkBtn";
import "pages/pageStyles.css";

const Home = () => {
  return (
    <section className="home">
      <h1>Unofficial Transcript Generator</h1>
      <h2>Upload your UBC SSC grade summary here</h2>
      <h2>
        Then this generator will parse your grade summary to good looking
        unofficial transcript with full course name
      </h2>
      <h3>
        So that reader can understand what you actually studied instead of some
        random abbreviation🫡
      </h3>
      <PageLinkBtn pageName="User Guide" pageLink="/guide" />
    </section>
  );
};

export default Home;
