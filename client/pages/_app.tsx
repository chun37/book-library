import "../styles/globals.css";
import type { AppProps } from "next/app";
import NavigationBar from "../components/navigationBar";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <NavigationBar></NavigationBar>
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
