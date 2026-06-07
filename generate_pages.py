import os

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Portfolio</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo">MyPortfolio.</div>
        <ul class="nav-links">
            <li><a href="index.html#about">Giới thiệu</a></li>
            <li><a href="index.html#projects">Dự án</a></li>
            <li><a href="index.html#summary">Tổng kết</a></li>
        </ul>
    </nav>
    <div class="project-page">
        <a href="index.html#projects" class="back-btn"><i class="fas fa-arrow-left"></i> Quay lại danh sách dự án</a>
        <div class="article-content">
            {content}
        </div>
    </div>
    <footer>
        <p>&copy; 2026 Bản quyền thuộc về Học viên.</p>
    </footer>
</body>
</html>
"""

projects = {
    "project1.html": {
        "title": "Bài 1: Thao tác cơ bản với tệp tin",
        "content": """
            <h1>Bài tập 1: Thao tác cơ bản với tệp tin và thư mục</h1>
            
            <h2>1. Mở File Explorer</h2>
            <p>Nhấn tổ hợp phím <strong>Windows + E</strong> hoặc nhấp vào biểu tượng thư mục màu vàng trên thanh tác vụ.</p>

            <h2>2. Truy cập ổ đĩa/thư mục</h2>
            <p>Ở cột bên trái, nhấp vào <strong>This PC</strong>, sau đó nhấp đúp vào một ổ đĩa không phải ổ hệ thống (ví dụ: ổ D: hoặc E:). Nếu chỉ có ổ C:, hãy vào thư mục Documents.</p>

            <h2>3. Tạo thư mục mới</h2>
            <p>Nhấp chuột phải vào một khoảng trống -> chọn <strong>New -> Folder</strong>. Đặt tên thư mục là <code>ThucHanh_NguyenVanNam</code>. Nhấn Enter.</p>

            <h2>4. Vào thư mục vừa tạo</h2>
            <p>Nhấp đúp vào thư mục <code>ThucHanh_NguyenVanNam</code>.</p>

            <h2>5. Tạo tệp tin văn bản</h2>
            <p>Nhấp chuột phải vào khoảng trống -> <strong>New -> Text Document</strong>. Đặt tên là <code>GhiChu.txt</code>. Nhấn Enter.</p>

            <h2>6. Đổi tên tệp tin</h2>
            <p>Nhấp chuột phải vào tệp <code>GhiChu.txt</code> -> chọn <strong>Rename</strong>. Đổi tên thành <code>GhiChuQuanTrong.txt</code>. Nhấn Enter.</p>

            <h2>7. Tạo thư mục con</h2>
            <p>Trong thư mục <code>ThucHanh_NguyenVanNam</code>, nhấp chuột phải -> <strong>New -> Folder</strong>. Đặt tên là <code>TaiLieu</code>.</p>

            <h2>8. Sao chép tệp tin (Copy & Paste)</h2>
            <p>Nhấp chuột phải vào tệp <code>GhiChuQuanTrong.txt</code> -> chọn <strong>Copy</strong> (hoặc chọn tệp rồi nhấn Ctrl + C).</p>
            <p>Nhấp đúp vào thư mục <code>TaiLieu</code>, nhấp chuột phải vào khoảng trống bên trong -> chọn <strong>Paste</strong> (hoặc nhấn Ctrl + V). Bây giờ bạn có một bản sao của tệp trong thư mục TaiLieu.</p>

            <h2>9. Di chuyển tệp tin (Cut & Paste)</h2>
            <p>Quay lại thư mục <code>ThucHanh_NguyenVanNam</code>. Tạo một tệp mới tên là <code>DiChuyen.txt</code>.</p>
            <p>Nhấp chuột phải vào tệp <code>DiChuyen.txt</code> -> chọn <strong>Cut</strong> (hoặc nhấn Ctrl + X).</p>
            <p>Nhấp đúp vào thư mục <code>TaiLieu</code>, nhấp chuột phải vào khoảng trống -> chọn <strong>Paste</strong>. Tệp gốc đã biến mất khỏi vị trí cũ và chỉ còn ở vị trí mới.</p>

            <h2>10. Xóa tệp tin</h2>
            <p>Trong thư mục <code>TaiLieu</code>, nhấp chuột phải vào tệp <code>GhiChuQuanTrong.txt</code> -> chọn <strong>Delete</strong>. Tệp sẽ được chuyển vào Thùng rác (Recycle Bin).</p>

            <h2>11. Xóa vĩnh viễn</h2>
            <p>Chọn tệp <code>DiChuyen.txt</code>, nhấn giữ phím <strong>Shift</strong> và nhấn phím <strong>Delete</strong>. Một cảnh báo sẽ hiện ra. Nếu đồng ý, tệp sẽ bị xóa vĩnh viễn mà không qua Thùng rác.</p>

            <h2>12. Khôi phục từ Thùng rác (Tùy chọn)</h2>
            <p>Tìm biểu tượng <strong>Recycle Bin</strong> trên màn hình nền, nhấp đúp để mở. Tìm tệp <code>GhiChuQuanTrong.txt</code> đã xóa, nhấp chuột phải vào nó và chọn <strong>Restore</strong>. Tệp sẽ quay trở lại vị trí ban đầu.</p>
        """
    },
    "project2.html": {
        "title": "Bài 2: Tìm kiếm và đánh giá thông tin",
        "content": """
            <h1>Tìm kiếm và đánh giá thông tin học thuật</h1>
            
            <h2>I. Giới thiệu chủ đề và Phạm vi tìm kiếm</h2>
            <ul>
                <li><strong>Chủ đề:</strong> Ứng dụng AI (Chatbots, hệ thống gợi ý, cá nhân hóa) và tác động đến sự hài lòng của khách hàng Gen Z tại Việt Nam.</li>
                <li><strong>Tính thách thức:</strong> Đây là lĩnh vực thay đổi nhanh chóng, đòi hỏi phải tổng hợp cả lý thuyết marketing truyền thống và các công nghệ mới nhất.</li>
                <li><strong>Từ khóa tìm kiếm:</strong> "AI in E-commerce", "Customer Experience", "Gen Z shopping behavior", "Artificial Intelligence Marketing".</li>
            </ul>

            <h2>II. Bảng tổng hợp và Đánh giá độ tin cậy</h2>
            <div style="overflow-x: auto;">
            <table>
                <tr>
                    <th>STT</th>
                    <th>Tên tài liệu</th>
                    <th>Loại nguồn</th>
                    <th>Đánh giá (Tác giả, Phương pháp, Cập nhật)</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Artificial Intelligence in Marketing (Kumar et al., 2024)</td>
                    <td>Bài báo (Tạp chí hạng A)</td>
                    <td>Tác giả là giáo sư đầu ngành. Phương pháp tổng hợp lý thuyết hệ thống. Rất cập nhật. (5 Sao)</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>AI and Customer Experience (Smith, 2023)</td>
                    <td>Sách chuyên khảo</td>
                    <td>Xuất bản bởi Oxford Press. Cung cấp khung lý thuyết sâu sắc về hành vi khách hàng. (5 Sao)</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Báo cáo Kinh tế số VN 2025 (Google & Temasek)</td>
                    <td>Nguồn mở uy tín</td>
                    <td>Dữ liệu thực tế từ thị trường Việt Nam. Tính ứng dụng thực tiễn cao nhưng thiếu phản biện học thuật. (4 Sao)</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Impact of Chatbots on Satifaction (Nguyen, 2022)</td>
                    <td>Bài báo khoa học</td>
                    <td>Nghiên cứu định lượng (khảo sát 400 người). Trích dẫn cao trên Google Scholar. (3 Sao)</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Machine Learning in Retail (IBM Whitepaper)</td>
                    <td>Nguồn mở doanh nghiệp</td>
                    <td>Chuyên sâu về kỹ thuật ứng dụng nhưng có thể mang tính quảng bá. (3 Sao)</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Consumer Trust in AI (Journal of Retailing, 2023)</td>
                    <td>Bài báo khoa học</td>
                    <td>Phương pháp thực nghiệm (Experimental design) cực kỳ chặt chẽ. (5 Sao)</td>
                </tr>
            </table>
            </div>

            <h2>III. Đánh giá chi tiết (Ví dụ)</h2>
            <p><strong>Tài liệu:</strong> Kumar, V. et al. (2024) 'Artificial Intelligence in Marketing', Journal of Marketing.</p>
            <ul>
                <li><strong>Tác giả:</strong> V. Kumar là chuyên gia có chỉ số H-index rất cao, uy tín hàng đầu trong giới Marketing.</li>
                <li><strong>Cơ quan xuất bản:</strong> Tạp chí Journal of Marketing (thuộc AMA) - tạp chí hàng đầu (Q1) trong danh mục Scopus.</li>
                <li><strong>Phương pháp:</strong> Sử dụng phương pháp Systematic Literature Review (Tổng quan lý thuyết hệ thống) từ hơn 200 nghiên cứu khác.</li>
                <li><strong>Tính cập nhật:</strong> Xuất bản năm 2024, bao hàm cả các đột phá về Generative AI.</li>
            </ul>

            <h2>IV. Danh mục tài liệu tham khảo (Harvard)</h2>
            <ol>
                <li>Chaffey, D. and Ellis-Chadwick, F. (2022) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.</li>
                <li>Google, Temasek and Bain & Company (2025) e-Conomy SEA 2025 Report.</li>
                <li>Kumar, V., Rajan, B., Venkatesan, R. and Lecinski, J. (2024) 'Understanding the Role of Artificial Intelligence in Personalized Engagement', Journal of Marketing, 88(1), pp. 112-135.</li>
                <li>Nguyen, H. M. (2022) 'Determinants of Customer Satisfaction with AI Chatbots in Vietnam', Vietnam Journal of Science and Technology, 60(3), pp. 45-58.</li>
                <li>Smith, A. (2023) The Algorithmic Consumer: AI and the Future of Experience. Oxford: Oxford University Press.</li>
            </ol>
        """
    },
    "project3.html": {
        "title": "Bài 3: Kỹ năng viết Prompt",
        "content": """
            <h1>Phát triển kỹ năng viết Prompt trong học tập</h1>
            
            <h2>I. Phân tích tác vụ học tập</h2>
            <p>Để tối ưu hóa hiệu quả của AI, chúng ta cần hiểu rõ bản chất của từng tác vụ:</p>
            <ul>
                <li><strong>Tác vụ 1: Tóm tắt bài đọc học thuật:</strong> Chuyển đổi thông tin phức tạp thành ngắn gọn nhưng không mất đi luận điểm cốt lõi.</li>
                <li><strong>Tác vụ 2: Giải thích khái niệm phức tạp:</strong> Đơn giản hóa thành ngôn ngữ dễ hiểu, có ví dụ minh họa. AI hay mắc lỗi giải thích bằng thuật ngữ chuyên ngành khác.</li>
                <li><strong>Tác vụ 3: Tạo bộ câu hỏi ôn tập:</strong> Tạo hệ thống câu hỏi đa dạng mức độ (nhận biết, thông hiểu, vận dụng).</li>
            </ul>

            <h2>II. Xây dựng các phiên bản Prompt</h2>
            <h3>1. Tác vụ 1: Tóm tắt bài đọc</h3>
            <ul>
                <li><strong>Cơ bản:</strong> "Tóm tắt giúp tôi bài văn sau: [Văn bản]"</li>
                <li><strong>Nâng cao (Role + CoT + Định dạng):</strong> "Bạn là một chuyên gia nghiên cứu học thuật... Hãy thực hiện tóm tắt theo các bước: B1: Xác định luận đề chính, B2: Liệt kê luận điểm hỗ trợ, B3: Rút ra kết luận. Trình bày dưới dạng bullet points."</li>
            </ul>

            <h3>2. Tác vụ 2: Giải thích khái niệm</h3>
            <ul>
                <li><strong>Cơ bản:</strong> "Lạm phát là gì?"</li>
                <li><strong>Nâng cao (Role + Persona + Few-shot):</strong> "Bạn là giáo sư kinh tế học nổi tiếng giải thích theo phương pháp Feynman... 1. Định nghĩa bình dân. 2. Ví dụ ẩn dụ sinh động. 3. Nguyên nhân cốt lõi."</li>
            </ul>

            <h3>3. Tác vụ 3: Tạo bộ câu hỏi</h3>
            <ul>
                <li><strong>Cơ bản:</strong> "Tạo 5 câu trắc nghiệm về CMCN 4.0."</li>
                <li><strong>Nâng cao (Role + Bloom + CoT):</strong> "Bạn là chuyên gia khảo thí. Tạo bộ câu hỏi theo thang đo Bloom (Nhận biết, Thông hiểu, Phân tích). Giải thích tại sao đáp án đó đúng và đáp án khác sai."</li>
            </ul>

            <h2>III. Tổng hợp nguyên tắc C-R-I-S-P</h2>
            <p>Công thức viết prompt đỉnh cao trong học tập:</p>
            <ul>
                <li><strong>C - Context (Bối cảnh):</strong> Luôn cung cấp ngữ cảnh rõ ràng.</li>
                <li><strong>R - Role (Vai trò):</strong> Định hình "bản sắc" cho AI (Chuyên gia, Gia sư).</li>
                <li><strong>I - Intent/Instruction (Chỉ dẫn):</strong> Dùng động từ mạnh mẽ, chia nhỏ quy trình (First, Then, Finally).</li>
                <li><strong>S - Style/Format (Phong cách):</strong> Quy định rõ đầu ra là bảng biểu, JSON, sơ đồ tư duy.</li>
                <li><strong>P - Parameter (Giới hạn):</strong> Đặt ranh giới (VD: Không quá 200 từ).</li>
            </ul>
        """
    },
    "project4.html": {
        "title": "Bài 4: Hợp tác trực tuyến",
        "content": """
            <h1>Năng lực cộng tác trực tuyến và Quản lý dự án số</h1>
            
            <h2>Phần 1: Tổng quan dự án</h2>
            <p><strong>Dự án:</strong> "Xây dựng mô hình và tài liệu đặc tả hệ thống cho Ứng dụng Quản lý Chi tiêu Cá nhân".</p>
            <p><strong>Hệ sinh thái công cụ:</strong></p>
            <ul>
                <li><strong>Trello:</strong> Quản lý tác vụ (Kanban board: To-do, In Progress, Under Review, Done).</li>
                <li><strong>Discord:</strong> Giao tiếp nhóm (Webhook, Channels chuyên biệt, Voice meeting).</li>
                <li><strong>Google Workspace:</strong> Lưu trữ và soạn thảo (Drive, Docs).</li>
            </ul>

            <h2>Phần 2: Nhật ký quản lý tác vụ</h2>
            <ul>
                <li><strong>Task 1:</strong> Thiết kế sơ đồ ERD. (Nhãn: Đỏ - Gấp).</li>
                <li><strong>Task 2:</strong> Viết tài liệu đặc tả thuộc tính. (Nhãn: Vàng).</li>
                <li><strong>Task 3:</strong> Tổng hợp chuẩn hóa file. (Nhãn: Xanh lá).</li>
            </ul>

            <h2>Phần 3: Quản lý tài nguyên và Đóng góp</h2>
            <p>Xây dựng cấu trúc thư mục 3 cấp trên Google Drive: <code>N28_DuAn_QuanLyChiTieu -> 02_Technical_Design -> 01_Database_Models</code>.</p>
            <p>Quy chuẩn đặt tên tệp: <code>[TênNhóm]_[TênMôđun]_[Phiênbản]</code>.</p>
            <p>Phân quyền: Chỉnh sửa (Editor) lúc làm việc, Xem (Viewer) cho bản Final để tránh ghi đè.</p>

            <h2>Phần 4: Thách thức và Giải pháp</h2>
            <ol>
                <li><strong>Xung đột ý kiến thiết kế DB:</strong> Thay vì chat chữ (hơn 50 tin nhắn không kết quả), hẹn lên kênh Voice Discord share màn hình, chốt phương án trong 10 phút.</li>
                <li><strong>Lệch pha thời gian (Người làm sáng, người làm đêm):</strong> Áp dụng "Cộng tác bất đồng bộ" (Asynchronous Collaboration) qua Trello. Tag tên kèm link Drive rõ ràng thay vì nhắn tin chờ đợi.</li>
                <li><strong>Ghi đè và mất dữ liệu:</strong> Sử dụng Version History của Google Docs để khôi phục. Sau đó dùng tính năng "Suggesting" và khóa quyền Editor trực tiếp.</li>
            </ol>
            <p><strong>Kết luận:</strong> Việc làm chủ Trello, Discord, Google Docs giúp kiểm soát toàn bộ tiến độ, không rơi vào hoang mang trước deadline.</p>
        """
    },
    "project5.html": {
        "title": "Bài 5: Sáng tạo nội dung số",
        "content": """
            <h1>Nghiên cứu và ứng dụng AI trong Sáng tạo nội dung số</h1>
            
            <h2>1. Tổng quan dự án</h2>
            <p><strong>Chiến dịch:</strong> Content Marketing "Xây dựng lối sống xanh cho Gen Z".</p>
            <p><strong>Công cụ AI sử dụng:</strong></p>
            <ul>
                <li><strong>Google Gemini:</strong> Tạo văn bản, nghiên cứu insight.</li>
                <li><strong>Midjourney:</strong> Tạo concept hình ảnh nghệ thuật.</li>
                <li><strong>Canva AI & Adobe Firefly:</strong> Thiết kế layout và chỉnh sửa ảnh (Generative Fill).</li>
            </ul>

            <h2>2. Quá trình thực hiện</h2>
            <h3>Bước 1: Gemini (Text)</h3>
            <p>Prompt đóng vai chuyên gia Content Marketer phân tích rào cản sống xanh của Gen Z. AI chỉ ra: Chi phí đắt, Bất tiện, Tâm lý FOMO/Greenwashing.</p>
            <p><em>Sự can thiệp cá nhân (50%):</em> Biên tập lại văn phong, thêm các từ lóng (flexing, quá oải) và ví dụ thực tế tại Việt Nam.</p>
            
            <h3>Bước 2: Midjourney (Image)</h3>
            <p>Prompt: <code>A futuristic cyber-organic bedroom of a Gen Z Vietnamese student...</code></p>
            <p>Lựa chọn 1 trong 4 kết quả, đem vào Lightroom chỉnh màu (Color grading) cho đồng bộ brand guidelines.</p>

            <h3>Bước 3: Canva AI & Firefly (Design)</h3>
            <p>Sử dụng Canva Magic Design gợi ý layout Infographic. Dùng Adobe Firefly xóa chi tiết thừa bằng Generative Fill.</p>
            <p>Thay đổi toàn bộ font chữ sang tiếng Việt, vẽ thêm luồng thị giác (Visual Hierarchy).</p>

            <h2>3. Phân tích chuyên sâu & Đạo đức AI</h2>
            <ul>
                <li><strong>Sự thay đổi quy trình:</strong> Từ "Thực thi" sang "Giám sát" (Định hướng -> Lọc lựa -> Tinh chỉnh thủ công). Năng suất tăng 3-4 lần.</li>
                <li><strong>Bản quyền (Copyright):</strong> Midjourney học từ tranh nghệ sĩ chưa có sự đồng thuận. Vì vậy chỉ dùng ở mức Concept, hoàn thiện qua Adobe Firefly (đã mua bản quyền Adobe Stock).</li>
                <li><strong>Thiên vị (AI Bias):</strong> AI mặc định vẽ người da trắng. Phải chủ động thêm từ khóa <code>Vietnamese student</code>, <code>Asian features</code>.</li>
                <li><strong>Trách nhiệm (Hallucination):</strong> Fact-check số liệu môi trường từ báo cáo WWF thay vì tin tuyệt đối vào AI.</li>
            </ul>
        """
    },
    "project6.html": {
        "title": "Bài 6: Sử dụng AI có trách nhiệm",
        "content": """
            <h1>Sử dụng AI có trách nhiệm và đạo đức trong học tập</h1>
            
            <h2>1. Chính sách của nhà trường</h2>
            <ul>
                <li><strong>Thừa nhận công cụ hỗ trợ:</strong> AI (ChatGPT, Copilot) là phương tiện gợi ý, hiệu đính, không thay thế con người.</li>
                <li><strong>Nghiêm cấm đạo văn AI (AI-giarism):</strong> Việc copy-paste nguyên văn bài làm từ AI là gian lận học thuật nghiêm trọng.</li>
                <li><strong>Minh bạch hóa:</strong> Bắt buộc khai báo tường tận công cụ AI đã dùng và mức độ sử dụng trong phần phụ lục.</li>
            </ul>

            <h2>2. Vấn đề đạo đức và Rủi ro</h2>
            <div style="overflow-x: auto;">
            <table>
                <tr>
                    <th>Vấn đề</th>
                    <th>Nguy cơ</th>
                    <th>Ranh giới đúng đắn</th>
                </tr>
                <tr>
                    <td>Gian lận học thuật</td>
                    <td>Thuê phần mềm viết toàn bộ, ủy thác tư duy</td>
                    <td>AI là người phản biện. Quyền quyết định cuối cùng thuộc về sinh viên.</td>
                </tr>
                <tr>
                    <td>Sở hữu trí tuệ</td>
                    <td>Đạo văn vô thức (Unintentional plagiarism)</td>
                    <td>Dùng reverse search để truy vết nguồn gốc, không coi AI là chân lý.</td>
                </tr>
                <tr>
                    <td>Lười tư duy</td>
                    <td>Triệt tiêu tư duy phản biện (Critical thinking)</td>
                    <td>Dùng AI như đối tác tập luyện (Sparring partner) để rèn tư duy logic.</td>
                </tr>
            </table>
            </div>

            <h2>3. Bộ 6 nguyên tắc cá nhân</h2>
            <ol>
                <li><strong>Tư duy độc lập trước (Originality First):</strong> Luôn tự suy nghĩ 15-30 phút để lên ý tưởng cốt lõi trước khi mở ứng dụng AI.</li>
                <li><strong>Nghi ngờ lành mạnh (Healthy Skepticism):</strong> Mọi dữ liệu do AI cung cấp đều là "giả thuyết", cần xác thực bằng tài liệu chính thống.</li>
                <li><strong>Minh bạch tuyệt đối (Radical Transparency):</strong> Công khai câu lệnh, công cụ và mức độ sử dụng trong bài nộp.</li>
                <li><strong>Tỷ lệ vàng 80/20:</strong> AI chỉ chiếm 20% (sửa lỗi, định dạng, dàn ý sơ bộ). 80% (chiều sâu, phản biện) thuộc về chất xám cá nhân.</li>
                <li><strong>Bảo mật dữ liệu (Data Privacy):</strong> Không đưa tài liệu nội bộ, thông tin cá nhân lên AI.</li>
                <li><strong>Sử dụng để học (Growth Mindset):</strong> Dùng AI để hiểu sâu bản chất, không dùng để đối phó điểm số.</li>
            </ol>
        """
    }
}

for filename, data in projects.items():
    html_content = html_template.format(title=data['title'], content=data['content'])
    with open(os.path.join(r"d:\CS_AI\portfolio_web", filename), 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Generated all 6 project files.")
