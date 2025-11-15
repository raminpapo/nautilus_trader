# Documentation: `tests/test_data/databento/options_catalog/usd_short_term_rate.xml`
**Generated:** 2025-11-15T19:40:08.222984Z
**File Size:** 20174 bytes
**Extension:** .xml
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `tests/test_data/databento/options_catalog/usd_short_term_rate.xml`
- **Size:** 20,174 bytes
- **Lines:** 448
- **Extension:** `.xml`
- **Type:** text

---

## Source Code

```xml
<!--NSI Web Service v8.19.2.2-->
<message:GenericData>
    <message:Header>
        <message:ID>IREF009042</message:ID>
        <message:Test>false</message:Test>
        <message:Prepared>2025-01-31T12:36:14</message:Prepared>
        <message:Sender id="Disseminate_Final_DMZ"/>
        <message:Structure structureID="OECD_SDD_STES_DSD_STES_at_DF_FINMARK_4_0" dimensionAtObservation="TIME_PERIOD">
            <common:StructureUsage>
                <Ref agencyID="OECD.SDD.STES" id="DSD_STES@DF_FINMARK" version="4.0"/>
            </common:StructureUsage>
        </message:Structure>
        <message:DataSetAction>Information</message:DataSetAction>
        <message:DataSetID>DSD_STES</message:DataSetID>
    </message:Header>
    <message:DataSet action="Information" structureRef="OECD_SDD_STES_DSD_STES_at_DF_FINMARK_4_0">
        <generic:Series>
            <generic:SeriesKey>
                <generic:Value id="REF_AREA" value="USA"/>
                <generic:Value id="FREQ" value="M"/>
                <generic:Value id="MEASURE" value="IR3TIB"/>
                <generic:Value id="UNIT_MEASURE" value="PA"/>
                <generic:Value id="ACTIVITY" value="_Z"/>
                <generic:Value id="ADJUSTMENT" value="_Z"/>
                <generic:Value id="TRANSFORMATION" value="_Z"/>
                <generic:Value id="TIME_HORIZ" value="_Z"/>
                <generic:Value id="METHODOLOGY" value="N"/>
            </generic:SeriesKey>
            <generic:Attributes>
                <generic:Value id="UNIT_MULT" value="0"/>
                <generic:Value id="DECIMALS" value="2"/>
            </generic:Attributes>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-08"/>
                <generic:ObsValue value="0.1"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-09"/>
                <generic:ObsValue value="0.1"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-03"/>
                <generic:ObsValue value="1.35"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-05"/>
                <generic:ObsValue value="0.17"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-06"/>
                <generic:ObsValue value="0.2"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-10"/>
                <generic:ObsValue value="5.46"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-11"/>
                <generic:ObsValue value="5.41"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-09"/>
                <generic:ObsValue value="0.13"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-10"/>
                <generic:ObsValue value="0.12"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-11"/>
                <generic:ObsValue value="0.16"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-12"/>
                <generic:ObsValue value="0.17"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-01"/>
                <generic:ObsValue value="0.14"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-02"/>
                <generic:ObsValue value="0.11"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-03"/>
                <generic:ObsValue value="0.1"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-04"/>
                <generic:ObsValue value="0.11"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-05"/>
                <generic:ObsValue value="0.1"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-06"/>
                <generic:ObsValue value="0.09"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-01"/>
                <generic:ObsValue value="1.65"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-02"/>
                <generic:ObsValue value="1.59"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-10"/>
                <generic:ObsValue value="0.11"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-11"/>
                <generic:ObsValue value="0.14"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-12"/>
                <generic:ObsValue value="0.17"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-01"/>
                <generic:ObsValue value="0.22"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-02"/>
                <generic:ObsValue value="0.38"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-03"/>
                <generic:ObsValue value="0.73"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-04"/>
                <generic:ObsValue value="0.91"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-05"/>
                <generic:ObsValue value="1.33"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-06"/>
                <generic:ObsValue value="1.87"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-07"/>
                <generic:ObsValue value="2.5"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-08"/>
                <generic:ObsValue value="2.76"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-09"/>
                <generic:ObsValue value="3.21"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-10"/>
                <generic:ObsValue value="3.85"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-11"/>
                <generic:ObsValue value="4.46"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2022-12"/>
                <generic:ObsValue value="4.51"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-01"/>
                <generic:ObsValue value="4.61"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-02"/>
                <generic:ObsValue value="4.74"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-03"/>
                <generic:ObsValue value="4.91"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-04"/>
                <generic:ObsValue value="5.03"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-05"/>
                <generic:ObsValue value="5.15"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-06"/>
                <generic:ObsValue value="5.22"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-07"/>
                <generic:ObsValue value="5.35"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-08"/>
                <generic:ObsValue value="5.44"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-09"/>
                <generic:ObsValue value="5.49"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-07"/>
                <generic:ObsValue value="0.18"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2020-08"/>
                <generic:ObsValue value="0.15"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2023-12"/>
                <generic:ObsValue value="5.32"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-01"/>
                <generic:ObsValue value="5.26"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-02"/>
                <generic:ObsValue value="5.22"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-03"/>
                <generic:ObsValue value="5.29"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-04"/>
                <generic:ObsValue value="5.33"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-05"/>
                <generic:ObsValue value="5.33"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-06"/>
                <generic:ObsValue value="5.28"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-07"/>
                <generic:ObsValue value="5.31"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-08"/>
                <generic:ObsValue value="5.12"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-09"/>
                <generic:ObsValue value="4.86"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-10"/>
                <generic:ObsValue value="4.62"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-11"/>
                <generic:ObsValue value="4.53"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2024-12"/>
                <generic:ObsValue value="4.46"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
            <generic:Obs>
                <generic:ObsDimension id="TIME_PERIOD" value="2021-07"/>
                <generic:ObsValue value="0.1"/>
                <generic:Attributes>
                    <generic:Value id="OBS_STATUS" value="A"/>
                </generic:Attributes>
            </generic:Obs>
        </generic:Series>
    </message:DataSet>
</message:GenericData>
```


---

## Overview

This file is located at `tests/test_data/databento/options_catalog/usd_short_term_rate.xml` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/test_data/databento/options_catalog`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


