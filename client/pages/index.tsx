import { Container } from "@mui/material";
import type { NextPage } from "next";
import SearchBar from "../components/searchBar";
import Shelf from "../components/shelf";

const Home: NextPage = () => {
  return (
    <>
      <SearchBar />
      <Shelf />
    </>
  );
};

export default Home;
