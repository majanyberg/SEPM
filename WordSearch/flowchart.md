```mermaid
flowchart LR
    subgraph GUI["Our GUI Layer"]
        B[Letter Buttons]
        D[Display Elements]
        D1[Found words Count]
        D2[Lives Count]
        D3[Button color]
        D4[Selected_words color]
    end

    subgraph Logic["Logic Layer (Other Team)"]
        L[Game Logic]
    end

    B -->|"submitData(row, col)"| L
    L -->|"Update game state"| D
    D --> D1
    D --> D2
    D --> D3
    D --> D4

    style GUI fill:#lightgreen
    style Logic fill:#lightgray