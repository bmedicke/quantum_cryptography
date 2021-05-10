![quantum cryptography logo](media/logo-00.png)

Demonstration of **quantum-cryptography-based one-time pad communication** via<br>the **BB84 algorithm** using a non-single photon source.

[project progress](#project-progress) | [contributors](#contributors) | [repository structure](#repository-structure) | [frequently asked questions](#frequently-asked-questions)

---

## project progress

Kanban Boards:  [Everyone](https://github.com/bmedicke/quantum_cryptography/projects/1?fullscreen=true), [Ben](https://github.com/bmedicke/quantum_cryptography/projects/1?fullscreen=true&card_filter_query=assignee%3Abmedicke), [Ferdi](https://github.com/bmedicke/quantum_cryptography/projects/1?fullscreen=true&card_filter_query=assignee%3Aosomo3000), [Manu](https://github.com/bmedicke/quantum_cryptography/projects/1?fullscreen=true&card_filter_query=assignee%3Anamanuel), [Niko](https://github.com/bmedicke/quantum_cryptography/projects/1?fullscreen=true&card_filter_query=assignee%3Anikobenedikt)

[![GitHub milestones](https://img.shields.io/github/milestones/open/bmedicke/quantum_cryptography)](https://github.com/bmedicke/quantum_cryptography/milestones?state=open)
[![GitHub milestones](https://img.shields.io/github/milestones/closed/bmedicke/quantum_cryptography)](https://github.com/bmedicke/quantum_cryptography/milestones?state=closed)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/w/bmedicke/quantum_cryptography?style=flat-square)](https://github.com/bmedicke/quantum_cryptography/graphs/contributors)

## contributors

| Author           | GitHub profile                                  |
|------------------|-------------------------------------------------|
| Benjamin Medicke | [bmedicke](https://github.com/bmedicke)         |
| Ferdi Cevik      | [Osomo3000](https://github.com/Osomo3000)       |
| Manuel Nagel     | [namanuel](https://github.com/namanuel)         |
| Nikolai Benedikt | [nikobenedikt](https://github.com/nikobenedikt) |

## repository structure

Here's a quick breakdown of what to find where in the repository:

* [Theory](markdown/theory.md) 💭 describes the the BB84 algorithm and required theory
* [Hardware](markdown/hardware.md) 🔭 collects information about which hardware was used and how to set it up
* [3D models](3d-models) 🏗️ holds printable components
* [Setup](markdown/setup.md) 🧑🏻‍💻 installation instructions for the software and required services
* [Notebooks](notebooks) 🪐 contains the actual JupyterLab Notebooks for Alice, Bob and Eve
* [Guidelines](markdown/guidelines.md) ✒️  coding and contribution guidelines

## frequently asked questions

**Why build some components instead of using the respective ThorLabs versions?**

Mainly to keep it open-source and reduce the size of the hardware setup. As an added bonus it lowers the cost and barrier of entry for anyone who is interested in replicating the project.

**What hardware do I need to run this project?**

See [Hardware](markdown/hardware.md) for a list of required components and [3D models](3d-models) for printable parts.
