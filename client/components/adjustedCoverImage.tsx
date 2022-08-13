import { Box } from "@mui/material";
import Image from "next/image";
import dummy from "../public/dummy.png";

const AdjustedCoverImage = () => {
  return (
    <Box>
      <Image src={dummy}></Image>
    </Box>
  );
};
export default AdjustedCoverImage;
