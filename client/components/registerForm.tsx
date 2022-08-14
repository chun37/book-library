import { Box, Button, TextField } from "@mui/material";
import FixedButton from "./fixedButton";

const RegisterForm = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <TextField
        label="ISBN"
        variant="outlined"
        sx={{ width: "auto", mr: 2 }}
        InputLabelProps={{
          shrink: true,
        }}
      ></TextField>
      <FixedButton>情報取得</FixedButton>
    </Box>
  );
};

export default RegisterForm;
