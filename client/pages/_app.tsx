import "../styles/globals.css";
import type { AppProps } from "next/app";
import NavigationBar from "../components/navigationBar";
import { Container } from "@mui/material";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <NavigationBar></NavigationBar>
      <Container fixed sx={{ mt: 3 }}>
        <Component {...pageProps} />
      </Container>
    </>
  );
}

export default MyApp;
