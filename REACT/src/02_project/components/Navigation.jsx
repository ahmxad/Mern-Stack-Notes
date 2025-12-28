import { useState } from "react";
import styles from "./Navigation.module.css";

export default function Navigation() {
  const [open, setOpen] = useState(false);
  return (
    <nav className={styles.nav}>
      <button
        className={styles.hamburger}
        aria-expanded={open}
        aria-label="Toggle menu"
        onClick={() => setOpen(!open)}
      >
        ☰
      </button>

      <ul className={`${styles.nav_list} ${open ? styles.open : ""}`}>
        <li>Home</li>
        <li>Contact</li>
        <li>About</li>
        <li>Other</li>
      </ul>

      <button className={styles.login_btn}>Login</button>
    </nav>
  );
}
