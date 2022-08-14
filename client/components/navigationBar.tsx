import { Box, AppBar, Toolbar, Typography, Button } from "@mui/material";
import AddCircleOutlineOutlinedIcon from "@mui/icons-material/AddCircleOutlineOutlined";
import Link from "next/link";

const NavigationBar = () => {
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <Link href="/">
            <a>
              <Typography variant="h6" component="div">
                蔵書管理
              </Typography>
            </a>
          </Link>
          <Box sx={{ mx: "auto" }}></Box>
          <Link href="/register">
            <Button
              color="inherit"
              variant="outlined"
              startIcon={<AddCircleOutlineOutlinedIcon />}
            >
              登録
            </Button>
          </Link>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default NavigationBar;
