from page import PageTask

"""PageProcessor class. Calculates page replacement algorithms when provided PageTask objects"""


class PageProcessor:
    #   Returns the index of least recently used task in frame_list
    def least_used_task_in_frame(self, frames: list):
        max_time = 0
        i = 0
        count = 0
        for frame in frames:
            if frame.use_time > max_time:
                max_time = frame.use_time
                i = count
            count += 1
        return i

    #   Updates use time of every task currently in frame_list by 1
    def update_use_time(self, x):
        for frame in x:
            frame.use_time += 1

    #   Calculates frame_list items by incoming_task using LRU algorithm
    def least_recently_used(self, incoming_tasks: list[PageTask], frame_num):
        frame_list = [PageTask(-1, -1)]*frame_num
        page_fault = 0
        page_hit = 0
        for task in incoming_tasks:
            is_repeated = False
            self.update_use_time(frame_list)
            for frame in frame_list:
                if task.value == frame.value:
                    frame_list[frame_list.index(frame)].use_time = 0
                    is_repeated = True
                    page_hit += 1
                    break
            if is_repeated == False:
                least = self.least_used_task_in_frame(frame_list)
                frame_list[least] = task
                page_fault += 1
        return [page_fault, page_hit]

    #   Calculates frame_list items by incoming_task using FIFO algorithm
    def first_in_first_out(self, incoming_tasks: list[PageTask], frame_num) -> list[float, float]:
        frame_list = [PageTask(-1, -1)]*frame_num
        current_frame_index = 0
        page_fault = 0
        page_hit = 0
        for task in incoming_tasks:
            is_hit = False
            for frame in frame_list:
                if task.value == frame.value:
                    page_hit += 1
                    is_hit = True
                    break
            if is_hit == False:
                frame_list[current_frame_index] = task
                current_frame_index += 1
                if current_frame_index > frame_num-1:
                    current_frame_index = 0
                page_fault += 1
        return [page_fault, page_hit]
