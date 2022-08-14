import { Box } from "@mui/material";
import { FC } from "react";

type Props = {
  link: string;
};

const DisplayedBook: FC<Props> = ({ link }) => {
  return (
    <Box
      sx={{
        backgroundImage: `url('${link}')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        aspectRatio: "1/1.4",
      }}
    ></Box>
  );
};

export default DisplayedBook;
