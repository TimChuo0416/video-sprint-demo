# AI Pipeline Orchestrator - Proof-of-Concept

This repository contains the preliminary work for the "AI Pipeline Orchestrator for Video Generation" proposal. It features a working, two-step video generation pipeline that demonstrates the core architectural concepts using Docker Compose.

### Quick Summary

[cite_start]To validate the proposal, I built a working prototype that simulates key concepts like "Containerized Execution" and a "Central Artifact Store". [cite_start]This end-to-end process successfully produces a final video artifact, proving the feasibility of the basic workflow. This experiment also showcases my ability to pragmatically adapt methods to achieve project goals.

---

### How to Run

1.  Ensure you have Docker and Docker Compose installed and running.
2.  Clone this repository.
3.  From the root of the project folder, run the following command:

    ```bash
    docker-compose up --build
    ```
4.  The final video, `demo.mp4`, will be generated in the `shared_data` folder.

---

### Results & Artifacts

* **Final Video Output:** [demo.mp4](<請在此貼上您 GitHub Release 的影片連結>)
* **Proof of Execution:** The screenshot below confirms both containers ran to completion successfully.

    ![Docker PS Output](<請在此貼上您 docker ps -a 的截圖路徑>)
