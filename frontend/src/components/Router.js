import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "pages/Home";
import Contact from "pages/Contact";
import Guide from "pages/Guide";
import Navbar from "components/Navbar";
import Footer from "components/Footer";

const AppRouter = () => {
  return (
    <Router basename="">
      <div id="page-container">
        <div id="content-wrap">
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/guide" element={<Guide />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
};

export default AppRouter;
