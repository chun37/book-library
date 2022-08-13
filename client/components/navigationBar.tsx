import { Box, AppBar, Toolbar, Typography } from "@mui/material";

const NavigationBar = () => {
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div">
            蔵書管理
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default NavigationBar;
