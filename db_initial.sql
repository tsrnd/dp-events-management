-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_group (
    id SERIAL PRIMARY KEY,
    groupname character varying(100) NOT NULL,
    rootid integer
);
COMMENT ON COLUMN tbl_group.groupname IS 'Tên nhóm không được phép trùng nhau trên cùng 1 level(Group riêng hoặc là group trong cùng tổ chức)';
COMMENT ON COLUMN tbl_group.rootid IS 'Trong trường hợp nhóm này thuộc 1 tổ chức(Group) thì phải thiết lập giá trị cha của nó.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_group_pkey ON tbl_group(id int4_ops);

-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_group_user (
    id SERIAL PRIMARY KEY,
    userid integer NOT NULL REFERENCES auth_user(id),
    groupid integer NOT NULL REFERENCES tbl_group(id),
    "isDelete" boolean NOT NULL DEFAULT false
);
COMMENT ON COLUMN tbl_group_user.userid IS 'Account login.';
COMMENT ON COLUMN tbl_group_user.groupid IS 'Liên kết với Group.';
COMMENT ON COLUMN tbl_group_user."isDelete" IS 'Thiết lập cờ cho trường hợp xoá mềm.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_group_user_pkey ON tbl_group_user(id int4_ops);

-- Table Definition ----------------------------------------------

CREATE TABLE IF NOT EXISTS tbl_invite_member (
    id SERIAL PRIMARY KEY,
    owner integer NOT NULL REFERENCES auth_user(id),
    userid integer NOT NULL REFERENCES auth_user(id),
    invite_link text,
    time_create timestamp with time zone,
    expire_time timestamp with time zone,
    "isConfirm" boolean NOT NULL DEFAULT false,
    invite_type smallint NOT NULL,
    "isDelete" boolean NOT NULL DEFAULT false
);
COMMENT ON COLUMN tbl_invite_member.invite_type IS '- 1: Invite join event. - 2: Invite join group. - 0: Other.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_invite_member_pkey ON tbl_invite_member(id int4_ops);

-- Table Definition ----------------------------------------------

CREATE TABLE IF NOT EXISTS tbl_events (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    start_date date NOT NULL,
    start_time time with time zone,
    end_date date NOT NULL,
    end_time time with time zone,
    "isDaily" boolean NOT NULL DEFAULT false,
    "isAllday" boolean NOT NULL DEFAULT false,
    location text,
    "isNotification" boolean DEFAULT false,
    "timeNotification" character varying(20),
    owner integer NOT NULL,
    event_content text,
    file_attack text,
    guest_can_invite boolean NOT NULL DEFAULT true,
    view_all_guest boolean NOT NULL DEFAULT true,
    item_preparing text,
    "isCancel" boolean NOT NULL DEFAULT false,
    "isDelete" boolean NOT NULL DEFAULT false,
    time_create timestamp with time zone NOT NULL,
    last_edit timestamp with time zone NOT NULL,
    user_edit integer NOT NULL
);
COMMENT ON COLUMN tbl_events.title IS 'Tiêu đề giới thiệu cho sự kiện sắp diễn ra.';
COMMENT ON COLUMN tbl_events.start_date IS 'Ngày bắt đầu.';
COMMENT ON COLUMN tbl_events.start_time IS 'Giờ bắt đầu.';
COMMENT ON COLUMN tbl_events.end_date IS 'Ngày kết thúc.';
COMMENT ON COLUMN tbl_events.end_time IS 'Giờ kết thúc.';
COMMENT ON COLUMN tbl_events."isDaily" IS 'Có phải là diễn ra hàng ngày hay không?';
COMMENT ON COLUMN tbl_events."isAllday" IS 'Sự kiện có diễn ra cả ngày hay không? Trường hợp là True thì phải thiết lập start_time và end_time là null.';
COMMENT ON COLUMN tbl_events.location IS 'Địa điểm diễn ra sự kiện (sẽ xác định bằng Google Map API)';
COMMENT ON COLUMN tbl_events."isNotification" IS 'Có thông báo trước khi diễn ra sự kiện hay không?';
COMMENT ON COLUMN tbl_events."timeNotification" IS 'Thời gian thông báo trước khi diễn ra sự kiện. -m  -h -d.';
COMMENT ON COLUMN tbl_events.owner IS 'Người tạo ra sự kiện.';
COMMENT ON COLUMN tbl_events.event_content IS 'Giới thiệu về sự kiện / lịch sử / ý nghĩa của sự kiện.';
COMMENT ON COLUMN tbl_events.file_attack IS 'Danh sách địa chỉ đầy đủ của các file đính kèm. Có thể là list được bố trí theo dạng XML(khá khó xử lý)';
COMMENT ON COLUMN tbl_events.guest_can_invite IS 'Cho phép những người trong ban tổ chức được phép mời người khác.';
COMMENT ON COLUMN tbl_events.view_all_guest IS 'Cho phép những người trong ban tổ chức có thể xem tất cả những người còn lại. (Không có chức năng xem tất cả các member joined)';
COMMENT ON COLUMN tbl_events.item_preparing IS 'Những trang bị cần chuẩn bị trước. Bố trí theo dạng Checkbox để kiểm tra.';
COMMENT ON COLUMN tbl_events."isCancel" IS 'Sự kiện bị huỷ vì lý do nào đó.';
COMMENT ON COLUMN tbl_events."isDelete" IS 'Thiết lập cờ cho trường hợp xoá mềm.';
COMMENT ON COLUMN tbl_events.last_edit IS 'Thời điểm chỉnh sửa gần nhất.';
COMMENT ON COLUMN tbl_events.user_edit IS 'Người chỉnh sửa cuối cùng.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_events_pkey ON tbl_events(id int4_ops);

-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_events_history (
    id SERIAL PRIMARY KEY,
    title character varying(200) NOT NULL,
    start_date date NOT NULL,
    start_time time with time zone,
    end_date date NOT NULL,
    end_time time with time zone,
    "isDaily" boolean NOT NULL DEFAULT false,
    "isAllday" boolean NOT NULL DEFAULT false,
    location text,
    "isNotification" boolean DEFAULT false,
    "timeNotification" character varying(20),
    owner integer NOT NULL,
    event_content text,
    file_attack text,
    guest_can_invite boolean NOT NULL DEFAULT true,
    view_all_guest boolean NOT NULL DEFAULT true,
    item_preparing text,
    "isCancel" boolean NOT NULL DEFAULT false,
    "isDelete" boolean NOT NULL DEFAULT false,
    time_create timestamp with time zone NOT NULL,
    last_edit timestamp with time zone NOT NULL,
    user_edit integer NOT NULL,
    event_id integer NOT NULL REFERENCES tbl_events(id)
);
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_events_history_pkey ON tbl_events_history(id int4_ops);


-- Table Definition ----------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_event_members (
    id integer DEFAULT nextval('tbl_event_guests_id_seq'::regclass) PRIMARY KEY,
    event_id integer NOT NULL REFERENCES tbl_events(id),
    user_id integer NOT NULL REFERENCES auth_user(id),
    "isGoing" boolean NOT NULL DEFAULT false,
    "isDelete" boolean DEFAULT false,
    invite_id integer
);
COMMENT ON COLUMN tbl_event_members.event_id IS 'Sự kiện cho phép add thêm người tham gia.';
COMMENT ON COLUMN tbl_event_members.user_id IS 'Liên kết với table user để lấy thông tin cụ thể.';
COMMENT ON COLUMN tbl_event_members."isGoing" IS 'Xác nhận trạng thái tham gia của các thành viên. Mặc định khi chưa confirm sẽ là FALSE.';
COMMENT ON COLUMN tbl_event_members."isDelete" IS 'Cờ trạng thái cho trường hợp xoá mềm.';
COMMENT ON COLUMN tbl_event_members.invite_id IS 'Ghi nhận tham gia sự kiện thông qua lời mời.';
-- Indices -------------------------------------------------------
CREATE UNIQUE INDEX tbl_event_guests_pkey ON tbl_event_members(id int4_ops);

