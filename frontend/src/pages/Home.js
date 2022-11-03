import React, { useCallback, useState } from "react";
import PageLinkBtn from "components/PageLinkBtn";
import FileDropZone from "components/FileDropZone";
import "pages/pageStyles.css";

const Home = () => {
  const [file, setFile] = useState(null);
  const onDrop = useCallback((acceptedFiles) => {
    console.log("in on drop");
    acceptedFiles.map((file) => {
      console.log("In");
      const reader = new FileReader();
      reader.onload = function (e) {
        setFile(e.target.result);
        console.log("loaded");
        console.dir(e.target);
      };
      reader.readAsDataURL(file);
      return file;
    });
  }, []);

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
      <FileDropZone onDrop={onDrop} accept={"application/pdf"} />
    </section>
  );
};

export default Home;
