import { Box, TextField, InputAdornment, Button } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import FixedButton from "./fixedButton";

const SearchBar = () => {
  return (
    <Box sx={{ display: "flex", my: 0.5 }}>
      <TextField
        id="book-name"
        label="タイトル"
        variant="outlined"
        sx={{ mr: 2, flexGrow: 1 }}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
      />
      <FixedButton sx={{ mr: 0 }}>検索</FixedButton>
    </Box>
  );
};

export default SearchBar;
