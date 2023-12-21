# clean_XDR_Incidents

These scripts help to completely clean up Incidents and every related objects that had been created around the incident.

Actually these script are customized to delete every objects in CTIM that have their **source=XDR Demo**.

These specific object are actually all the objects created by the [**Detect, Alert and Block Threat Use Case**](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab). The XDR demo.

You can modify the source value in order to search for objects other than **source=XDR Demo**. Just open the **get_xxx** and replace the value of the variable named **source_to_select** by an other value than **XDR Demo**.

## Some explanation

When we create an **Incident** within XDR, we use to create other objects that are attached to this **incident**.

We create :

- **Incident**
- **Sightings** now called **events**
- **Judgments**
- **Relationships**

An incident contains one or several Sightings. Every sightings contains targets and malicious observables. Relationships are used to attach sightings to Incidents, they are used to attach Observables to targets and to attach observables in judgments to Indicators and feeds.

In the **Detect, Alert and Block Threat Use Case** every created object has as **source** value : **XDR Demo**.

This source value is an easy criteria to delete easily every created objects during the demo.

## How to do

### Step 1 : edit the config.txt file

And set the correct values for the variables.

### Step 2 : Run the script one after the other in their numerical order

