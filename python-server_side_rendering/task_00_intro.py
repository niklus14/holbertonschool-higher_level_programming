import os

def generate_invitations(template, attendees):
    """Generate invitation files based on a template and attendee list."""

    # ---------------------------------------------------
    # 1. INPUT TYPE CHECK
    # ---------------------------------------------------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ---------------------------------------------------
    # 2. EMPTY TEMPLATE CHECK
    # ---------------------------------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ---------------------------------------------------
    # 3. EMPTY LIST CHECK
    # ---------------------------------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------------------------------------------------
    # 4. PROCESS EACH ATTENDEE
    # ---------------------------------------------------
    for index, attendee in enumerate(attendees, start=1):

        # Hər placeholder üçün "N/A" fallback veririk
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Template-i emal edirik
        try:
            output_text = (
                template.replace("{name}", name)
                        .replace("{event_title}", event_title)
                        .replace("{event_date}", str(event_date))
                        .replace("{event_location}", event_location)
            )
        except Exception as e:
            print(f"Error processing attendee #{index}: {e}")
            continue

        # ---------------------------------------------------
        # 5. WRITE OUTPUT FILE
        # ---------------------------------------------------
        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, "w") as f:
                f.write(output_text)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
            continue
