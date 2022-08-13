import { Box, TextField, InputAdornment, Button } from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";

const SearchBar = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <TextField
        id="book-name"
        label="タイトル"
        variant="outlined"
        margin="normal"
        sx={{ mr: 2, flexGrow: 1 }}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
      />
      <Button variant="contained" sx={{ my: 3, mr: 0 }}>
        検索
      </Button>
    </Box>
  );
};

export default SearchBar;
