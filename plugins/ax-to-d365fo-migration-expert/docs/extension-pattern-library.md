# D365FO Extension Pattern Library

## Chain of Command

Use when a class method must be extended and the method supports CoC.

```xpp
[ExtensionOf(classStr(TargetClass))]
final class TargetClass_Extension
{
    public void targetMethod()
    {
        next targetMethod();
        // migrated business logic
    }
}
```

## Event Handler

Use for decoupled reactions to table, form, or class events.

```xpp
public static void Target_onValidatedField(Common sender, DataEventArgs e)
{
    // validation logic
}
```

## Table Extension

Use for additional fields, indexes, relations, and validation events.

## Form Extension

Use form extensions plus event handlers instead of overlayering form controls.

## Data Entity

Use for migration, integrations, recurring data jobs, and controlled data access.

## Custom Service

Use when data entity/OData is insufficient and a service contract is needed.

## Business Event

Use for event-driven integration and external process notification.

## SysOperation

Use for batchable, service-oriented operations instead of legacy RunBaseBatch where redesign is required.

## Security Mapping

Map AX groups/roles to D365FO roles, duties, and privileges with SoD validation.
