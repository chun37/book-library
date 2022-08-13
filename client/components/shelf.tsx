import { Box } from "@mui/material";
import DisplayedBook from "./displayedBook";

const Shelf = () => {
  const books = new Array(50).fill(null);

  const displayedBooks = books.map((book, idx) => {
    return (
      <DisplayedBook
        key={idx}
        sx={{
          flexBasis: "200px",
          flexGrow: 1,
          m: 1,
        }}
      ></DisplayedBook>
    );
  });

  return (
    <Box
      sx={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "space-between",
      }}
    >
      {displayedBooks}
    </Box>
  );
};

export default Shelf;
