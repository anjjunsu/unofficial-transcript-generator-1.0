import React from "react";
import { Link } from "react-router-dom";
import "components/componentStyles.css";

// Button component for page navigation
const PageLinkBtn = ({ pageName, pageLink }) => {
  return (
    <button className="page-link-btn">
      <Link
        to={pageLink}
        style={{ textDecoration: "inherit", color: "inherit" }}
      >
        {pageName}
      </Link>
    </button>
  );
};

export default PageLinkBtn;
