import sys
import json
import decimal

import lib
import config

def main(vessel):
    # make sure we don't accidentially import using the wrong name
    if vessel not in config.PROPER_NAMES:
        print "ERROR: Unknown vessel %s" % vessel
        return

    print "Clearing data for vessel %s..." % vessel

    count = lib.clear_vessel(vessel)

    print "Removed %d entries" % count

    print "Importing PredictWind JSON..."

    predictwind_entries = json.load(open('predictwind.json'))

    print "%d entries to import..." % len(predictwind_entries['route'])

    entry_count = 0
    import_count = 0
    last_entry = None
    for entry in predictwind_entries['route']:
        if entry_count % 100 == 0:
            print "   %d entries..." % entry_count

        entry_count += 1

        # save time by not checking the last position in dynamo
        if last_entry:
            distance_from_last = lib.distance(
                (entry['p']['lat'], entry['p']['lon']),
                (last_entry['p']['lat'], last_entry['p']['lon']))

            if distance_from_last < 1:
                last_entry = entry
                continue

        # add the position
        lib.add_position_to_dynamo(vessel,
                                   decimal.Decimal(str(entry['p']['lat'])),
                                   decimal.Decimal(str(entry['p']['lon'])),
                                   entry['t'],
                                   skip_last_position_check=True)
        last_entry = entry

        import_count += 1

    print "Processed %d positions, imported %d" % (entry_count, import_count)


if __name__ == "__main__":
    main(sys.argv[1])
