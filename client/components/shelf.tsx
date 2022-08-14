import { Box, Grid, Typography } from "@mui/material";
import DisplayedBook from "./displayedBook";

const Shelf = () => {
  const books = new Array(53).fill(null);

  const displayedBooks = books.map((_, idx) => {
    const randomLengthString = "あ".repeat(idx);
    const bookImages = ["/dummy.png", "/isekaijoucho.jpg", "hoshi.jpg"];

    return (
      <Box key={idx} p={1} my={0.5}>
        <Grid
          sx={{
            display: "flex",
            flexDirection: "column",
            width: "200px",
          }}
        >
          <DisplayedBook
            link={bookImages[idx % bookImages.length]}
          ></DisplayedBook>
          <Typography mt={1}>{randomLengthString}</Typography>
        </Grid>
      </Box>
    );
  });

  return (
    <Box sx={{ padding: "auto" }}>
      <Box sx={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}>
        {displayedBooks}
      </Box>
    </Box>
  );
};

export default Shelf;
