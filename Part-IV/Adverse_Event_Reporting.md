# Adverse Event Reporting & Data Export Standards

[**HOME**](../index.md) | [**PART I**](../Part-I/index.md) | [**PART II**](../Part-II/index.md) | [**PART III**](../Part-III/index.md) | [**PART IV**](../Part-IV/index.md)

---

## **Overview**
This document establishes the standardized procedures for reporting, tracking, and analyzing adverse events across all 75 sessions of the WRH Master Curriculum. The framework ensures participant safety, institutional accountability, federal compliance, and continuous program improvement through systematic data collection and analysis.

---

## **1.0 Adverse Event Definition & Classification**

An **adverse event** is any occurrence during or immediately following a WRH session that results in participant distress, dysregulation, or requires intervention beyond standard session protocol. Adverse events are classified into four categories:

| Classification | Severity | Examples | Response Level |
| :------------- | :------- | :------- | :-------------- |
| **Level 1 (Minor)** | Low | Mild participant anxiety, brief emotional response, self-corrected with RGP | Facilitator-managed, documented |
| **Level 2 (Moderate)** | Moderate | Significant dysregulation requiring extended RGP, participant requests session pause | Facilitator-managed, clinical staff notified, documented |
| **Level 3 (Major)** | High | Acute distress, indirect suicidal ideation, aggressive behavior, SPI handoff required | SPI Handoff Protocol activated, clinical staff assumes care, documented |
| **Level 4 (Critical)** | Critical | Direct suicidal ideation, active self-harm, threat to others, emergency services required | Immediate crisis response, emergency services contacted, documented |

---

## **2.0 Reporting Procedure & Timeline**

### **2.1 Immediate Notification (Within 1 Hour)**
Upon occurrence of a Level 2, 3, or 4 adverse event, the facilitator must immediately notify the Program Coordinator and designated clinical support staff. Notification includes:
*   Session number and participant identifier (de-identified code).
*   Brief description of the event.
*   Current participant status (stabilized, in clinical care, etc.).
*   Any immediate actions taken.

### **2.2 Detailed Incident Report (Within 24 Hours)**
A comprehensive incident report must be completed within 24 hours using the standardized **Adverse Event Report Form** (see Section 3.0). This report includes:
*   Complete S-Prefix Metrics (S-ACT, S-REG, S-INT, S-OUT).
*   Detailed description of the event and triggering factors.
*   Facilitator response and effectiveness.
*   Clinical intervention (if applicable).
*   Participant disposition and follow-up plan.

### **2.3 7-Day Follow-up Assessment**
The Program Coordinator must conduct a follow-up assessment within 7 days of any Level 2, 3, or 4 adverse event. This assessment includes:
*   Direct contact with the participant (or clinical team, if handoff occurred).
*   Assessment of participant well-being and program impact.
*   Determination of whether additional clinical support is needed.
*   Documentation of follow-up findings and any recommendations.

---

## **3.0 Standardized Adverse Event Report Form**

| Field | Description | Required |
| :---- | :---------- | :------- |
| **Incident ID** | Unique identifier (e.g., AER-2026-001) | Yes |
| **Date & Time** | Date and time of incident | Yes |
| **Session Number** | WRH session during which incident occurred | Yes |
| **Delivery Tier** | Tier 1 (Community), Tier 2 (Structured), or Tier 3 (Clinical) | Yes |
| **Participant Code** | De-identified participant identifier | Yes |
| **Facilitator Name** | Name of facilitator conducting session | Yes |
| **Adverse Event Level** | Level 1, 2, 3, or 4 | Yes |
| **Event Description** | Detailed, de-identified description of what occurred | Yes |
| **Triggering Factors** | Content, participant state, or environmental factors that may have contributed | Yes |
| **S-ACT (Activation Level)** | 1-5 scale of participant nervous system activation | Yes |
| **S-REG (RGP Effectiveness)** | Success, Partial Success, or Failure | Yes |
| **S-INT (Intervention Type)** | Verbal, RGP, SPI Handoff, or Other | Yes |
| **S-OUT (Outcome)** | Stabilized, Handoff to Clinical, Exit, or Other | Yes |
| **Clinical Staff Involved** | Names of clinical staff who assisted (if applicable) | Conditional |
| **Emergency Services** | Whether emergency services were contacted | Yes |
| **Facilitator Reflection** | Facilitator's assessment of what could be improved | No |
| **Follow-up Date** | Date of 7-day follow-up assessment | Conditional |
| **Follow-up Findings** | Summary of follow-up assessment results | Conditional |

---

## **4.0 De-Identified CSV Export Standards**

### **4.1 Export Frequency & Timing**
Adverse event data is compiled and exported weekly (every Monday) into a de-identified Comma Separated Values (CSV) format. Weekly exports allow for timely trend analysis and rapid identification of emerging safety concerns.

### **4.2 Data Fields for CSV Export**
The following fields are included in the weekly CSV export:

```
Incident_ID, Date, Time, Session_Number, Delivery_Tier, S_ACT, S_REG, S_INT, S_OUT, 
Event_Level, Triggering_Factor_Category, Emergency_Services_Contacted, Follow_Up_Completed, 
Follow_Up_Status, Facilitator_Tier, Location_Code
```

### **4.3 Anonymization & Privacy Standards**
All personally identifiable information (PII) is removed or aggregated prior to export:
*   Participant names, dates of birth, and contact information are replaced with de-identified codes.
*   Facilitator names are replaced with facilitator tier and location code.
*   Specific clinical diagnoses or sensitive personal details are summarized into categorical variables.
*   Geographic information is aggregated to facility/program level only.

### **4.4 Data Retention & Access Control**
*   **Retention Period**: Adverse event data is retained for a minimum of 7 years to comply with federal contracting and healthcare regulations.
*   **Access Control**: CSV exports are stored in a secure, encrypted repository accessible only to authorized personnel (Program Coordinator, Clinical Director, Compliance Officer).
*   **Audit Trail**: All access to adverse event data is logged and audited quarterly.

---

## **5.0 Trend Analysis & Program Improvement**

### **5.1 Monthly Trend Report**
The Program Coordinator generates a monthly trend report analyzing the previous month's adverse events. This report includes:
*   Total number of adverse events by level and session.
*   Identification of sessions or delivery tiers with elevated adverse event rates.
*   Analysis of common triggering factors.
*   Effectiveness of interventions (RGP success rates, SPI handoff outcomes).
*   Recommendations for facilitator training, script refinement, or protocol adjustment.

### **5.2 Continuous Improvement Process**
Based on trend analysis, the program implements the following continuous improvement cycle:
1.  **Identify** emerging safety concerns or patterns.
2.  **Analyze** root causes and contributing factors.
3.  **Develop** targeted interventions or protocol refinements.
4.  **Implement** changes with facilitator training.
5.  **Monitor** effectiveness of changes through subsequent adverse event data.

---

## **6.0 Compliance & Reporting to Federal Agencies**

### **6.1 Quarterly Compliance Report**
A quarterly compliance report is submitted to the contracting federal agency (e.g., VA, DoD) summarizing:
*   Total adverse events by level and session.
*   Serious adverse events (Level 3 or 4) with de-identified case summaries.
*   Program-level safety metrics and trends.
*   Any protocol changes or facilitator retraining conducted in response to adverse events.

### **6.2 Serious Adverse Event Notification**
Any Level 4 (Critical) adverse event, or any Level 3 adverse event involving potential harm, must be reported to the contracting federal agency within 48 hours of occurrence, with a detailed follow-up report within 5 business days.

---
---
[**BACK TO TOP**](#) | [**CURRICULUM INDEX**](../index.md)
*Proprietary Intellectual Property of Capitol Contracts LLC. All Rights Reserved.*
*UEI: HH77KN5AV5X7 | CAGE: 9ZFJ6*
