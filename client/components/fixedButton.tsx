import { Button, ButtonProps } from "@mui/material";
import { FC } from "react";

const FixedButton: FC<ButtonProps> = (props) => {
  return (
    <Button variant="contained" sx={{ my: 1, ...props.sx }} {...{ props }}>
      {props.children}
    </Button>
  );
};

export default FixedButton;
