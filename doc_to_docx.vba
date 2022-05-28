
Sub main()
    Dim fso As New FileSystemObject  '定义一个文件系统对象
    Dim fld As Folder
    Dim xDlg As FileDialog
    Dim xDirNam As String
    
    Application.ScreenUpdating = False
    
    Set xDlg = Application.FileDialog(msoFileDialogFolderPicker)
    If xDlg.Show <> -1 Then Exit Sub
    ' 退出
    
    xDirName = xDlg.SelectedItems(1)
    If fso.FolderExists(xDirName) Then        '判断文件是否存在
        Set fld = fso.GetFolder(xDirName)
        ScanDirs fld         '调用函数
    Else
        MsgBox "文件夹不存在"
    End If
    MsgBox "转换完成"
    
    Application.ScreenUpdating = True
End Sub

Sub ScanDirs(fld As Folder)
    '递归遍历文件夹
    Dim fil As File, outFld As Folder    '定义一个文件夹和文件变量
    Set subfiles = fld.Files()     '获取文件夹下所有文件
    Set SubFolders = fld.SubFolders      '获取文件夹下所有文件夹
    
    
    ConvertDocToDocx fld.Path    '检查根目录是否有需要转换的
    For Each outFld In SubFolders    '遍历文件夹
        ConvertDocToDocx outFld.Path
        ScanDirs outFld      '调用函数自身
    Next
End Sub

' https://blog.csdn.net/uu00soldier/article/details/106443966

Sub ConvertDocToDocx(xDirName As String)
    'doc转换成docx
    Dim xFolder As Variant
    Dim xSaveFolder As Variant
    Dim xFileName As String
    ' sou 
    ' vba 打印
    Debug.Print "xFolder"
    Debug.Print xFolder
    
    xFolder = xDirName + "\"
    xSaveFolder = xDirName + "_docx\"
    If Dir(xFolder) <> "" And Dir(xSaveFolder) = "" Then MkDir xSaveFolder '判断文件夹是否存在，不存在则创建。
        
    xFileName = Dir(xFolder & "*.doc", vbNormal)
    While xFileName <> ""
        Documents.Open FileName:=xFolder & xFileName, _
        ConfirmConversions:=False, ReadOnly:=False, AddToRecentFiles:=False, _
        PasswordDocument:="", PasswordTemplate:="", Revert:=False, _
        WritePasswordDocument:="", WritePasswordTemplate:="", Format:= _
        wdOpenFormatAuto, XMLTransform:=""
        
        ActiveDocument.SaveAs xSaveFolder & Replace(xFileName, "doc", "docx"), wdFormatDocumentDefault
        ActiveDocument.Close
        xFileName = Dir()
    Wend
End Sub



