# மயல் (Mayal) - Biconsonantal Cluster Analysis in Old Tamil

**மயல்** is a computational linguistics tool for analysing the frequency patterns of biconsonantal clusters (மெய் + மெய் / consonant + consonant sequences) in classical Tamil texts from the Sangam period.

## Publications

This research has resulted in two peer-reviewed publications:

### English Publication
**"Pattern of Biconsonantal Clusters in Old Tamil Texts"**  
*International Journal of Dravidian Linguistics (IJDL)*, January 2025

- [Academia.edu](https://www.academia.edu/127789335/Pattern_of_Biconsonantal_Clusters_in_Old_Tamil_Texts)
- [IJDL Journal](https://ijdl.org/Html/ijdl-journal-jan2025.html)

### Tamil Publication (தமிழ் வெளியீடு)
**"பழந்தமிழ் இலக்கியத்தில் மெய்ம்மயக்கத்தின் பாங்கு"**  
*பன்னாட்டுக் கணித்தமிழ்த் தகவல் தொழில்நுட்ப மாநாடு (ICTCIT) 2024*  
International Conference on Tamil Computing and Information Technology

- [Academia.edu](https://www.academia.edu/127786715/%E0%AE%AA%E0%AE%B4%E0%AE%A8_%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4_%E0%AE%87%E0%AE%B2%E0%AE%95_%E0%AE%95%E0%AE%BF%E0%AE%AF%E0%AE%A4_%E0%AE%A4%E0%AE%BF%E0%AE%B2_%E0%AE%AE%E0%AF%86%E0%AE%AF_%E0%AE%AE_%E0%AE%AE%E0%AE%AF%E0%AE%95_%E0%AE%95%E0%AE%A4_%E0%AE%A4%E0%AE%BF%E0%AE%A9_%E0%AE%AA%E0%AE%BE%E0%AE%99_%E0%AE%95%E0%AF%81)

## Citing This Work

If you use this tool or build upon this research, please cite our publications:

```bibtex
@article{venkatakrishnan2025biconsonantal,
  title={Pattern of Biconsonantal Clusters in Old Tamil Texts},
  author={Venkatakrishnan, Ramprashanth and Kumarasamy, R. and Lakshmanan, Balasundararaman},
  journal={International Journal of Dravidian Linguistics},
  year={2025},
  month={January}
}

@inproceedings{venkatakrishnan2024meymayakkam,
  title={பழந்தமிழ் இலக்கியத்தில் மெய்ம்மயக்கத்தின் பாங்கு},
  author={Venkatakrishnan, Ramprashanth and Lakshmanan, Balasundararaman},
  booktitle={Proceedings of the International Conference on Tamil Computing and Information Technology (ICTCIT)},
  year={2024}
}
```

### Authors

| Name | Affiliation |
|------|-------------|
| இராம்பிரசாந்த் வெங்கடக்கிருஷ்ணன் (Ramprashanth Venkatakrishnan) | மதுரை காமராசர் பல்கலைக்கழகம் (Madurai Kamaraj University), India |
| R. Kumarasamy | மதுரை காமராசர் பல்கலைக்கழகம் (Madurai Kamaraj University), India |
| பாலசுந்தரராமன் இலக்குவன் (Balasundararaman Lakshmanan) | Indeed Japan, Tokyo |

## Overview

This project computes and visualises the frequency of biconsonantal clusters in Sangam literature—the oldest extant literature of Old Tamil. The analysis covers:

### எட்டுத்தொகை (Eṭṭuttokai) - Eight Anthologies
| Tamil | ISO 15919 |
|-------|-----------|
| ஐங்குறுநூறு | Aiṅkuṟunūṟu |
| அகநானூறு | Akanāṉūṟu |
| கலித்தொகை | Kalittokai |
| குறுந்தொகை | Kuṟuntokai |
| நற்றிணை | Naṟṟiṇai |
| பரிபாடல் | Paripāṭal |
| பதிற்றுப்பத்து | Patiṟṟuppattu |
| புறநானூறு | Puṟanāṉūṟu |

### பத்துப்பாட்டு (Pattuppāṭṭu) - Ten Idylls
| Tamil | ISO 15919 |
|-------|-----------|
| திருமுருகாற்றுப்படை | Tirumurukāṟṟuppaṭai |
| பொருநராற்றுப்படை | Porunārāṟṟuppaṭai |
| சிறுபாணாற்றுப்படை | Ciṟupāṇāṟṟuppaṭai |
| பெரும்பாணாற்றுப்படை | Perumpāṇāṟṟuppaṭai |
| முல்லைப்பாட்டு | Mullaippāṭṭu |
| மதுரைக்காஞ்சி | Maturaikkāñci |
| நெடுநல்வாடை | Neṭunalvāṭai |
| குறிஞ்சிப்பாட்டு | Kuṟiñcippāṭṭu |
| பட்டினப்பாலை | Paṭṭiṉappālai |
| மலைபடுகடாம் | Malaipaṭukaṭām |

## Methodology

The study uses two text processing modes to handle word boundaries:

| Mode | Tamil | Description |
|------|-------|-------------|
| **யாப்பு** (Metrical) | Yāppu | Treats text as continuous metrical verse |
| **சொற்பிரிப்பு** (Word-separated) | Coṟpirippu | Respects word boundaries |

This produces four estimation types based on whether whitespace is removed ("merged") or preserved:

| Type | Mode | Whitespace | Effect |
|------|------|------------|--------|
| Type 1 | யாப்பு | Preserved | Underestimation |
| Type 2 | யாப்பு | Removed (merged) | Overestimation |
| Type 3 | சொற்பிரிப்பு | Preserved | Underestimation |
| Type 4 | சொற்பிரிப்பு | Removed (merged) | Overestimation |

The mean of Types 2 and 3 represents the best estimate for cluster frequencies.

### Phonetic Categories Analysed

Clusters are classified based on consonant types:
- **Plosives (P)**: க், ச், ட், த், ப், ற்
- **Nasals (N)**: ங், ஞ், ண், ந், ம், ன்
- **Approximants (A)**: ய், ர், ல், வ், ழ், ள்

## Output

The tool generates:
- **Frequency matrices** (18×18 consonant co-occurrence tables)
- **Maximum Likelihood Estimation** (row-wise and column-wise probabilities)
- **Pie charts** showing distribution of cluster types (PP, PN, NP, NN, etc.)
- **CSV exports** for further analysis

## Installation

```bash
pip install -r requirements.txt
```

### Requirements
- Python 3.x
- NLTK
- Pandas
- Matplotlib
- dataframe-image

## Usage

```bash
python mayal.py
```

Output files are generated in the `out/` directory, organised by estimation type and text collection.

## Project Structure

```
mayal/
├── mayal.py              # Main analysis script
├── corpora/
│   ├── யாப்பு/           # Metrical text versions
│   │   ├── எட்டுத்தொகை/
│   │   └── பத்துப்பாட்டு/
│   └── சொற்பிரிப்பு/      # Word-separated versions
│       ├── எட்டுத்தொகை/
│       └── பத்துப்பாட்டு/
├── out/                  # Generated analysis outputs
├── publications/         # Published papers (PDF)
└── requirements.txt
```

## Licence

See [LICENSE](LICENSE) for details.
