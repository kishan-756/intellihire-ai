import json

questions_db = {
    "aptitude": [
        {"question": "A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?", "options": ["120 metres", "180 metres", "324 metres", "150 metres"], "answer": "150 metres"},
        {"question": "The angle of elevation of a ladder leaning against a wall is 60° and the foot of the ladder is 4.6 m away from the wall. The length of the ladder is:", "options": ["2.3 m", "4.6 m", "7.8 m", "9.2 m"], "answer": "9.2 m"},
        {"question": "A sum of money at simple interest amounts to Rs. 815 in 3 years and to Rs. 854 in 4 years. The sum is:", "options": ["Rs. 650", "Rs. 690", "Rs. 698", "Rs. 700"], "answer": "Rs. 698"},
        {"question": "Three unbiased coins are tossed. What is the probability of getting at most two heads?", "options": ["3/4", "1/4", "3/8", "7/8"], "answer": "7/8"},
        {"question": "Two numbers are respectively 20% and 50% more than a third number. The ratio of the two numbers is:", "options": ["2:5", "3:5", "4:5", "6:7"], "answer": "4:5"},
        {"question": "A fruit seller had some apples. He sells 40% apples and still has 420 apples. Originally, he had:", "options": ["588 apples", "600 apples", "672 apples", "700 apples"], "answer": "700 apples"},
        {"question": "What percentage of numbers from 1 to 70 have 1 or 9 in the unit's digit?", "options": ["1", "14", "20", "21"], "answer": "20"},
        {"question": "If A = x% of y and B = y% of x, then which of the following is true?", "options": ["A is smaller than B", "A is greater than B", "Relationship can't be determined", "If x is smaller than y, then A is greater than B", "None of these (A=B)"], "answer": "None of these (A=B)"},
        {"question": "In a certain store, the profit is 320% of the cost. If the cost increases by 25% but the selling price remains constant, approximately what percentage of the selling price is the profit?", "options": ["30%", "70%", "100%", "250%"], "answer": "70%"},
        {"question": "A vendor bought toffees at 6 for a rupee. How many for a rupee must he sell to gain 20%?", "options": ["3", "4", "5", "6"], "answer": "5"},
        {"question": "The cost price of 20 articles is the same as the selling price of x articles. If the profit is 25%, then the value of x is:", "options": ["15", "16", "18", "25"], "answer": "16"},
        {"question": "A boat can travel with a speed of 13 km/hr in still water. If the speed of the stream is 4 km/hr, find the time taken by the boat to go 68 km downstream.", "options": ["2 hours", "3 hours", "4 hours", "5 hours"], "answer": "4 hours"},
        {"question": "A man's speed with the current is 15 km/hr and the speed of the current is 2.5 km/hr. The man's speed against the current is:", "options": ["8.5 km/hr", "9 km/hr", "10 km/hr", "12.5 km/hr"], "answer": "10 km/hr"},
        {"question": "A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is:", "options": ["1/4", "1/10", "7/15", "8/15"], "answer": "8/15"},
        {"question": "A is twice as good a workman as B and together they finish a piece of work in 18 days. In how many days will A alone finish the work?", "options": ["27", "28", "29", "30"], "answer": "27"},
        {"question": "A sum of money becomes 7/6 of itself in 3 years at a certain rate of simple interest. The rate per annum is:", "options": ["5 5/9%", "6 5/9%", "18%", "25%"], "answer": "5 5/9%"},
        {"question": "Present ages of Sameer and Anand are in the ratio of 5 : 4 respectively. Three years hence, the ratio of their ages will become 11 : 9 respectively. What is Anand's present age in years?", "options": ["24", "27", "40", "Cannot be determined"], "answer": "24"},
        {"question": "Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together?", "options": ["4", "10", "15", "16"], "answer": "16"},
        {"question": "The sum of the digits of a two-digit number is 15 and the difference between the digits is 3. What is the two-digit number?", "options": ["69", "78", "96", "Cannot be determined"], "answer": "Cannot be determined"},
        {"question": "If 20% of a = b, then b% of 20 is the same as:", "options": ["4% of a", "5% of a", "20% of a", "None of these"], "answer": "4% of a"}
    ],
    "dsa": [
        {"difficulty": "easy", "question": "Reverse a linked list: Write a function to reverse a singly linked list in-place.", "reference_answer": "Initialize three pointers: prev as NULL, curr as head, and next as NULL. Iterate through the list, temporarily storing curr->next, then pointing curr->next to prev. Move prev to curr and curr to next. Finally, return prev as the new head."},
        {"difficulty": "easy", "question": "Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.", "reference_answer": "Use a hash map. Iterate through the array. For each element, check if (target - element) exists in the hash map. If it does, return the two indices. If not, add the element and its index to the hash map."},
        {"difficulty": "easy", "question": "Valid Parentheses: Check if a string of brackets is valid.", "reference_answer": "Use a stack. Push opening brackets onto the stack. For closing brackets, pop the top of the stack and check if it matches. Unmatched brackets or an empty stack at the end indicate invalid input."},
        {"difficulty": "medium", "question": "Detect cycle in a linked list.", "reference_answer": "Use Floyd's tortoise and hare algorithm. Have a slow pointer moving one step and a fast pointer moving two steps. If they ever intersect, there is a cycle."},
        {"difficulty": "medium", "question": "Longest Substring Without Repeating Characters: Find the length of the longest substring without repeating characters.", "reference_answer": "Use the Sliding Window technique with a set or a map. Expand the window by adding characters to the set. If a duplicate is found, shrink the window from the left until the duplicate is removed. Track the maximum window size."},
        {"difficulty": "medium", "question": "Number of Islands: Given a grid of 1s (land) and 0s (water), count the number of islands.", "reference_answer": "Iterate through the grid. When a '1' is found, increment the island count and trigger a DFS/BFS to mark all connected '1's as visited (or turn them to '0')."},
        {"difficulty": "hard", "question": "Implement LRU Cache: Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.", "reference_answer": "Use a combination of a Hash Map (for O(1) lookups) and a Doubly Linked List (for O(1) insertions, deletions, and moves to the head). The hash map keys point to the nodes in the linked list."},
        {"difficulty": "hard", "question": "Merge K Sorted Lists: Given an array of k linked-lists, each sorted in ascending order. Merge all the linked-lists into one sorted list.", "reference_answer": "Use a priority queue (min-heap). Push the head of each list into the heap. Extract the minimum node, append it to the result list, and if the extracted node has a next node, push it into the heap. Repeat until the heap is empty."},
        {"difficulty": "hard", "question": "Trapping Rain Water: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.", "reference_answer": "Use two pointers, left and right. Keep track of max_left and max_right. Move the pointer with the smaller max height inward, adding max_left - height[left] or max_right - height[right] to the total water."}
    ],
    "technical": {
        "python": [
            {"question": "Explain the difference between deep and shallow copy in Python.", "reference_answer": "A shallow copy constructs a new compound object and then inserts references into it to the objects found in the original. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."},
            {"question": "What are decorators in Python and how do they work?", "reference_answer": "Decorators are functions that take another function as an argument and extend its behavior without explicitly modifying it. They use the @wrapper syntax."},
            {"question": "Explain the Global Interpreter Lock (GIL) in Python.", "reference_answer": "The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This simplifies CPython implementation but limits multi-threading performance for CPU-bound tasks."},
            {"question": "How is memory managed in Python?", "reference_answer": "Python uses reference counting along with a garbage collector that detects and cleans up cyclical references. Memory allocation is mostly handled by Python's memory manager."},
            {"question": "What is the difference between list append() and list extend()?", "reference_answer": "append() adds a single element to the end of the list. extend() iterates over its argument and adds each element to the list, extending the list by multiple elements."}
        ],
        "java": [
            {"question": "Explain the difference between == and .equals() in Java.", "reference_answer": "== compares object references (memory addresses) to check if they point to the same object. .equals() is a method that can be overridden to compare the actual contents or state of objects."},
            {"question": "What is the difference between an Abstract Class and an Interface?", "reference_answer": "An abstract class can have state (instance variables) and implementations, while an interface (prior to Java 8) only defines method signatures. A class can implement multiple interfaces but extend only one abstract class."},
            {"question": "How does Garbage Collection work in Java?", "reference_answer": "Java's Garbage Collector automatically deallocates memory for objects that are no longer reachable from any GC roots. It typically uses generational garbage collection (Young, Old, Permanent/Metaspace)."},
            {"question": "Explain the concepts of HashMap and ConcurrentHashMap.", "reference_answer": "HashMap is non-synchronized and not thread-safe. ConcurrentHashMap is thread-safe and designed for concurrent updates, locking only segments of the map instead of the whole object."},
            {"question": "What are the core concepts of OOP in Java?", "reference_answer": "Encapsulation (hiding state), Inheritance (code reuse), Polymorphism (interfaces/overriding), and Abstraction (hiding implementation details)."}
        ],
        "sql": [
            {"question": "Explain the difference between INNER JOIN and LEFT JOIN.", "reference_answer": "INNER JOIN returns only the rows that have matching values in both tables. LEFT JOIN returns all rows from the left table, and the matched rows from the right table (or NULLs if no match)."},
            {"question": "What is the difference between WHERE and HAVING?", "reference_answer": "WHERE filters rows before any grouping is done. HAVING filters aggregated data after the GROUP BY clause has been applied."},
            {"question": "What are indexes, and how do they improve database performance?", "reference_answer": "Indexes are data structures (like B-trees) that store references to data blocks, allowing the database engine to quickly narrow down the rows to examine without a full table scan, speeding up SELECT queries."},
            {"question": "Explain normalization and its normal forms (1NF, 2NF, 3NF).", "reference_answer": "Normalization organizes data to reduce redundancy. 1NF ensures atomic values. 2NF removes partial dependencies on a composite key. 3NF removes transitive dependencies (non-key attributes depending on other non-key attributes)."},
            {"question": "What is a transaction and the ACID properties?", "reference_answer": "A transaction is a logical unit of work. ACID stands for Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent operations don't interfere), and Durability (committed data is saved)."}
        ],
        "docker": [
            {"question": "Explain the difference between a Docker image and a container.", "reference_answer": "A Docker image is a read-only template containing instructions for creating a Docker container. A container is a runnable, isolated instance of an image."},
            {"question": "What is a Dockerfile?", "reference_answer": "A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image."},
            {"question": "How do Docker volumes work?", "reference_answer": "Volumes are the preferred mechanism for persisting data generated by and used by Docker containers. They are stored on the host filesystem outside the container's copy-on-write filesystem."},
            {"question": "What is Docker Compose?", "reference_answer": "Docker Compose is a tool for defining and running multi-container Docker applications using a YAML file to configure application services."},
            {"question": "Explain the difference between ADD and COPY in a Dockerfile.", "reference_answer": "COPY only copies files from the build context to the container. ADD can also extract tar files and download files from URLs."}
        ],
        "kubernetes": [
            {"question": "What is a Pod in Kubernetes?", "reference_answer": "A Pod is the smallest deployable computing unit in Kubernetes. It encapsulates one or more containers that share storage/network resources and a specification for how to run the containers."},
            {"question": "Explain the role of a Deployment in Kubernetes.", "reference_answer": "A Deployment provides declarative updates for Pods and ReplicaSets. It manages the rollout of new versions, scaling, and rolling back if necessary."},
            {"question": "What is a Kubernetes Service?", "reference_answer": "A Service is an abstraction that defines a logical set of Pods and a policy by which to access them. It provides a stable IP address and DNS name to access dynamically changing Pods."},
            {"question": "How does Kubernetes handle self-healing?", "reference_answer": "Kubernetes automatically restarts containers that fail, replaces and reschedules containers when nodes die, kills containers that don't respond to user-defined health checks (liveness probes)."},
            {"question": "Explain the difference between a NodePort and a LoadBalancer service.", "reference_answer": "NodePort opens a specific port on every Node's IP to route traffic to the Service. LoadBalancer provisions a cloud provider's external load balancer to route traffic to the Service."}
        ],
        "react": [
            {"question": "Explain the Virtual DOM and how React uses it.", "reference_answer": "The Virtual DOM is an in-memory representation of the real DOM. React compares the current Virtual DOM with an updated Virtual DOM (diffing), calculates the minimal set of changes required, and applies only those changes to the real DOM (reconciliation)."},
            {"question": "What are React Hooks?", "reference_answer": "Hooks are functions that let you 'hook into' React state and lifecycle features from function components. Examples include useState, useEffect, and useContext."},
            {"question": "Explain the difference between state and props.", "reference_answer": "Props (properties) are passed to a component from its parent and are read-only. State is managed within the component and can change over time in response to user actions or network responses."},
            {"question": "What is useEffect used for?", "reference_answer": "useEffect is used to perform side effects in function components, such as data fetching, subscriptions, or manually changing the DOM. It replaces lifecycle methods like componentDidMount and componentDidUpdate."},
            {"question": "How does React Context work?", "reference_answer": "React Context provides a way to pass data through the component tree without having to pass props down manually at every level, solving the 'prop drilling' problem for global data."}
        ],
        "node": [
            {"question": "Explain the Node.js Event Loop.", "reference_answer": "The Event Loop is what allows Node.js to perform non-blocking I/O operations, despite being single-threaded, by offloading operations to the system kernel whenever possible."},
            {"question": "What is the difference between process.nextTick() and setImmediate()?", "reference_answer": "process.nextTick() callbacks fire immediately on the same phase of the event loop before returning to the event loop. setImmediate() fires on the following iteration or 'tick' of the event loop, specifically in the check phase."},
            {"question": "How do streams work in Node.js?", "reference_answer": "Streams are objects that let you read data from a source or write data to a destination in continuous fashion. There are four types: Readable, Writable, Duplex, and Transform. They help handle large amounts of data efficiently."},
            {"question": "Explain the role of package.json.", "reference_answer": "package.json holds metadata relevant to the project, manages project dependencies, configuration, scripts, and versions."},
            {"question": "What is middleware in Express.js?", "reference_answer": "Middleware functions are functions that have access to the request object, response object, and the next middleware function in the application’s request-response cycle. They can execute code, modify req/res, and end the cycle."}
        ],
        "data structures": [
            {"question": "Compare an Array and a Linked List.", "reference_answer": "Arrays have contiguous memory allocation, O(1) read access, but O(N) insertion/deletion. Linked Lists have non-contiguous memory, O(N) read access, but O(1) insertion/deletion if the node reference is known."},
            {"question": "What is a Hash Table?", "reference_answer": "A Hash Table is a data structure that implements an associative array abstract data type. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found in O(1) average time."},
            {"question": "Explain the concept of a Binary Search Tree (BST).", "reference_answer": "A BST is a tree where each node has at most two children. The left child contains a value less than the parent, and the right child contains a value greater than the parent, allowing O(log N) search times on average."},
            {"question": "What is a Stack and a Queue?", "reference_answer": "A Stack is a LIFO (Last-In-First-Out) data structure. A Queue is a FIFO (First-In-First-Out) data structure."},
            {"question": "What is a Graph and what are its representations?", "reference_answer": "A Graph consists of vertices and edges. It can be represented using an Adjacency Matrix (2D array) or an Adjacency List (array of lists/arrays)."}
        ],
        "algorithms": [
            {"question": "Explain Quicksort.", "reference_answer": "Quicksort is a divide-and-conquer algorithm. It picks a 'pivot' element, partitions the array into elements less than and greater than the pivot, and recursively sorts the sub-arrays. Average time complexity is O(N log N)."},
            {"question": "Explain Binary Search.", "reference_answer": "Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one."},
            {"question": "What is Dynamic Programming?", "reference_answer": "Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems. It solves each subproblem just once and stores its answer (memoization or tabulation) to avoid re-computation."},
            {"question": "Explain the concept of Greedy Algorithms.", "reference_answer": "Greedy algorithms make the locally optimal choice at each stage with the hope of finding a global optimum. Examples include Dijkstra's algorithm and Kruskal's algorithm."},
            {"question": "What is the Time Complexity of Merge Sort?", "reference_answer": "Merge Sort consistently has a Time Complexity of O(N log N) in all cases (worst, average, and best) because it always divides the array into two halves and takes linear time to merge two halves."}
        ]
    },
    "hr": [
        {"question": "Tell me about yourself.", "reference_answer": "Provide a brief summary of your professional background, current role, key achievements, and what direction you want your career to move in. Focus on experiences relevant to the job."},
        {"question": "Why do you want to work for this company?", "reference_answer": "Demonstrate knowledge about the company's products/services, culture, or recent achievements. Connect their goals with your own career aspirations and skills."},
        {"question": "What are your greatest strengths?", "reference_answer": "Highlight 2-3 strengths that are highly relevant to the role. Back them up with specific examples from your past work experience."},
        {"question": "What is your biggest weakness?", "reference_answer": "Choose a real but resolvable weakness that is not a critical requirement for the job. Explain what steps you are actively taking to improve upon it."},
        {"question": "Describe a challenging situation you faced at work and how you handled it.", "reference_answer": "Use the STAR method (Situation, Task, Action, Result). Focus on a situation that showed your problem-solving skills, resilience, or leadership."},
        {"question": "Where do you see yourself in 5 years?", "reference_answer": "Show ambition but keep it realistic and aligned with the company and the role you're applying for. Focus on acquiring skills and taking on more responsibility."},
        {"question": "Why should we hire you?", "reference_answer": "Summarize how your skills, experience, and attitude make you uniquely qualified for the role and how you will add value to the team."},
        {"question": "Can you explain a time you disagreed with a coworker or manager?", "reference_answer": "Focus on your communication and conflict resolution skills. Show that you can handle disagreements professionally, listen to others, and work towards a productive compromise."},
        {"question": "What is your greatest professional achievement?", "reference_answer": "Share an achievement using the STAR method that highlights your impact, whether it's saving money, improving a process, or leading a successful project."},
        {"question": "Do you have any questions for us?", "reference_answer": "Always say yes. Ask thoughtful questions about the team dynamics, company culture, expectations for the first 90 days, or the company's future plans."}
    ]
}

with open("backend/questions.json", "w") as f:
    json.dump(questions_db, f, indent=4)
print("questions.json successfully generated!")
