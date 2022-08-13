import { Box, SxProps, Theme } from "@mui/material";
import AspectRatio from "@mui/joy/AspectRatio";
import Image from "next/image";
import dummy from "../public/dummy.png";
import { FC } from "react";

type Props = {
  sx: SxProps;
};
const DisplayedBook: FC<Props> = ({ sx }) => {
  return (
    <Box
      sx={{
        ...sx,
        backgroundImage: "url('/dummy.png')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        aspectRatio: "1/1.4",
      }}
    ></Box>
  );
};

export default DisplayedBook;
