# Drive FAQs

### Can I increase the Drive storage limit?
!!! help ""
    No, the Drive storage limit is fixed at 10 GB. It may be increased in later updates.

### Can I share Drive contents?
!!! help ""
    You can't share Drive files via links. You can create a simple API on a Micro that serves files from your Drive.
    An example of this can be found [here](/examples/fastapi-drive-cdn).

### How to delete Drive files or Drive ?
!!! help ""
    You can delete Drive files by deleting them from the [drive ui](https://docs.deta.sh/docs/drive/drive_ui/) or using
    their [SDK](https://docs.deta.sh/docs/drive/sdk/) / [HTTP API](https://docs.deta.sh/docs/drive/http/).

    To delete whole Drive, you need to remove all the files & folders in it. Then it will be deleted automatically.