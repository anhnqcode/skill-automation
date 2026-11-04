# Cài bộ Skill BA cho Claude Code trên máy này.
# Chạy lại mỗi khi thêm skill mới hoặc chuyển thư mục Skill BA sang chỗ khác:
#   powershell -ExecutionPolicy Bypass -File "<thư mục Skill BA>\cai-dat.ps1"
# Mỗi thư mục con có SKILL.md được nối (junction) vào ~/.claude/skills,
# nên skill dùng được ở mọi dự án, còn file gốc vẫn nằm trong thư mục Skill BA.

$root = $PSScriptRoot
$skills = Join-Path $env:USERPROFILE ".claude\skills"
New-Item -ItemType Directory -Force $skills | Out-Null

# Cho skill biết thư mục Skill BA nằm ở đâu
[System.IO.File]::WriteAllText((Join-Path $skills ".skill-ba-root"), $root.Replace('\', '/'))

Get-ChildItem $root -Directory | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } | ForEach-Object {
    $link = Join-Path $skills $_.Name
    if (Test-Path $link) {
        $item = Get-Item $link -Force
        if ($item.LinkType -ne "Junction") {
            Write-Host "Bỏ qua $($_.Name): đã có thư mục thật cùng tên trong $skills"
            return
        }
        cmd /c rmdir "$link" | Out-Null
    }
    cmd /c mklink /J "$link" "$($_.FullName)" | Out-Null
    Write-Host "Đã cài /$($_.Name)"
}

# Agent riêng (thư mục _agents, nếu có): nối cứng (hard link) vào ~/.claude/agents,
# sửa file ở đâu cũng là sửa cùng một file. Khác ổ đĩa thì chép, khi đó sửa trong _agents rồi chạy lại.
$agentSrc = Join-Path $root "_agents"
if (Test-Path $agentSrc) {
    $agents = Join-Path $env:USERPROFILE ".claude\agents"
    New-Item -ItemType Directory -Force $agents | Out-Null
    Get-ChildItem $agentSrc -Filter *.md | ForEach-Object {
        $dst = Join-Path $agents $_.Name
        if (Test-Path $dst) { Remove-Item $dst -Force }
        try { New-Item -ItemType HardLink -Path $dst -Target $_.FullName -ErrorAction Stop | Out-Null }
        catch { Copy-Item $_.FullName $dst }
        Write-Host "Đã cài agent $($_.BaseName)"
    }
}
