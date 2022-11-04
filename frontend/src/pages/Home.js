import React, { useCallback, useState } from "react";
import PageLinkBtn from "components/PageLinkBtn";
import FileDropZone from "components/FileDropZone";
import "pages/pageStyles.css";

const Home = () => {
  const url = "http://localhost:8000/upload/file";
  const [file, setFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);

  const handleFileSubmission = async (event) => {
    const formData = new FormData();

    formData.append("file", file);
    formData.append("type", "application/pdf");

    console.dir(formData);
    // Post request to fastapi server to upload file
    const response = await fetch(url, {
      method: "POST",
      body: formData,
    }).then((response) => {
      response.json();
      console.log(response);
    });
  };

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    console.dir(file);
    setFile(file);
    setIsFilePicked(true);

    return file;
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
      <button className="submit-btn" onClick={handleFileSubmission}>
        Submit
      </button>
    </section>
  );
};

export default Home;
